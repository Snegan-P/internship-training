CREATE TABLE st(
  id SERIAL PRIMARY KEY ,
  name VARCHAR(30),
  department VARCHAR(20),
  mark INT);
  
  
INSERT INTO st
VALUES(10,'SNT',80);

INSERT INTO st
VALUES(20,'SST',90);
  
CREATE TABLE employe(
id SERIAL PRIMARY KEY,
name VARCHAR(20),
mark INT);
    
INSERT INTO employe 
VALUES(20,'SST',30);
INSERT INTO employe 
VALUES(25,'SNT',40);

SELECT
    department,
    AVG(mark) AS average_mark
FROM st
GROUP BY department;


UPDATE st
SET id = 30
WHERE id = 10;

DELETE  FROM st WHERE id=10;

SELECT COUNT(*) FROM st;


SELECT AVG(mark)FROM st;



# INNER JOINS

SELECT s.id,
s.name AS st_name,
e.name AS employe_name
FROM st s INNER JOIN employe e ON s.id=e.id;


    
    
    
    
    
    








    













