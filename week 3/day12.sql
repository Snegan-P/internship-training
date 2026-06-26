CREATE TABLE st(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    mark INT
);

INSERT INTO st
VALUES(10,'SNT',80);

INSERT INTO st
VALUES(20,'SST',90);

CREATE TABLE employe(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    mark INT
);

INSERT INTO employe
VALUES(20,'SST',30);

INSERT INTO employe
VALUES(25,'SNT',40);

-- UPDATE

UPDATE st
SET name = 'SNEGAN'
WHERE id = 10;

-- DELETE

DELETE FROM st
WHERE id = 20;

-- COUNT

SELECT COUNT(*) AS total_students
FROM st;

-- AVG

SELECT AVG(mark) AS average_mark
FROM st;

-- sum 
SELECT SUM(mark) AS total_age
FROM st;

-- INNER JOIN

SELECT
    s.id,
    s.name AS st_name,
    e.name AS employe_name
FROM st s
INNER JOIN employe e
ON s.id = e.id;
  
-- GROUP BY

SELECT
    name,
    COUNT(*) AS total_count
FROM st
GROUP BY name;

-- Left joins 

SELECT
    s.id,
    s.name AS st_name,
    e.name AS employe_name
FROM st s
LEFT JOIN employe e
ON s.id = e.id;