import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

//Zachary Plante, zplante
//HW 2, CMPS12B
//This is the main mathod of a jar file designed to take in an input file
// that represents a chessboard and output and analysis of it in a .txt file
//NOTE: this .jar file is capable of handling pawns
public class Chessboard {

	public static void main(String[] args) throws IOException {
		//finds input.txt and creates analysis.txt
		Scanner input= new Scanner(new File("input.txt"));
		File analysis = new File("analysis.txt");
		analysis.createNewFile();
		FileWriter wrt = new FileWriter("analysis.txt");
		
		
		String line =new String();
		String arg =new String();
		
		while(input.hasNextLine()){
			ChessList list = new ChessList();
			//pulls arguments from input.txt
			line=input.nextLine();
			arg=input.nextLine();
			
			String[] data=line.split("\\s+");
			String[] ar = arg.split("\\s+");
			
			int xarg = Integer.parseInt(ar[0]);
			int yarg = Integer.parseInt(ar[1]);
			int size = Integer.parseInt(data[0]);
			for(int i=1;i<data.length;i+=3){
				String name=data[i];
				int x=Integer.parseInt(data[i+1]);
				int y=Integer.parseInt(data[i+2]);
				Node temp=new Node(createPiece(name,x,y,size));
				list.add(temp);
			}
				
				//checks validity and writes it into analysis.txt
				if (list.checkValid()==false){
					wrt.write("Invalid");
				}
				//if valid, finds the argument and returns an attack if possible
				else{
					if(list.checkSpace(xarg, yarg)==null){
						wrt.write("- ");
					}
					else{
						wrt.write(list.checkSpace(xarg, yarg).name()+" ");
					}
					if(!list.checkAttack()){
						wrt.write("-");
					}
					else{
						wrt.write(list.firstAttack());
					}
				}
				
			wrt.write("\n");
		}
		input.close();
		wrt.close();
	}
	
	
	//method for creating the diffrent ChessPieces
	public static ChessPiece createPiece(String tname,int tx, int ty, int tsize){
		ChessPiece ret=null;
		if(tname.equalsIgnoreCase("k")){
			ret=new King(tx,ty,tsize,tname.equals("k"));
		}
		else if(tname.equalsIgnoreCase("q")){
			ret=new Queen(tx,ty,tsize,tname.equals("q"));
		}
		else if(tname.equalsIgnoreCase("r")){
			ret=new Rook(tx,ty,tsize,tname.equals("r"));
		}
		else if(tname.equalsIgnoreCase("n")){
			ret=new Knight(tx,ty,tsize,tname.equals("n"));
		}
		else if(tname.equalsIgnoreCase("b")){
			ret=new Bishop(tx,ty,tsize,tname.equals("b"));
		}
		else if(tname.equalsIgnoreCase("p")){
			ret=new Pawn(tx,ty,tsize,tname.equals("p"));
		}
		return ret;
	}

}
