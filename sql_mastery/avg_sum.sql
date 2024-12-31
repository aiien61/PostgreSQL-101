-- The average freight of orders shipped to Brazil
SELECT AVG(freight)
FROM orders
WHERE shipcountry = 'Brazil';

-- How many individual items of tofu (product id = 14) were ordered
SELECT SUM(quantity)
FROM order_details
WHERE productid = 14;

-- What was the average number of Steeleye Stout (product id = 35) per order
SELECT AVG(quantity)
FROM order_details
WHERE productid=35;