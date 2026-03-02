-- List records from second_table where name contains a value
-- Selects score and name sorted by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
