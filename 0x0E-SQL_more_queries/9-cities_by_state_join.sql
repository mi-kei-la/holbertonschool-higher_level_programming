-- Show all cities with their state using a join.
SELECT
	cities.id AS id,
	cities.name AS name,
	states.name AS name
FROM
	cities
LEFT JOIN
	states ON cities.state_id = states.id
ORDER BY
	cities.id ASC;

