-- Script that creates the table unique_id.
-- id has a default value of 1 and must be unique.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
