-- BETWEEN is the shortcut for greater than and lower than

-- WHERE frieght BETWEEN 50 AND 100
-- is same as 
-- WHERE freight >= 50 AND freight <= 100


-- How many orders details have a unit between $10 and $20
SELECT COUNT(*)
FROM order_details
WHERE unitprice BETWEEN 10 AND 20;

-- How many order shipped between June 1, 1996 and September 30, 1996
SELECT COUNT(*)
FROM orders
WHERE shippeddate BETWEEN '1996-06-01' AND '1996-09-30';


-- WHERE id IN (2, 3, 22, 33, 88)
-- is same as
-- WHERE id=2 OR id=3 OR id=22 OR id=33 OR id=88

-- How many suppliers are located in Germany, France, Spain, or Italy
SELECT COUNT(*)
FROM suppliers
WHERE country IN ('Germany', 'Spain', 'France', 'Italy');

-- How many products do we have in categoryid 1, 4, 6, or 7
SELECT COUNT(*)
FROM products
WHERE categoryid IN (1, 4, 6, 7);
