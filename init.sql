DROP TABLE IF EXISTS dbwork_file;
CREATE TABLE dbwork_file (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    data BYTEA NOT NULL
);