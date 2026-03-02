-- Count records grouped by score in second_table
-- Returns each score and its number of records sorted by count descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
