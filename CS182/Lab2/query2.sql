SELECT productID AS theProduct, customerID AS theCustomer, storeID AS theStore
FROM Sales
WHERE 	dayDate = DATE '2018-01-16'
	AND	paidPrice > 20.00
	AND	quantity > 5;