import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;

public class AnagramPuzzleGenerator {

	public static void main(String[] args) throws FileNotFoundException {
		String word = new String();
		String puzzle = new String();
		Random r = new Random();
		
		Scanner in = new Scanner(new FileInputStream(args[0]));

		int size = in.nextInt();
		int getword = r.nextInt(size);
		int i = 0;
		while ( i <= getword ) {
		   word = in.next();
		    i++;
		}
		
		//word = "ZACHARY";
		
		
		
		int length = word.length();
		
		while (length>0){
			int place = r.nextInt(length);
			puzzle = puzzle + word.substring(place, place+1);
			word = word.substring(0, place) + word.substring(place+1);
			length = word.length();
		}
		
		System.out.println(puzzle);

	}

}

