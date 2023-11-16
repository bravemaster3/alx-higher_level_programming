-- script that lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
FROM tv_genres
JOIN tv_show_genres sg
JOIN tv_shows
WHERE sg.genre_id = tv_genres.id AND sg.show_id = tv_shows.id
ORDER BY title ASC, name ASC;
