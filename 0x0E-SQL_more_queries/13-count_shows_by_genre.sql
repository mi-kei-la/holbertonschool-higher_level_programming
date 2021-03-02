-- List genres by number of shows.
SELECT
	tv_genres.name AS genre,
	count(tv_show_genres.show_id) AS number_of_shows
FROM
	tv_genres
RIGHT JOIN
	tv_show_genres
ON
	tv_genres.id = tv_show_genres.genre_id
GROUP BY
	tv_genres.name
HAVING
	count(tv_show_genres.show_id)
ORDER BY
	count(tv_show_genres.show_id) DESC;

