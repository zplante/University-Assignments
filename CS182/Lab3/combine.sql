/*starts transaction*/
BEGIN TRANSACTION;


/*updates Customers with information from NewCustomers*/
UPDATE Customers
SET custName= n.custName, address=n.address, joinDate=n.joinDate
FROM  NewCustomers n
WHERE n.customerID = Customers.customerID;


/*adds new customers to Customers*/
INSERT INTO Customers (customerID, custName, address, joinDate, amountOwed, lastPaidDate, status)
SELECT /*1*/
     n.customerID, n.custName, n.address, n.joinDate, 0, NULL, 'L'
FROM 
     NewCustomers n
WHERE 
    NOT EXISTS ( SELECT c.customerID 
     						 FROM Customers c
		    				 WHERE n.customerID = c.customerID
			 				);
/*deletes all new customers once they've been added*/
/*not required but felt right*/
/*DELETE FROM NewCustomers;*/
/*ends transaction*/
COMMIT;