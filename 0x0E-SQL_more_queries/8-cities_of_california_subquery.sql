-- This script will lists all cities of California --
-- cities, state_id --

SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

