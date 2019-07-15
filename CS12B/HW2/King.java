public class King extends ChessPiece{


	public King(int a, int b,int c, boolean temp) {
		super(a, b,c, temp);
	}

	@Override
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

}

