-- List all Comedy shows in the database

SELECT ts.title
  FROM tv_genres AS tg
		INNER JOIN tv_show_genres AS tsg
		ON tsg.genre_id = tg.id

		INNER JOIN tv_shows AS ts
		ON ts.id = tsg.show_id
 WHERE tg.name = 'Comedy'
 ORDER BY ts.title;
