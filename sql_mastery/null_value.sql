-- How many customers don't have a region value
SELECT COUNT(*)
FROM customers
WHERE region IS NULL;

-- How many suppliers have a region value
SELECT COUNT(*)
FROM suppliers
WHERE region IS NOT NULL;

-- How many orders did not have a ship region
SELECT COUNT(*)
FROM orders
WHERE shipregion IS NULL;