-- Selection of rows with a name value,
-- only score and name, descending svore
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
