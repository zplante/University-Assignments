public class Knight extends ChessPiece{

	public Knight(int a, int b, int c, boolean temp) {
		super(a, b, c, temp);
		
	}

	@Override
	public boolean checkAttack(ChessPiece en) {
		boolean ret=false;
		if(en.checkShare(x+1, y+2)){
			ret=true;
		}
		else if(en.checkShare(x+2,y+1)){
			ret=true;
		}
		else if(en.checkShare(x-1,y+2)){
			ret=true;
		}
		else if(en.checkShare(x-2,y+1)){
			ret=true;
		}
		else if(en.checkShare(x+1,y-2)){
			ret=true;
		}
		else if(en.checkShare(x+2,y-1)){
			ret=true;
		}
		else if(en.checkShare(x-2,y-1)){
			ret=true;
		}
		else if(en.checkShare(x-1,y-2)){
			ret=true;
		}
		return ret;
	}
	public String name(){
		if(color){
			return "n";
		}
		else{
			return "N";
		}
	}

}

