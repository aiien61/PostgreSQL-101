-- Find number of orders that were ordered on or after January 01, 1998
SELECT COUNT(*)
FROM orders
WHERE orderdate >= '1998-01-01';

-- How many orders shipped before July 5, 1997
SELECT COUNT(*)
FROM orders
WHERE shippeddate < '1997-07-05';