/*creates a view of every customer with atleast one cleared 
payment and records how many cleared payments they have*/
CREATE VIEW ClearedPayments
AS SELECT customerID, SUM(amountPaid) AS totalClearedPayments
FROM Payments
WHERE cleared = true
GROUP BY customerID;
