-- List all genres not linked to the show Dexter

SELECT DISTINCT tg.name
  FROM tv_genres AS tg
		INNER JOIN tv_show_genres AS tsg
		ON tsg.genre_id = tg.id
 WHERE tg.name NOT IN (
			   SELECT tg.name
 			   FROM tv_genres AS tg
		           	INNER JOIN tv_show_genres AS tsg
				ON tsg.genre_id = tg.id

				INNER JOIN tv_shows AS ts
				ON ts.id = tsg.show_id
 			   WHERE ts.title = 'Dexter'
		)

 ORDER BY tg.name;
