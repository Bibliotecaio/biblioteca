CREATE USER biblioteca WITH password '123456';
ALTER USER biblioteca CREATEDB;
CREATE DATABASE biblioteca;
GRANT ALL privileges ON DATABASE biblioteca TO biblioteca;
