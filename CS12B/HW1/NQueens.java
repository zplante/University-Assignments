import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;


//Homework 1
//Zachary Plante, zplante
//This code is designed to take 3 command line arguments
//for a board size(n) and the placement on a the board(x,y)
//and solve the n Queens problem if possible
public class NQueens {

	public static void main(String args[]) throws IOException{
		int n=Integer.parseInt(args[0]);
		int x=Integer.parseInt(args[1]);
		int y=Integer.parseInt(args[2]);
		
		
		//Initializes board
		boolean[][] board = new boolean[n][n];
		for (boolean[] r:board){
			for(boolean t:r){
				t=false;
			}
		}
		
		//places first queen
		board[x-1][y-1]=true;
		
		//recursive NQueens solution
		boolean answer=NQueensRec(board,n-1);
		
		//creates a .txt file here
				File solution = new File("solution.txt");
				try {
					solution.createNewFile();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				try(FileWriter wrt = new FileWriter("solution.txt")){
				
		
		
		//prints values to see if it works
		if(!answer){
			wrt.write("No Solution\n");
			System.out.println("No solution given that sive and placement");
			
		}else{
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if(board[i][j]){
					System.out.println((i+1)+" "+(j+1));
					wrt.write((i+1)+" "+(j+1)+"\n");
					
				}
			}
		}
		
	}
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
	}
	
	static boolean NQueensRec(boolean[][] b,int m){
		
		//return value
		boolean ret=false;
		//stores playable y values
		ArrayList<Integer> liveY = new ArrayList<Integer>();
		int[] queensx = new int[b.length-m];
		int space=0;
		//finds playable y spaces

		for(int i=0;i<b.length;i++){
			liveY.add(i);
		}
		for (int i=0;i<b.length;i++){
			for (int j=0;j<b.length;j++){
				if(b[i][j]){
					liveY.remove((Integer)j);
					queensx[space]=i;
					space++;
				}
			}
		}
		//finds lowest playable x
		int column = 0;
		for (int a:queensx){
			if(column==a){
				column++;
			}
		}
		//base case
		if(m==0){
			ret=true;
		}
		else if(m==1){
			if(checkDiag(b,column,liveY.get(0))){
				ret=true;
				b[column][liveY.get(0)]=true;
			}else{
				ret=false;
			}
		//all other cases
		}else{
			int row=0;
			while(row<liveY.size()&&ret==false){
				boolean clear=checkDiag(b,column,liveY.get(row));
				if (clear){
					b[column][liveY.get(row)]=true;
					ret=NQueensRec(b,m-1);
					b[column][liveY.get(row)]=ret;
					
				}
				row++;
			}
			
		}
		return ret;
	}
	
	//checks the diagonals of a space for queens
	static boolean checkDiag(boolean[][] b,int x,int y){
		boolean ret=true;
		int tempX=x;
		int tempY=y;
		
		while(tempX>=0&&tempY>=0){
			if(b[tempX][tempY]){
				
				ret=false;
			}
			tempX--;
			tempY--;
		}
			tempX=x;
			tempY=y;
			
			while(tempX<b.length&&tempY>=0){
				if(b[tempX][tempY]){
					
					ret=false;
				}
				tempX++;
				tempY--;
			}
	
			tempX=x;
			tempY=y;
			
			while(tempX<b.length&&tempY<b.length){
				if(b[tempX][tempY]){
					
					ret=false;
				}
				tempX++;
				tempY++;
			}
		
			tempX=x;
			tempY=y;
			
			while(tempX>=0&&tempY<b.length){
				if(b[tempX][tempY]){
					
					ret=false;
					
				}
				tempX--;
				tempY++;
			}
		
		
		return ret;
	}
}
