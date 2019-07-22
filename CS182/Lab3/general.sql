/*customers cannot owe negative money*/
ALTER TABLE Customers ADD CONSTRAINT owed_is_not_negative
CHECK ( amountOwed >= 0.00);

/*Sales must have a revenue of 10 dollars or more*/
ALTER TABLE Sales ADD
CHECK (paidPrice * quantity >=10.00);

/*If lastpaid Date is NULL status is 'L'*/
ALTER TABLE Customers ADD
CHECK (lastPaidDate IS NOT NULL OR (lastPaidDate IS NULL AND status ='L'));
