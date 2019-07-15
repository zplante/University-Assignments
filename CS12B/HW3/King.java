public class King extends ChessPiece{


	public King(int a, int b,int c, boolean temp) {
		super(a, b,c, temp);
	}

	
	//fix for edge of board
	public boolean checkAttack(ChessPiece en) {
		if(checkShare(en.x-1,en.y)){
			return true;
		}
		else if(checkShare(en.x+1,en.y)){
			return true;
		}
		else if(checkShare(en.x,en.y-1)){
			return true;
		}
		else if(checkShare(en.x,en.y+1)){
			return true;
		}
		else if(checkShare(en.x-1,en.y+1)){
			return true;
		}
		else if(checkShare(en.x-1,en.y-1)){
			return true;
		}
		else if(checkShare(en.x+1,en.y-1)){
			return true;
		}
		else if(checkShare(en.x+1,en.y+1)){
			return true;
		}
		else{
			return false;
		}
	}

	

	public boolean isWhiteKing(){
		return color;
	}
	public boolean isBlackKing(){
		return !color;
	}
	public String name(){
		if(color){
			return "k";
		}
		else{
			return "K";
		}
	}



	@Override
	public boolean checkMove(int a, int b, ChessList l) {
		int disX = Math.abs(x-a);
		int disY = Math.abs(y-b);
		if(disX>1||disY>1){
			return false;
		}else{
			if(l.checkSpace(a, b)!=null){
				if(color==l.checkSpace(a, b).color){
					return false;
				}
			}
		}
		return true;
	}

	@Override
	public int[][] path(int a, int b, ChessList l) {
		int[][] ret = new int[1][2];
		ret[0][0]=x;
		ret[0][1]=y;
		return ret;
	}
	
	public boolean underAttack(ChessList lst){
		Node trav = lst.head;
		while(trav!=null){
			if(trav.piece.color!=color){
				if (trav.piece.checkMove(x,y,lst)){
					return true;
				}	
			}
			trav=trav.next;
		}
		return false;
	}

}

