-- This script will list all genres from database --
-- hbtn_0d_tvshows --
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_shows'
FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_shows DESC;

