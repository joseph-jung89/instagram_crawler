create schema operations;
grant ALL PRIVILEGES on all tables in schema operations to developer;
grant ALL PRIVILEGES on all sequences in schema operations to developer;
GRANT ALL PRIVILEGES ON SCHEMA operations TO developer;
ALTER DEFAULT PRIVILEGES IN SCHEMA operations GRANT ALL ON TABLES TO developer;
ALTER DEFAULT PRIVILEGES FOR ROLE developer IN SCHEMA operations GRANT ALL ON TABLES TO developer;
ALTER DEFAULT PRIVILEGES FOR ROLE developer IN SCHEMA operations GRANT ALL ON SEQUENCES TO developer;

CREATE TABLE if not exists operations.crawl_logs (
  id serial not null primary key,
  entity_type varchar(64) not null,
  source varchar(64) not null,
  result varchar(256) DEFAULT NULL,
  start_time timestamp NOT NULL,
  end_time timestamp DEFAULT NULL
);