import java.util.Random;
import java.util.Scanner;

public class CrapsSim {

	public static void main(String[] args) {
		//Assignment 3
		//Zachary Plante, zplante
		//This Program runs a user inputed number of games of craps and returns the probability of winning
		
		Scanner user= new Scanner(System.in);
		System.out.println("How many games would you like to simulate?");
		
		//number of games to simulate
		int runs=user.nextInt();
		int wins=0;
		
		//loop runs the games(modified code from part 1)
		for(int i = 1;i<=runs; i++){
		
			boolean gameend;
			
			Random ran = new Random();
				int die1;
				int die2;
				int sum;
				int point;
				gameend=false;
				die1=ran.nextInt(6)+1;
				die2=ran.nextInt(6)+1;
				sum=die1+die2;
				
				if(sum==7||sum==11){
					//tracks wins
					wins++;
				
				} else if(sum==2||sum==3||sum==12){
					gameend=true;
				
				}else{
					point=sum;
					
					while(!gameend){
						die1=ran.nextInt(6)+1;
						die2=ran.nextInt(6)+1;
						sum=die1+die2;
						
						if(sum==7){
							gameend=true;
						
						}else if(sum==point){
							//tracks wins
							wins++;
							gameend=true;
						}
					}
				}
			}
		
		//calculate probability of winning
		double prob = (double)wins/(double)runs;
		//returns odds of winning
		System.out.println("Probability of winning: "+prob);
	
	
	}
		
		
	}



