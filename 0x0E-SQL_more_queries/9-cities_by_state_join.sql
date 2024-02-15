-- List all cities contained in the database

SELECT c.id, c.name, s.name
FROM states AS s
       INNER JOIN cities AS c
       ON c.state_id = s.id
 ORDER BY c.id
