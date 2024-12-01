-- total records in products table
SELECT COUNT(*)
FROM products;

-- total records in orders table
SELECT COUNT(*)
FROM orders;

-- find how many distinct city from suppliers table
SELECT COUNT(DISTINCT(city))
FROM suppliers;

-- find how many distinct products have been ordered 
SELECT COUNT(DISTINCT(productid))
FROM order_details;