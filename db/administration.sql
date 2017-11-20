create role developer;
alter role developer with password '{password}';
ALTER ROLE developer VALID UNTIL 'infinity';
alter role developer with LOGIN
create database development owner developer;
-- GRANT LOGIN ON DATABASE development TO developer
-- GRANT CONNECT ON DATABASE development TO developer
grant all privileges on database development to developer;

create database production owner developer;
grant all privileges on database production to developer;