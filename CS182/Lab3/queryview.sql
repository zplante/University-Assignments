/*querys view to find "Great Customers"*/
SELECT cp.customerID, cp.totalClearedPayments, COUNT(DISTINCT s.productID) AS numDiffProducts
FROM ClearedPayments AS cp, Sales AS s, Customers AS c
WHERE cp.totalClearedPayments > c.amountOwed
	AND c.customerID = cp.customerID
	AND s.customerID = cp.customerID
GROUP BY cp.customerID, cp.totalClearedPayments
HAVING COUNT(DISTINCT s.productID)>=3;
/* results */
/*
 customerid | totalclearedpayments | numdiffproducts 
------------+----------------------+-----------------
       1001 |               269.11 |               5
       1002 |               364.56 |               5
       1004 |               494.40 |               3
       1005 |               249.99 |               3
*/
/* deletes*/
DELETE FROM Payments WHERE (customerID=1002 AND paidDate=DATE'2018-02-19')OR(customerID=1004 AND paidDate=DATE'2018-02-04');
/*runs the query again*/

SELECT cp.customerID, cp.totalClearedPayments, COUNT(DISTINCT s.productID) AS numDiffProducts
FROM ClearedPayments AS cp, Sales AS s, Customers AS c
WHERE cp.totalClearedPayments > c.amountOwed
	AND c.customerID = cp.customerID
	AND s.customerID = cp.customerID
GROUP BY cp.customerID, cp.totalClearedPayments
HAVING COUNT(DISTINCT s.productID)>=3;

/*results*/
/*
 customerid | totalclearedpayments | numdiffproducts 
------------+----------------------+-----------------
       1001 |               269.11 |               5
       1002 |               352.24 |               5
       1005 |               249.99 |               3
*/
