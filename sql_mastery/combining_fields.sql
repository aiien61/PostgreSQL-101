-- calculation by combining fields
SELECT customerid, shippeddate - orderdate
FROM orders;

SELECT orderid, unitprice * quantity
FROM order_details;