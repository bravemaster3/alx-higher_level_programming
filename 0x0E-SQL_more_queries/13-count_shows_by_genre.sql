-- Number of shows by genre LEFT JOIN GROUP BY and count
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) as number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
