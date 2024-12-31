-- Find the total spent for each order detail and name the field TotalSpent
SELECT unitprice * quantity AS TotalSpent
FROM order_details;

-- Use the alias in order by
SELECT unitprice * quantity AS TotalSpent
FROM order_details
ORDER BY TotalSpent DESC;

-- Calculate our inventory value of products and return as TotalInventory and order by column desc
SELECT unitprice * unitsinstock AS TotalInventory
FROM products
ORDER BY TotalInventory DESC;