/*These INSERT Statments violate the foreign keys*/
INSERT INTO Sales(productID, customerID, storeID, dayDate)
VALUES(999,1001,1,DATE'2018-01-15');
INSERT INTO Sales(productID, customerID, storeID, dayDate)
VALUES(101,9999,1,DATE'2018-01-15');
INSERT INTO Sales(productID, customerID, storeID, dayDate)
VALUES(101,1001,9,DATE'2018-01-15');
INSERT INTO Sales(productID, customerID, storeID, dayDate)
VALUES(101,1001,1,DATE'2000-01-01');
INSERT INTO Payments(customerID,paidDate)
VALUES(9999,DATE'2018-01-15');



/*These UPDATE Statments meet the general constraints*/
UPDATE Customers
SET amountOwed = 0;

UPDATE Sales
SET quantity = 1, paidPrice = 10;

UPDATE Customers
SET lastPaidDate = NULL
WHERE status = 'L';

/*These UPDATE Statments do not meet the general constraints*/
UPDATE Customers
SET amountOwed = -1;

UPDATE Sales
SET quantity = 0;

UPDATE Customers
SET lastPaidDate=NULL
WHERE status != 'L';