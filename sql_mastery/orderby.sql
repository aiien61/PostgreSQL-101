-- Select columns and order them by sepecific columns in ascending order
SELECT DISTINCT country
FROM suppliers
ORDER BY country ASC;

-- Select columns and order them by sepecific columns in descending order
SELECT DISTINCT country
FROM suppliers
ORDER BY country DESC;

-- Select columns and order them by some columns in ascending order and other columns in descending order
SELECT DISTINCT country, city
FROM suppliers
ORDER BY country ASC, city DESC;

SELECT DISTINCT country, city
FROM suppliers
ORDER BY country DESC, city ASC;

-- Get a list of product names and unit prices order by price highest to lowest and product name a to z (if they have same price)
SELECT productname, unitprice
FROM products
ORDER BY unitprice DESC, productname ASC;