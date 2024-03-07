-- Lists all cities contained in the database hbtn_0d_usa.

-- SELECT cities.id, cities.name FROM cities
-- LEFT JOIN 
-- ON states.name='San Francisco'
-- ORDER BY cities.id ASC;

SELECT cities.id, cities.name, states.name 
FROM cities
JOIN states 
ON cities.id = states.id
ORDER BY cities.id ASC;
