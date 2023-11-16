-- All genres of tv_show Dexter JOIN 3 tables
SELECT DISTINCT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
JOIN tv_shows
ON tv_show_genres.genre_id = tv_genres.id AND tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;
