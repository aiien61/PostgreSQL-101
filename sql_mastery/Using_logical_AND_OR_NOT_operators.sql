-- How many orders shipped to Germany and the freight cost more than $100
SELECT COUNT(*)
FROM orders
WHERE shipcountry = 'Germany' AND freight > 100;

-- We want the distinct customers where orders were shipped via United Package (id=2) and the ship country is Brazil
SELECT DISTINCT(customerid)
FROM orders
WHERE shipvia = 2 AND shipcountry = 'Brazil';

-- How many customers do we have in USE and Canada
SELECT COUNT(*)
FROM customers
WHERE country = 'USA' OR country = 'Canada';

-- How many suppliers do we have in Germany and Spain
SELECT COUNT(*)
FROM suppliers
WHERE country = 'Germany' OR country = 'Spain';

-- How many orders shipped to USA, Brazil and Argentina
SELECT COUNT(*)
FROM orders
WHERE shipcountry = 'USA' OR shipcountry = 'Brazil' OR shipcountry = 'Argentina';

-- How many customers are not in France
SELECT COUNT(*)
FROM customers
WHERE NOT country = 'France';

-- How many customers are not in USA
SELECT COUNT(*)
FROM customers
WHERE NOT country = 'USA';

-- How many orders are shipped to Germany and freight charges < 50 or > 175
SELECT COUNT(*)
FROM orders
WHERE shipcountry = 'Germany' AND (freight < 50 OR freight > 175);

-- How many orders shipped to Canada or Spain and shippeddate after May 1, 1997
SELECT COUNT(*)
FROM orders
WHERE (shipcountry = 'Canada' OR shipcountry = 'Spain') 
AND shippeddate > '1997-05-01';
