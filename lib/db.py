import psycopg2
import psycopg2.extras

log = logging.getLogger(__name__)


def get_db(db_name, **kwargs):
    return DBFactory().get_db(db_name, **kwargs)

def load_db_config():
    try:
        database_yaml_path = (os.environ.get('DATABASE_YAML_PATH') or '/tmp/database.yml')
        with open(database_yaml_path) as db_file:
            db_config = yaml.load(db_file)
        return db_config
    except IOError:
        error_str = 'It seems that you do not have the database.yml file at: {}'.format(database_yaml_path)
        raise IOError(error_str)


class PostgresDB(object):

    def __init__(self, database, host, username, password, port,
                 autocommit=True,
                 cursorclass=psycopg2.extras.DictCursor):
        self.database = database
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.autocommit = autocommit
        self.cursorclass = cursorclass
        self._connect()

    def _connect(self):
        # pulled out to support reconnection
        self.conn = self.DbClass.connect(
                        database=self.database, 
                        user=self.username, 
                        password=self.password,
                        host=self.host, 
                        port=self.port,
                        cursor_factory=self.cursorclass)
        self.conn.autocommit = self.autocommit
        self.cursor = self.conn.cursor()

    def execute(self, query, args=None):
        """
        We have had trouble with the DB going away, that will raise an
        InterfaceError.  Catch that error and retry once.
        """
        try:
            return self.cursor.execute(query, args)
        except psycopg2.InterfaceError:
            log.warn("Caught Postgres InterfaceError, reconnecting and retrying")
            self._connect()
            return self.cursor.execute(query, args)


class DBFactory(object): 

    def __init__(self):
        self.db_config = load_db_config()

    def get_db_class(self, config):
        adapter = config.get('adapter', 'postgresql')
        if adapter.startswith('postgresql'):
            return PostgresDB
        else:
            raise Exception("Unknown adapter name, not gonna try to guess this one")

    def get_db(self, db_name, **kwargs):
        file_config = self.db_config[db_name]
        DatabaseClass = self.get_db_class(file_config)
        connect_params = ['database', 'host', 'username', 'password', 'port']
        config = {k: file_config[k] for k in connect_params}
        config.update(kwargs)
        db = DatabaseClass(**config)
        return db
