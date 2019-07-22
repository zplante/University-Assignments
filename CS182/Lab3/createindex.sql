/*Creates an index for Sales over customerID and dayDate*/
CREATE INDEX LookUpSales
ON Sales (customerID,dayDate);