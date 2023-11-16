-- script that lists all genres in the database
-- hbtn_0d_tvshows_rate by their rating
SELECT g.name, SUM(sr.rate) as rating
FROM tv_genres g
JOIN tv_show_genres sg ON sg.genre_id = g.id
JOIN tv_show_ratings sr ON sg.show_id = sr.show_id
GROUP BY g.name
ORDER BY rating DESC;
