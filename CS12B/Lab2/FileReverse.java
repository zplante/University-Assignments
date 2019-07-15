import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class FileReverse {

	public static void main(String[] args) throws IOException {
		

		      int lineNumber = 0;

		      // check number of command line arguments is at least 2
		      if(args.length < 2){
		         System.out.println("Usage: FileCopy <input file> <output file>");
		         System.exit(1);
		      }

		      // open files
		      Scanner in = new Scanner(new File(args[0]));
		      PrintWriter out = new PrintWriter(new FileWriter(args[1]));

		      // read lines from in, extract and print tokens from each line
		      while( in.hasNextLine() ){
		         lineNumber++;

		         // trim leading and trailing spaces, then add one trailing space so 
		         // split works on blank lines
		         String line = in.nextLine().trim() + " "; 

		         // split line around white space 
		         String[] token = line.split("\\s+");  

		         // print out tokens       
		         int n = token.length;
		         for(int i=0; i<n; i++){
		            out.println(stringReverse(token[i]));
		         }
		      }

		      // close files
		      in.close();
		      out.close();
		      
		      
		      
		   }
		
	public static String stringReverse(String s){
		int l = s.length();
		String ret = "";
		for(int i=l-1;i>=0;i--){
			ret += s.charAt(i);
		}
		return ret;
	}

	}



