import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class TTT3D {

	public static void main(String[] args) {
		Scanner user = new Scanner(System.in);
		int board[][][]=new int [4][4][4];
	

//Assignment 4
//		//Zachary Plante, zplante@ucsc.edu
//				//This Program sets up a game of tic-tac-toe and allows a player to play against a computer							
		//Sets up board for play
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				for(int k=0;k<4;k++){
					board[i][j][k]=0;
				}
			}
		}
		
		
		//A 3 Dimensional Array of all possible lines
		int[][][] lines = {
				{{0,0,0},{0,0,1},{0,0,2},{0,0,3}},  //lev 0; row 0   rows in each lev
				{{0,1,0},{0,1,1},{0,1,2},{0,1,3}},  //       row 1     
				{{0,2,0},{0,2,1},{0,2,2},{0,2,3}},  //       row 2     
				{{0,3,0},{0,3,1},{0,3,2},{0,3,3}},  //       row 3     
				{{1,0,0},{1,0,1},{1,0,2},{1,0,3}},  //lev 1; row 0     
				{{1,1,0},{1,1,1},{1,1,2},{1,1,3}},  //       row 1     
				{{1,2,0},{1,2,1},{1,2,2},{1,2,3}},  //       row 2     
				{{1,3,0},{1,3,1},{1,3,2},{1,3,3}},  //       row 3     
				{{2,0,0},{2,0,1},{2,0,2},{2,0,3}},  //lev 2; row 0     
				{{2,1,0},{2,1,1},{2,1,2},{2,1,3}},  //       row 1     
				{{2,2,0},{2,2,1},{2,2,2},{2,2,3}},  //       row 2       
				{{2,3,0},{2,3,1},{2,3,2},{2,3,3}},  //       row 3     
				{{3,0,0},{3,0,1},{3,0,2},{3,0,3}},  //lev 3; row 0     
				{{3,1,0},{3,1,1},{3,1,2},{3,1,3}},  //       row 1 
				{{3,2,0},{3,2,1},{3,2,2},{3,2,3}},  //       row 2       
				{{3,3,0},{3,3,1},{3,3,2},{3,3,3}},  //       row 3           
				{{0,0,0},{0,1,0},{0,2,0},{0,3,0}},  //lev 0; col 0   cols in each lev
				{{0,0,1},{0,1,1},{0,2,1},{0,3,1}},  //       col 1    
				{{0,0,2},{0,1,2},{0,2,2},{0,3,2}},  //       col 2    
				{{0,0,3},{0,1,3},{0,2,3},{0,3,3}},  //       col 3    
				{{1,0,0},{1,1,0},{1,2,0},{1,3,0}},  //lev 1; col 0     
				{{1,0,1},{1,1,1},{1,2,1},{1,3,1}},  //       col 1    
				{{1,0,2},{1,1,2},{1,2,2},{1,3,2}},  //       col 2    
				{{1,0,3},{1,1,3},{1,2,3},{1,3,3}},  //       col 3    
				{{2,0,0},{2,1,0},{2,2,0},{2,3,0}},  //lev 2; col 0     
				{{2,0,1},{2,1,1},{2,2,1},{2,3,1}},  //       col 1    
				{{2,0,2},{2,1,2},{2,2,2},{2,3,2}},  //       col 2    
				{{2,0,3},{2,1,3},{2,2,3},{2,3,3}},  //       col 3    
				{{3,0,0},{3,1,0},{3,2,0},{3,3,0}},  //lev 3; col 0     
				{{3,0,1},{3,1,1},{3,2,1},{3,3,1}},  //       col 1
				{{3,0,2},{3,1,2},{3,2,2},{3,3,2}},  //       col 2
				{{3,0,3},{3,1,3},{3,2,3},{3,3,3}},  //       col 3
			    {{0,0,0},{1,0,0},{2,0,0},{3,0,0}},  //cols in vert plane in front
			    {{0,0,1},{1,0,1},{2,0,1},{3,0,1}},
			    {{0,0,2},{1,0,2},{2,0,2},{3,0,2}},
			    {{0,0,3},{1,0,3},{2,0,3},{3,0,3}},
			    {{0,1,0},{1,1,0},{2,1,0},{3,1,0}},  //cols in vert plane one back
			    {{0,1,1},{1,1,1},{2,1,1},{3,1,1}},
			    {{0,1,2},{1,1,2},{2,1,2},{3,1,2}},
			    {{0,1,3},{1,1,3},{2,1,3},{3,1,3}},
			    {{0,2,0},{1,2,0},{2,2,0},{3,2,0}},  //cols in vert plane two back
			    {{0,2,1},{1,2,1},{2,2,1},{3,2,1}},
			    {{0,2,2},{1,2,2},{2,2,2},{3,2,2}},
			    {{0,2,3},{1,2,3},{2,2,3},{3,2,3}},
			    {{0,3,0},{1,3,0},{2,3,0},{3,3,0}},  //cols in vert plane in rear
			    {{0,3,1},{1,3,1},{2,3,1},{3,3,1}},
			    {{0,3,2},{1,3,2},{2,3,2},{3,3,2}},
			    {{0,3,3},{1,3,3},{2,3,3},{3,3,3}},
			    {{0,0,0},{0,1,1},{0,2,2},{0,3,3}},  //diags in lev 0
				{{0,3,0},{0,2,1},{0,1,2},{0,0,3}},
			    {{1,0,0},{1,1,1},{1,2,2},{1,3,3}},  //diags in lev 1
			    {{1,3,0},{1,2,1},{1,1,2},{1,0,3}},
			    {{2,0,0},{2,1,1},{2,2,2},{2,3,3}},  //diags in lev 2
			    {{2,3,0},{2,2,1},{2,1,2},{2,0,3}},
			    {{3,0,0},{3,1,1},{3,2,2},{3,3,3}},  //diags in lev 3
			    {{3,3,0},{3,2,1},{3,1,2},{3,0,3}},
			    {{0,0,0},{1,0,1},{2,0,2},{3,0,3}},  //diags in vert plane in front
			    {{3,0,0},{2,0,1},{1,0,2},{0,0,3}},
			    {{0,1,0},{1,1,1},{2,1,2},{3,1,3}},  //diags in vert plane one back
			    {{3,1,0},{2,1,1},{1,1,2},{0,1,3}},
			    {{0,2,0},{1,2,1},{2,2,2},{3,2,3}},  //diags in vert plane two back
			    {{3,2,0},{2,2,1},{1,2,2},{0,2,3}},
			    {{0,3,0},{1,3,1},{2,3,2},{3,3,3}},  //diags in vert plane in rear
			    {{3,3,0},{2,3,1},{1,3,2},{0,3,3}},
			    {{0,0,0},{1,1,0},{2,2,0},{3,3,0}},  //diags left slice      
			    {{3,0,0},{2,1,0},{1,2,0},{0,3,0}},        
			    {{0,0,1},{1,1,1},{2,2,1},{3,3,1}},  //diags slice one to right
			    {{3,0,1},{2,1,1},{1,2,1},{0,3,1}},        
			    {{0,0,2},{1,1,2},{2,2,2},{3,3,2}},  //diags slice two to right      
			    {{3,0,2},{2,1,2},{1,2,2},{0,3,2}},        
			    {{0,0,3},{1,1,3},{2,2,3},{3,3,3}},  //diags right slice      
			    {{3,0,3},{2,1,3},{1,2,3},{0,3,3}},        
			    {{0,0,0},{1,1,1},{2,2,2},{3,3,3}},  //cube vertex diags
			    {{3,0,0},{2,1,1},{1,2,2},{0,3,3}},
			    {{0,3,0},{1,2,1},{2,1,2},{3,0,3}},
			    {{3,3,0},{2,2,1},{1,1,2},{0,0,3}}        
			    };

		
		boolean gameover=false;
		int move;
		
		//loop runs as game is played
		while (!gameover&&!draw(board,lines)){
			printBoard(board);
			System.out.println("Type your move as a 3 digit number(lrc)");
			move=user.nextInt();
			int a = move/100;
			int b = (move-(a*100))/10;
			int c = move%10;
			board[a][b][c] = 5;
			gameover=checkWin(board,lines);
			if(!gameover&&!draw(board,lines)){
			int comp = compMove(board,lines);
			int x = comp/100;
			int y = (comp-(x*100))/10;
			int z = comp%10;
			board[x][y][z] = 1;
			gameover=checkWin(board,lines);
			}
		}
		
		//print results based on end game conditions
		if(compWin(board,lines)){
			System.out.println("I win, better luck next time");
		}else if(draw(board,lines)){
			System.out.println("Looks like its a draw, good game");
		}else{
			System.out.println("You win this one! Excellent game");
		}
		
	}
	
	//method prints the current board for player to view
	public static boolean printBoard(int[][][] temp){
		int change=3;
		for(int i=3;i>=0;i--){
			for(int j=3;j>=0;j--){
				if(change!=i){
					System.out.println("");
				}
				for(int s=0;s<=j;s++){
					System.out.print(" ");
				}
				System.out.print(i+""+j+" ");
				for(int k=0;k<4;k++){
					//prints visual representation for player based on value in board
					if(temp[i][j][k]==5){
						System.out.print("X");
					}else if(temp[i][j][k]==1){
						System.out.print("O");
					}else{
						System.out.print("_");
					}
				}
			System.out.println("");
			change=i;
			}
		}
		System.out.println("    0123");
		return true;
	}
	
	
	//method runs through possible strategies and outputs a move for the computer
	public static int compMove(int[][][] b,int [][][] l){
		
		Random r=new Random();
		ArrayList<Integer> sum2 = new ArrayList<Integer>();
		ArrayList<Integer> sum10 = new ArrayList<Integer>();
		ArrayList<Integer> live = new ArrayList<Integer>();
		int move=0;
		
		for(int i=0;i<76;i++){
			int sum=0;
			for(int j=0;j<4;j++){
				//outputs a sum for the line
				sum+= b[l[i][j][0]][l[i][j][1]][l[i][j][2]];			
			}
			//stores lines in an array for future strategies
			if(sum==2){
				sum2.add(i);
			}else if(sum==10){
				sum10.add(i);
			} if(sum<5||sum%5==0){
				live.add(i);
			} if(sum==3){
				//plays winning move if one is available
					for(int c=0;c<4;c++){
						if(b[l[i][c][0]][l[i][c][1]][l[i][c][2]]==0);
						move=l[i][c][0]*100+l[i][c][1]*10+l[i][c][2];
					
				}
			}
		}
		
		//blocks a player about to win
		if(move==0){
		for(int i=0;i<76;i++){
			int sum=0;
			for(int j=0;j<4;j++){
				sum+= b[l[i][j][0]][l[i][j][1]][l[i][j][2]];			
			}
			if(sum==15){
					for(int c=0;c<4;c++){
						if(b[l[i][c][0]][l[i][c][1]][l[i][c][2]]==0){
						move=l[i][c][0]*100+l[i][c][1]*10+l[i][c][2];
					}
				}	
				}
			}
		}
		
		//creates a fork if one is available 
		//by checking if any sum 2 lines have cells in common
		if(move==0){
		for(int i=0;i<sum2.size()-1;i++){
			for(int j=i+1;j<sum2.size();j++){
				for(int k=0;k<3;k++){
					for(int m=k+1;m<4;m++){
						int tot1=(l[sum2.get(i)][k][0]*100)+(l[sum2.get(i)][k][1]*10)+(l[sum2.get(i)][k][2]);
						int tot2=(l[sum2.get(j)][m][0]*100)+(l[sum2.get(j)][m][1]*10)+(l[sum2.get(j)][m][2]);
						if(tot1==tot2&&b[l[sum2.get(i)][k][0]][l[sum2.get(i)][k][1]][l[sum2.get(i)][k][2]]==0){
							move=tot1;
						}
					}
				}
				
			}
		}
	}
		
		//blocks a player about to make a fork 
		//by checking is any sum10 lines have a cell in common
		if(move==0){
			for(int i=0;i<sum10.size()-1;i++){
				for(int j=i+1;j<sum10.size();j++){
					for(int k=0;k<3;k++){
						for(int m=k+1;m<4;m++){
							int tot1=(l[sum10.get(i)][k][0]*100)+(l[sum10.get(i)][k][1]*10)+(l[sum10.get(i)][k][2]);
							int tot2=(l[sum10.get(j)][m][0]*100)+(l[sum10.get(j)][m][1]*10)+(l[sum10.get(j)][m][2]);
							if(tot1==tot2&&b[l[sum10.get(i)][k][0]][l[sum10.get(i)][k][1]][l[sum10.get(i)][k][2]]==0){
								move=tot1;
							}
						}
					}
					
				}
			}
		}
		
		//plays a random live line if no move has been made yet
		if(move==0){
			int ln = r.nextInt(live.size());
			for(int n=0; n<4;n++){
			if(b[l[ln][n][0]][l[ln][n][1]][l[ln][n][2]]==0){	
			move=(l[ln][n][0]*100)+(l[ln][n][1]*10)+l[ln][n][2];
				}
			}
		}	
		return move;
	}
	
	
	
	//checks if the game has come to a draw
	public static boolean draw(int[][][] b,int[][][] l){
		boolean draw = true;
		for(int i=0;i<76;i++){
			int sum=0;
			for(int j=0;j<4;j++){
				sum+= b[l[i][j][0]][l[i][j][1]][l[i][j][2]];			
			}
			if(sum<5||sum%5==0){
				draw=false;
			}
		}
		return draw;
	}
	
	//checks if the computer wins
	public static boolean compWin(int[][][] b,int[][][] l){
		boolean compwin=false;
		for(int i=0;i<76;i++){
			int sum=0;
			for(int j=0;j<4;j++){
				sum+= b[l[i][j][0]][l[i][j][1]][l[i][j][2]];
			}
			if(sum==4){
				compwin=true;
			}
		}
		return compwin;
	}
	
	//checks if either player has won
	public static boolean checkWin(int[][][] b,int[][][] l){
		boolean win =false;
		for(int i=0;i<76;i++){
			int sum=0;
			for(int j=0;j<4;j++){
				sum+= b[l[i][j][0]][l[i][j][1]][l[i][j][2]];
			}
			if(sum==20){
				win=true;
			}else if(sum==4){
				win=true;
			}
		}
		return win;
	}
}

