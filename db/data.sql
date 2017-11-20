create schema data;
grant ALL PRIVILEGES on all tables in schema data to developer;
grant ALL PRIVILEGES on all sequences in schema data to developer;
GRANT ALL PRIVILEGES ON SCHEMA data TO developer;
ALTER DEFAULT PRIVILEGES IN SCHEMA data GRANT ALL ON TABLES TO developer;
ALTER DEFAULT PRIVILEGES FOR ROLE developer IN SCHEMA data GRANT ALL ON TABLES TO developer;
ALTER DEFAULT PRIVILEGES FOR ROLE developer IN SCHEMA data GRANT ALL ON SEQUENCES TO developer;

create table data.profiles (
    id serial not null primary key,
    document_id varchar(64) not null,
    document jsonb,
    checksum varchar(255),
    created_at timestamp not null default CURRENT_TIMESTAMP,
);
CREATE UNIQUE INDEX document_id_created_at_idx ON licenses.profiles (document_id, created_at);
create index profiles_created_at_idx on licenses.profiles (created_at);