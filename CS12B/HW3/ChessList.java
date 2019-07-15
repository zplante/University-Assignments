
public class ChessList {
	Node head=null;
	
	public void add(Node n){
		n.next=head;
		head=n;
	}
	
	
	
	
	//returns false if two pieces share a spot
	public boolean checkNotShare(){
		boolean ret = true;
		Node trav=head;
		while(trav!=null){
			Node trav2=trav.next;
			while(trav2!=null){
				ChessPiece spot = trav.piece;
				ChessPiece com = trav2.piece;
				if(spot.checkShare(com)){
					ret=false;
				}
				trav2=trav2.next;
			}
			trav=trav.next;
		}
	return ret;	
	}
	//returns true if a piece can attack another piece
	
	public boolean checkAttack(){
		boolean ret = false;
		Node trav=head;
		while(trav!=null){
			Node trav2=trav.next;
			while(trav2!=null){
				ChessPiece spot = trav.piece;
				ChessPiece com = trav2.piece;
				if(spot.checkAttack(com)){
					ret=true;
				}
				trav2=trav2.next;
			}
			trav=trav.next;
		}
	return ret;	
	}
	//returns a string of the first possible attack possible
	public String firstAttack(){
		String ret = "-";
		Node trav=head;
		while(trav!=null){
			Node trav2=trav.next;
			while(trav2!=null){
				ChessPiece spot = trav.piece;
				ChessPiece com = trav2.piece;
				if(spot.checkAttack(com)){
					ret=spot.name()+" "+spot.toString()+" "+com.name()+" "+com.toString();
				}
				trav2=trav2.next;
			}
			trav=trav.next;
		}
	return ret;	
	}
	//returns true if there is a king of each color
	public boolean checkKings(){
		int bk=0;
		int wk=0;
		Node trav=head;
		while(trav!=null){
			ChessPiece p = trav.piece;
			trav=trav.next;
			if(p.isBlackKing()){
				bk++;
			}
			if(p.isWhiteKing()){
				wk++;
			}
		}
		boolean ret = (bk==1&&wk==1);
		return ret;
	}
	//checks if the board is valid
	public boolean checkValid(){
		return (checkNotShare()&&checkKings());
		}
	
//returns something at a spot
	public ChessPiece checkSpace(int a,int b){
		Node trav=head;
		while(trav!=null){
			ChessPiece p = trav.piece;
			if(p.checkShare(a, b)){
				return p;
			}
			trav=trav.next;
		}
		return null;
	}
	public ChessPiece find(int a, int b){
		Node trav=head;
		while(trav!=null){
			ChessPiece p = trav.piece;
			if(p.x==a&&p.y==b){
				return p;
			}
			trav=trav.next;
		}
		return null;
	}
	
	public void remove(ChessPiece p){
		if(head.piece==p){
			head=head.next;
		}else{
		Node trav=head;
		while (trav.next!=null){
			if(trav.next.piece==p){
				trav.next=trav.next.next;
			}
			trav=trav.next;
		}
		}
	}
	

}
