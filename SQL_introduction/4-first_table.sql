-- Create the table first_table in the current database
-- Creates first_table with columns id and name when missing
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
