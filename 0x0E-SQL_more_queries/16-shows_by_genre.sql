-- List all shows, and all genres linked to that show

SELECT ts.title, tg.name
  FROM tv_genres AS tg
		INNER JOIN tv_show_genres AS tsg
		ON tsg.genre_id = tg.id

		RIGHT JOIN tv_shows AS ts
		ON ts.id = tsg.show_id
 ORDER BY ts.title, tg.name;
