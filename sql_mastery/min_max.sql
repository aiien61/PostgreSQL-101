-- Find the first order date
SELECT MIN(orderdate)
FROM orders
WHERE shipcountry = 'Italy';

-- Find the last order date
SELECT MAX(orderdate)
FROM orders
WHERE shipcountry = 'Canada';

-- Find the slowest order sent to France based on order date versus ship date
SELECT MAX(shippeddate - orderdate)
FROM orders
WHERE shipcountry = 'France';