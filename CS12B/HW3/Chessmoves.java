import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

//Zac Plante, zplante
//HW 3
//This code is capable of handling Bishops, Pawns, Knights
//This code runs weak checkmate
public class Chessmoves {

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
					//creates ChessList of pieces
					int size = Integer.parseInt(data[0]);
					for(int i=1;i<data.length;i+=3){
						String name=data[i];
						int x=Integer.parseInt(data[i+1]);
						int y=Integer.parseInt(data[i+2]);
						Node temp=new Node(createPiece(name,x,y,size));
						list.add(temp);
					}
					
					String whiteCheck="";
					String blackCheck="";
					Node trav=list.head;
					while(trav!=null){
						if(trav.piece.isWhiteKing()){
							if(Check(trav.piece, list)){
								if(Checkmate(trav.piece,list)){
									whiteCheck+="White checkmated ";
								}else{
									whiteCheck+="White in check ";
								}
							}
						}
						if(trav.piece.isBlackKing()){
							if(Check(trav.piece, list)){
								if(Checkmate(trav.piece,list)){
									blackCheck+="Black checkmated ";
								}else{
									blackCheck+="Black in check ";
								}
							}
						}
						
						trav=trav.next;
					}
					if(whiteCheck=="White checkmated "){
						blackCheck="";
					}
					if(blackCheck=="Black checkmated "){
						whiteCheck="";
					}
					String printCheck=whiteCheck+blackCheck;
					if(printCheck.equals("")){
						printCheck+="All kings safe";
					}
					printCheck+="\n";
					
					
						String printer = "Valid ";
						int i=0;
						//checks moves
						while(i<ar.length&&printer.equals("Valid ")){
							int argX = Integer.parseInt(ar[i]);
							int argY = Integer.parseInt(ar[i+1]);
							ChessPiece p=list.find(argX, argY);
							int argX2 = Integer.parseInt(ar[i+2]);
							int argY2 = Integer.parseInt(ar[i+3]);
							if(p.checkMove(argX2, argY2, list)){
								if(list.find(argX2, argY2)!=null){
									list.remove(list.find(argX2, argY2));
								}
								p.move(argX2, argY2);
								wrt.write(printer);
							}
							else{
								printer="Invalid";
								wrt.write(printer);
							}
							i+=4;
						}
						wrt.write("\n");
						
					//prints checkmate values
						wrt.write(printCheck);
				}	
				
				input.close();
				wrt.close();
	}
	
	
	
	
	//give checkmates a second pass
	
	
	
	

	
	//checks checkmate
	public static boolean Check(ChessPiece kng, ChessList lst){
		Node trav=lst.head;
		while (trav!=null){
			if(trav.piece.color!=kng.color){
				if(trav.piece.checkMove(kng.x, kng.y, lst)){
					return true;
					
				}
			}
			trav=trav.next;
		}
		return false;
	}
	public static boolean Checkmate(ChessPiece kng, ChessList lst){
		
			for(int i=1;i<=kng.size;i++){
				for(int j=1;j<=kng.size;j++){
						if(kng.checkMove(i, j, lst)){
							Node trav=lst.head;
							while(trav!=null){
								if(trav.piece.color!=kng.color){
									if(!trav.piece.checkMove(i, j, lst)){
										return false;
									}
								}
								trav=trav.next;
							}
						}
				}
			}
			return true;
		
	}
	
	//creates chesspieces
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

