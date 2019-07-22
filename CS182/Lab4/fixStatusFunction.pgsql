CREATE FUNCTION fixStatusFunction (lowCustomerID INTEGER) RETURNS INTEGER AS $$
	DECLARE
		theCustomer INTEGER;
		theStatus CHAR(1);
		numChanges INTEGER := 0;
		strongCustomers CURSOR FOR
		SELECT Customers.customerId, Customers.status
		FROM Customers, (SELECT customerId, SUM(amountPaid) AS totalAmount
							FROM Payments GROUP BY customerID) AS LifetimePayments
		WHERE Customers.customerId = LifetimePayments.customerId
			AND Customers.amountOwed <= LifetimePayments.totalAmount;	

	BEGIN

	OPEN strongCustomers;
	LOOP
		FETCH strongCustomers INTO theCustomer, theStatus;
		IF theCustomer IS NULL THEN EXIT; END IF;
		IF theCustomer>=lowCustomerID THEN
			IF theStatus IS NULL THEN
				UPDATE Customers SET status = 'L' WHERE customerId=theCustomer;
				numChanges := numChanges+1;

			ELSEIF theStatus = 'L' THEN
				UPDATE Customers SET status = 'M' WHERE customerId=theCustomer;
				numChanges := numChanges+1;

			ELSEIF theStatus = 'M' THEN
				UPDATE Customers SET status = 'H' WHERE customerId=theCustomer;
				numChanges := numChanges+1;
			END IF;
		END IF;
	END LOOP;
	CLOSE strongCustomers;


	RETURN numChanges;
	END;

	$$ LANGUAGE plpgsql;