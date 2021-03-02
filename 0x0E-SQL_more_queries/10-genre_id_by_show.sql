-- Display all shows with a genre id.
SELECT
	tv_shows.title AS title,
	tv_show_genres.genre_id AS genre_id
FROM
	tv_shows
INNER JOIN
	tv_show_genres
ON
	tv_show_genres.show_id = tv_shows.id
ORDER BY
	tv_shows.title,
	tv_show_genres.genre_id
;

