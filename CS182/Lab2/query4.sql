SELECT DISTINCT c.customerID, c.custName
FROM Customers AS c, Sales AS sa1, Sales AS sa2, Stores AS st
WHERE 	sa1.customerID = sa2.customerID
	AND c.customerID = sa1.customerID
	AND	sa1.storeID = sa2.storeID
	AND	sa1.productID <> sa2.productID
	AND st.storeID = sa1.storeID
	AND st.region = 'North';