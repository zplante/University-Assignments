import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class AnagramFinder {

	public static void main(String[] args) throws FileNotFoundException {
		//Assignment 2
		//Zachary Plante, zplante@ucsc.edu
		//This Program takes a user imported string and finds anagrams of it from a .txt file
		
		String keepplaying = "y";
		
		
		System.out.println("Welcome to Anagram Finder! Type a string to find its anagrams (lower case only).");
		
		//while loop allows for repeated inputs
		while(keepplaying.equalsIgnoreCase("y")){
			
			Scanner user = new Scanner(System.in);
			Scanner in = new Scanner(new FileInputStream(args[0]));
			int size = in.nextInt();
			
			String input = new String();
			input = user.next();//user inputed string
			ArrayList<String> list = new ArrayList<String>();
			int[] primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101};
			int inputnum=1;
			int length = input.length();
			
			for(int count = 0;count<length;count++){
				inputnum=inputnum*primes[((int)input.charAt(count)-97)];
				//translates each letter in the input into a diff prime
				//then multiplies those primes to create a unique value for that string
			}
			
			
			int i = 0;
			 //searches through .txt file
			while ( i < size) {
				int wordnum = 1;
			   String word = in.next();
			   int templ = word.length();
			   
			 //multiplies primes to create a unique value for each word
			   for(int temp = 0; temp<templ;temp++){
				   wordnum=wordnum*primes[((int)word.charAt(temp)-97)];
			   }
			   
			   if(inputnum==wordnum){
				   list.add(word);
				   //only true if the two strings are anagrams, due to the nature of prime numbers
			   }
		
			 
			    i++;
			}
			
			int listlength = list.size();
			int t=0;
			
			while(t<listlength){
				System.out.println(list.get(t));
				t++;
			} //prints out the anagrams that have been placed in the ArrayList
			
			System.out.println("Would you like to go again? y/n");
			keepplaying=user.next();
			//asks the user if they would like to run another string
		}
		System.out.println("GoodBye");

			
				
				


	}

}
