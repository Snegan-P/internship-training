
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO users (name, email)
VALUES ('Snegan', 'sneganp26@gmail.com');

INSERT INTO users (name,email)
VALUES ('SNT','snegan4446@gmail.com');

INSERT INTO users(name,email) 
VALUES ('SST','siva@gmail.com');

INSERT INTO users(name,email)
VALUES('SSS','sss@gmail.com');

INSERT INTO users(name,email)
VALUES ('SANJAY','sanjay@gmail.com');

INSERT INTO users(name,email)
VALUES ('shibi','shibi@gmail.com');


SELECT * FROM users;

SELECT* FROM users WHERE ID =3;

SELECT * FROM users
ORDER BY id DESC;

UPDATE users
SET name = 'SNEGAN'
WHERE email = 'sne@gmail.com';


SELECT MAX(id) FROM users;