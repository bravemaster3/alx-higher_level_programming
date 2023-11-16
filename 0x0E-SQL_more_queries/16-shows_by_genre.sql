-- script that lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres sg ON sg.genre_id = tv_genres.id
RIGHT JOIN tv_shows ON sg.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
