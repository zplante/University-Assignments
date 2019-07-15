import java.util.Random;
import java.util.Scanner;

public class Craps {

	public static void main(String[] args) {
		//Assignment 3
		//Zachary Plante, zplante
		//This program simulates a game of craps for the user, allowing them to set their own seed and bets
		int pool;
		int seed;
		boolean gameend;
		
		Scanner user = new Scanner(System.in);
		
		//lets user set betting pool and seed
		System.out.println("Welcom to craps! How many chips would you like?");
		pool = user.nextInt();
		System.out.println("You are playing with "+pool+" chip(s). Set the seed");
		seed = user.nextInt();
		Random ran = new Random(seed);
		//loop runs games until the user is out of money
		while(pool>0){
			int bet;
			int die1;
			int die2;
			int sum;
			int point;
			gameend=false;
			
			//takes bet
			System.out.println("How much would you like to bet?");
			bet=user.nextInt();
			while(bet>pool){
				System.out.println("Invalid bet, you only have "+pool+" chips");
				bet=user.nextInt();
			}
			
			System.out.println("Press enter to roll");
			//simulates roll of dice and returns dice to the user
			user.nextLine();
			die1=ran.nextInt(6)+1;
			die2=ran.nextInt(6)+1;
			sum=die1+die2;
			System.out.println("You rolled "+die1+", "+die2);
			
			//checks win/loose conditions
			if(sum==7||sum==11){
				//adds bet to pool and returns new pool
				pool+=bet;
				System.out.println("You won! You now have "+pool+" chips!");
			
			} else if(sum==2||sum==3||sum==12){
				//removes bet from pool and returns new pool
				pool-=bet;
				System.out.println("You lost. You now have "+pool+" chips");
			
			}else{
				point=sum;
				//while loop continues until win/loose condition is met
				
				while(!gameend){
					System.out.println("The point is "+point+". Roll again");
					user.nextLine();
					die1=ran.nextInt(6)+1;
					die2=ran.nextInt(6)+1;
					sum=die1+die2;
					System.out.println("You rolled "+die1+", "+die2);
					
					if(sum==7){
						//loose condition
						pool-=bet;
						gameend=true;
						System.out.println("You lost. You now have "+pool+" chips");
					
					}else if(sum==point){
						//win condition
						pool+=bet;
						gameend=true;
						System.out.println("You won! You now have "+pool+" chips!");
					}
				}
			}
		}
	}

}

