USE databasename;

CREATE TABLE cats
	(
	name varchar(50) DEFAULT 'no name provided',
        age int NOT NULL
	);

INSERT INTO cats(name,age)
VALUES ('kitty',7),
	   ('Gucci',5);

INSERT INTO cats() value();
INSERT INTO cats(name) VALUES('gucci');
INSERT INTO cats(age) VALUES(23);

SHOW WARNINGS;
SHOW TABLES;
DROP TABLES cats;
DESC cats;
SELECT * FROM cats;

# You need primary key to prevent duplicated values
CREATE TABLE cats
	(
		cat_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		name varchar(50) DEFAULT 'no name provided',
        breed varchar(50) NOT NULL,
        age int NOT NULL
	);

INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);

# Use quotes if you want to include whitespace
SELECT cat_id AS id, name as 'cat names' FROM cats;

SET SQL_SAFE_UPDATES=0;
UPDATE cats SET breed='Tabby' WHERE name='Cindy';

###########
# Strings #
###########

# Need to use SELECT otherwise CONCAT won't know which TABLE
SELECT CONCAT('hello','world');
SELECT CONCAT(author_fname,' ',author_lname) AS 'full name' from books;
SELECT CONCAT_WS(' - ', title, author_fname, author_lname) FROM books;

# Select first 10 characters of the title
SELECT CONCAT
(
        SUBSTRING(title, 1, 10),
        '...'
    ) AS 'short title'
FROM books;

SELECT
    REPLACE(SUBSTRING(title, 1, 5), 'e', '3') AS 'weird string'
FROM books;

SELECT
    SUBSTRING(REPLACE(title, 'e', '3'), 1, 10) AS 'weird string'
FROM books;

SELECT author_lname, CHAR_LENGTH(author_lname) AS 'length' FROM books;

SELECT UPPER(title) FROM books;

SELECT SUBSTRING(title, 1, 10) AS 'short title',
CONCAT(author_lname, ' ' ,author_fname) AS 'author', 
CONCAT(stock_quantity,' in stock') AS 'quantity'
FROM books;

INSERT INTO books
    (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
           ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
           ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);

SELECT distinct author_fname, author_lname FROM books;

SELECT title, released_year, pages 
FROM books ORDER BY 2 DESC,1 ASC LIMIT 0,4;

SELECT * FROM books;
SELECT CONCAT(title, ' - ' ,released_year) AS summary FROM books ORDER BY released_year DESC LIMIT 3;
SELECT title, author_lname FROM books WHERE author_lname LIKE '% %';

# Find the year each author published their first book
# Need to first group by the author then pick the min for each author
# Find the longest page count for each author
SELECT CONCAT(author_fname,' ',author_lname) AS 'Author Name', max(pages)
FROM books
GROUP BY author_fname,author_lname;

# Find the full name of the author who wrote the longest book
SELECT CONCAT(author_fname, ' ' ,author_lname), pages
FROM books
ORDER BY pages DESC limit 1;

SELECT released_year AS 'year', COUNT(*) AS '# books', AVG(pages) 
FROM books
GROUP BY released_year;

##############
# Data types #
##############

# Float - 4 bytes (7 digits)
# Double - 8 bytes (15 digits)
# Date - only date no time
# Time - only time no date
# Datetime - YYYY-MM-DD HH:MM:SS
# CURDATE() - current date
# CURTIME() - current time
# now() - current datetime
# Useful to be used during inserts
SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
SELECT DATE_FORMAT(birthdt, '%m/%d/%Y at %h:%i') FROM people;
# DATEDIFF
# DATE_ADD
# https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html

