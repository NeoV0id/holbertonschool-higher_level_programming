-- This script will list all cities of database cities --
-- cities --
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER by cities.id ASC;

