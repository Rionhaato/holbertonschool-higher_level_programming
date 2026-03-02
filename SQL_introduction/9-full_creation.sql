-- Create second_table and add initial records
-- Creates second_table with id, name, and score when missing
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserts John with score 10
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);

-- Inserts Alex with score 3
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);

-- Inserts Bob with score 14
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);

-- Inserts George with score 8
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