CREATE TABLE comments2 (
    content VARCHAR(100),
    changed_at TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO comments2 (content) VALUES('dasdasdasd');
INSERT INTO comments2 (content) VALUES('lololololo');
INSERT INTO comments2 (content) VALUES('I LIKE CATS AND DOGS');
UPDATE comments2 SET content='THIS IS NOT GIBBERISH' WHERE content='dasdasdasd';
SELECT * FROM comments2;
SELECT * FROM comments2 ORDER BY changed_at;

SELECT DAYOFWEEK(CURDATE());
SELECT DAYOFWEEK(NOW());
SELECT DATE_FORMAT(NOW(), '%w') + 1;
 
SELECT DAYNAME(NOW());
SELECT DATE_FORMAT(NOW(), '%W');
 
SELECT DATE_FORMAT(CURDATE(), '%m/%d/%Y');
 
SELECT DATE_FORMAT(NOW(), '%M %D at %h:%i');
 
CREATE TABLE tweets(
    content VARCHAR(140),
    username VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);
 
INSERT INTO tweets (content, username) VALUES('this is my first tweet', 'coltscat');
SELECT * FROM tweets;
 
INSERT INTO tweets (content, username) VALUES('this is my second tweet', 'coltscat');
SELECT * FROM tweets;

# Use cast when comparing dates
SELECT CAST('2018-08-31' AS DATETIME);
SELECT name, birthdt FROM people
WHERE birthdt BETWEEN CAST('1980-01-01' AS DATETIME) AND CAST('2000-01-01' AS DATETIME);

# NOT IN
SELECT title, released_year FROM books
WHERE released_year NOT IN 
(2000,2002,2004,2006,2008,2010,2012,2014,2016);

# Modulo
SELECT title, released_year FROM books
WHERE released_year >= 2000 AND
released_year % 2 != 0;

# CASE
SELECT title, released_year,
       CASE 
         WHEN released_year >= 2000 THEN 'Modern Lit'
         ELSE '20th Century Lit'
       END AS GENRE
FROM books;

# Excerise
set session sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';

SELECT author_lname, COUNT(*) AS 'count', title
FROM books
GROUP BY author_lname;

SELECT title, author_fname, author_lname,
    CASE 
        WHEN COUNT(*) = 1 THEN '1 book'
        ELSE CONCAT(COUNT(*), ' books')
    END AS COUNT
FROM books 
GROUP BY author_lname, author_fname;

#########
# JOINS #
#########

CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100)
);
CREATE TABLE orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    amount DECIMAL(8,2),
    customer_id INT,
    FOREIGN KEY(customer_id) 
        REFERENCES customers(id)
        ON DELETE CASCADE
);

INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016/02/10', 99.99, 1),
       ('2017/11/11', 35.50, 1),
       ('2014/12/12', 800.67, 2),
       ('2015/01/03', 12.50, 2),
       ('1999/04/11', 450.25, 5);

-- IMPLICIT INNER JOIN
 SELECT * FROM customers, orders 
WHERE customers.id = orders.customer_id;
    
-- EXPLICIT INNER JOINS
SELECT first_name, last_name, order_date, amount FROM customers
JOIN orders
    ON customers.id = orders.customer_id;

-- Order does not affect results only the way it is presented
SELECT * FROM orders
JOIN customers
    ON customers.id = orders.customer_id;

-- LEFT JOIN. There could be some customers that did not order anything hence the amount is 0 
SELECT 
    first_name, 
    last_name,
    IFNULL(SUM(amount), 0) AS total_spent
FROM customers
LEFT JOIN orders
    ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY total_spent;

-- You can set dependency on foreign key so that when you delete the primary all associated foreign keys get deleted as well
-- ON DELETE CASCADE
DROP TABLE customers, orders;

# Excerise
CREATE TABLE students(
	id INT auto_increment PRIMARY KEY,
    first_name varchar(50)
);

CREATE TABLE papers(
	student_id INT,
    title varchar(50),
    grade int,
    FOREIGN KEY(student_id)
		REFERENCES students(id)
        ON DELETE CASCADE
);

INSERT INTO students (first_name) VALUES 
('Caleb'), ('Samantha'), ('Raj'), ('Carlos'), ('Lisa');

INSERT INTO papers (student_id, title, grade ) VALUES
(1, 'My First Book Report', 60),
(1, 'My Second Book Report', 75),
(2, 'Russian Lit Through The Ages', 94),
(2, 'De Montaigne and The Art of The Essay', 98),
(4, 'Borges and Magical Realism', 89);

SELECT first_name,
IFNULL(title, 'MISSING') AS 'title',
IFNULL(grade, 0) AS 'grade'
FROM students
LEFT JOIN papers
	ON students.id = papers.student_id;

###################
# Special queries #
###################

# names of movies where one or more actors acted in two or more movies.
SELECT movie_title FROM movies LEFT JOIN movies_cast 
    ON movies.movie_id = movies_cast.movie_id
WHERE movies_cast.actor_id IN 
    (SELECT actor_id FROM movies_cast GROUP BY actor_id HAVING COUNT(actor_id) > 1);

# movie_title and name of director who directed a movie that casted a role as ‘SeanMaguire’

SELECT CONCAT(d.director_first_name, d.director_last_name) as 'director_name', m.movie_title
FROM movies m 
LEFT JOIN movies_directors md
    ON m.movie_id = md.movie_id
LEFT JOIN directors d
    ON d.director_id = md.director_id
WHERE m.movie_id IN
(SELECT movies.movie_id FROM movies LEFT JOIN movies_cast
ON movies_cast.movie_id = movies.movie_id WHERE movies_cast.role = 'SeanMaguire')
;








