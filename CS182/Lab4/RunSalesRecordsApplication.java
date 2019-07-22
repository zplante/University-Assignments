import java.sql.*;
import java.io.*;
import java.util.*;

/**
 * A class that connects to PostgreSQL and disconnects.
 * You will need to change your credentials below, to match the usename and password of your account
 * in the PostgreSQL server.
 * The name of your database in the server is the same as your username.
 * You are asked to include code that tests the methods of the SalesRecordsApplication class
 * in a similar manner to the sample RunFilmsApplication.java program.
*/


public class RunSalesRecordsApplication
{
    public static void main(String[] args) {
    	
    	Connection connection = null;
    	try {
            String username = ""; //put username here
            String password = ""; //put password here
    	    //Register the driver
    		Class.forName("org.postgresql.Driver"); 
    	    // Make the connection.
            // You will need to fill in your real username abd password for your
            // Postgres account in the arguments of the getConnection method below.
            connection = DriverManager.getConnection(
                                                     "jdbc:postgresql://cmps182-db.lt.ucsc.edu/"+username,
                                                     username,
                                                     password);
            
            if (connection != null)
                System.out.println("Connected to the database!");

            /* Include your code below to test the methods of the SalesRecordsApplication class
             * The sample code in RunFilmsApplication.java should be useful.
             * That code tests other methods for a different database schema.
             * Your code below: */
            //creates app instance
            SalesRecordsApplication app = new SalesRecordsApplication(connection);

            //variables for testing, feel free to change
            int numProducts = 3;//for getStores that SoldFewProducts
            String oldName = "Google";//for updateManufacturer
            String newName = "Alphabet";//for updateManufacturer
            int firstID = 1001;//for fixCustomerStatus
            int secondID = 1004;//for fixCustomerStatus


            //runs functions and gets result values
            List<Integer> result1 = app.getStoresThatSoldFewProducts(numProducts);
            int result2 = app.updateManufacturer(oldName,newName);
            int result3 = app.fixCustomerStatus(firstID);
            int result4 = app.fixCustomerStatus(secondID);



            //finally prints out the reuslts of the test to the user
            System.out.println("Testing getStoresThatSoldFewProducts with input of "+numProducts);
            System.out.println("Results: "+result1);
            System.out.println("Testing updateManufacturer with input "+oldName+" and "+newName);
            System.out.println("Number of rows changed: "+result2);
            System.out.println("Testing fixCustomerStatus with input "+firstID);
            System.out.println("Number of rows changed: "+result3);
            System.out.println("Testing fixCustomerStatus with input "+secondID);
            System.out.println("Number of rows changed: "+result4);
            System.out.println("Closing Connection");

            
            /*******************
            * Your code ends here */
            connection.close();
    	}
    	catch (SQLException | ClassNotFoundException e) {
    		System.out.println("Error while connecting to database: " + e);
    		e.printStackTrace();
    	}
    	finally {
    		if (connection != null) {
    			// Closing Connection
    			try {
					connection.close();
				} catch (SQLException e) {
					System.out.println("Failed to close connection: " + e);
					e.printStackTrace();
				}
    		}
    	}
    }
}
