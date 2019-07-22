/*creates 4 foreing keys for Sales (productID, customerID,storeID,dayDate)
and one for Payments (customerID)*/
ALTER TABLE Sales
ADD FOREIGN KEY (productID) REFERENCES Products(productID);

ALTER TABLE Sales
ADD FOREIGN KEY (customerID) REFERENCES Customers(customerID);

ALTER TABLE Sales
ADD FOREIGN KEY (storeID) REFERENCES Stores(storeID);

ALTER TABLE Sales
ADD FOREIGN KEY (dayDate) REFERENCES Days(dayDate);

ALTER TABLE Payments
ADD FOREIGN KEY (customerID) REFERENCES Customers(customerID);