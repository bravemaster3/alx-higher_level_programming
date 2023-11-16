-- All shows without genre Comedy
SELECT title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT sg.show_id
    FROM tv_show_genres sg
    JOIN  tv_genres g ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
)
ORDER BY title ASC;
