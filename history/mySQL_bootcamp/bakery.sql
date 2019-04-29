# Questions from https://www.interviewcake.com/article/java/sql

USE bakery;
CREATE TABLE cakes (
    cake_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    flavor VARCHAR(100) NOT NULL
);

CREATE TABLE customers (
    customer_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    street_address VARCHAR(255),
    city VARCHAR(255),
    zip_code VARCHAR(5),
    referrer_id INT,
    FOREIGN KEY (referrer_id) REFERENCES customers (customer_id)
);

CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cake_id INT NOT NULL,
    customer_id INT,
    pickup_date DATE NOT NULL,
    FOREIGN KEY (cake_id) REFERENCES cakes (cake_id),
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

/*
Qn1: How can we make this query faster?
*/
SELECT order_id FROM orders WHERE DATEDIFF(orders.pickup_date, '2017-03-01') < 0;
-- 161314 row(s) returned in 0.0078 sec / 0.267 sec

# First, we could consider adding an index on pickup_date. This'll make our inserts less efficient, but will drastically make this query faster.
ALTER TABLE orders ADD INDEX (pickup_date);
SELECT order_id FROM orders WHERE DATEDIFF(orders.pickup_date, '2017-03-01') < 0;

# We added an index but didn't get an improvement. This is because we're using the DATEDIFF function in the WHERE clause. 
# Functions evaluate for every row in a table without using the index!
SELECT order_id FROM orders WHERE orders.pickup_date < '2017-03-01';

/*
Qn2: How can we get the nth highest number of orders a single customer has?
*/

# Group by customer, and count the number of orders, then sort to get top n. But what if you wanted say the nth row onwards?
SELECT customers.customer_id, customers.first_name, COUNT(orders.order_id) as 'order_count'
FROM customers LEFT JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id ORDER BY COUNT(orders.order_id) DESC LIMIT 5
;

# Alternatively, we can create a view
CREATE VIEW customer_order_counts AS
SELECT customers.customer_id, first_name, count(orders.customer_id) AS order_count
FROM customers LEFT OUTER JOIN orders
ON (customers.customer_id = orders.customer_id)
GROUP BY customers.customer_id;

# We can then use the LIMIT command to filter for top nth
SELECT * FROM customer_order_counts 
ORDER BY order_count DESC LIMIT 1,5;

# If LIMIT has one argument, that argument is the number of rows to return starting with the first row. 
# With 2 arguments, the first argument is the row offset and the second argument is the number of rows to return. 
# So in our query with “1, 1” we're saying "starting one row down from the top, give us one row."

/*
Qn3: What ways can we use wildcard characters in LIKE clauses?
*/

# LIKE lets you use two wildcard characters, "%" and "_".
# "%" matches any amount of characters (including zero characters). So if we want all our customers whose last name starts with "A", we could query:
SELECT customer_id, first_name FROM customers
WHERE first_name LIKE 'A%';

# "_" matches exactly one character. If we want all our customers who live on the 200 block of Flatley Avenue in Dover, we could query:
SELECT customer_id, first_name, street_address FROM customers
WHERE street_address LIKE '2__ Flatley Avenue' AND city = 'Dover';

/*
Qn4: how can we make this query faster?
- https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/like-performance-tuning
*/
SELECT first_name, last_name, street_address, city, zip_code FROM customers
WHERE first_name LIKE '%sam%' AND city = 'Dover';
-- 1072 row(s) returned 0.136 sec / 0.263 sec

# Apply business context - do not return zip_code if not required, can we accept sam% then we can use index
# LIKE filters can only use the characters before the first wild card during tree traversal. 
# The remaining characters are just filter predicates that do not narrow the scanned index range. 
ALTER TABLE customers ADD INDEX (first_name);
SELECT first_name, last_name, street_address, city FROM customers
WHERE first_name LIKE 'sam%' AND city = 'Dover';
-- 1065 row(s) returned 0.0081 sec / 0.0091 sec

/*
Qn5: What are the different types of JOINS?
*/
# LEFT JOIN customers, means keep all rows from customers
# SQL does not support full outer join but you can use UNION to combine 2 OUTER queries

SELECT order_id, pickup_date, customers.customer_id, first_name
FROM orders LEFT OUTER JOIN customers
ON orders.customer_id = customers.customer_id

UNION

SELECT order_id, pickup_date, customers.customer_id, first_name
FROM orders RIGHT OUTER JOIN customers
ON orders.customer_id = customers.customer_id;

# List all customers and the names of their referrers if any
SELECT c.first_name, r.first_name
FROM customers AS c LEFT JOIN customers AS r
ON c.customer_id = r.referrer_id;

/*
Qn6: What’s an example of SQL injection and how can we prevent it?
*/

# SELECT * FROM customers WHERE phone = '1' OR 1=1 LIMIT 5;--';

# Method 1: Used stored procedures or prepared SQL statements. Do not allow dynamic SQL queries
# Using stored procedures, the database will understand the difference between the query and the data

#DROP PROCEDURE IF EXISTS spGetCustomersByCity;
DELIMITER //
CREATE PROCEDURE spGetCustomersByCity
(IN input_city VARCHAR(15))
BEGIN
	SELECT first_name, street_address, city FROM customers 
    WHERE city = input_city LIMIT 5;
END //
DELIMITER ;

CALL spGetCustomersByCity('Dover');

DELIMITER //
CREATE PROCEDURE get_customer_from_phone
(IN input_phone VARCHAR(15))
BEGIN
    SELECT * FROM customers WHERE phone = input_phone;
END //
DELIMITER ;

CALL get_customer_from_phone('1');

# Method 2: Input string validation
# Method 3: Escape special characters like quotes
# Method 4: Limit database command privileges - normal users should not be able to execute DROP tables
# Method 5: DO not display error messages




















