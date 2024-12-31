-- Find 3 most expensive order details
SELECT productid, unitprice * quantity AS TotalCost
FROM order_details
ORDER BY TotalCost DESC
LIMIT 3;

-- Calculate the 2 products with the least inventory in stock by total dollar amount of inventory
SELECT productname, unitprice * unitsinstock AS totalinventory
FROM products
ORDER BY totalinventory ASC
LIMIT 2;