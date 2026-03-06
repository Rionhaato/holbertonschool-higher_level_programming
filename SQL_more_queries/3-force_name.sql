-- Script that creates the table force_name.
-- name must be VARCHAR(256) and cannot be NULL.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
