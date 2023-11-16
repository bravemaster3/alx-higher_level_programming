-- Script that lists all Comedy shows in the database
SELECT DISTINCT tv_shows.title
FROM tv_genres
JOIN tv_show_genres sg
JOIN tv_shows
ON sg.genre_id = tv_genres.id AND sg.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
