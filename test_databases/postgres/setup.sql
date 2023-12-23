CREATE SCHEMA dbo;

CREATE TABLE dbo.staging_person(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(25) NOT NULL,
    age INT NOT NULL
);