SELECT c.customerID, c.address, sa.paidPrice * sa.quantity AS theRevenue, sa.dayDate
FROM Customers AS c, Sales AS sa
WHERE 	c.status = 'H'
	AND	c.address IS NOT NULL
	AND sa.paidPrice * sa.quantity >=200
	AND c.customerID = sa.customerID