    DROP SCHEMA Lab4 CASCADE;
    CREATE SCHEMA Lab4;

--Remember to execute:  ALTER ROLE your_user_id SET SEARCH_PATH TO Lab4;
--Logout and login again for this to take effect

    CREATE TABLE Products (
        productID INTEGER PRIMARY KEY,
        productName VARCHAR(40),
        manuf VARCHAR(40),
        normalPrice DECIMAL(5,2) NOT NULL,
        discount INTEGER,
        UNIQUE(productName, manuf)
    );

    CREATE TABLE Customers (
        customerID INTEGER PRIMARY KEY, 
        custName VARCHAR(40) NOT NULL, 
        address VARCHAR(40), 
        joinDate DATE, 
        amountOwed DECIMAL(6,2), 
        lastPaidDate DATE, 
        status CHAR(1),
        UNIQUE (custName, address)
    );

    CREATE TABLE Stores (
        storeID INTEGER PRIMARY KEY, 
        storeName VARCHAR(40) UNIQUE NOT NULL, 
        region CHAR(5), 
        address VARCHAR(40), 
        manager VARCHAR(40)
    );


    CREATE TABLE Days(
        dayDate DATE PRIMARY KEY, 
        category CHAR(1)
    );

    CREATE TABLE Sales(
        productID INTEGER REFERENCES Products(productID), 
        customerID INTEGER REFERENCES Customers(customerID), 
        storeID INTEGER REFERENCES Stores(storeID), 
        dayDate DATE REFERENCES Days(dayDate), 
        paidPrice DECIMAL(5,2), 
        quantity INTEGER,
        PRIMARY KEY (productID, customerID, storeID, dayDate)
    );

    CREATE TABLE Payments(
        customerID INTEGER REFERENCES Customers(customerID), 
        custName VARCHAR(40), 
        paidDate DATE, 
        amountPaid DECIMAL(6,2), 
        cleared BOOLEAN,
        PRIMARY KEY (customerID, paidDate)
    );