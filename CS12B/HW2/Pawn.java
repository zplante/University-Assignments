public class Pawn extends ChessPiece {

	public Pawn(int a, int b, int c, boolean temp) {
		super(a, b, c, temp);
		
	}

	
	public boolean checkAttack(ChessPiece en) {
		boolean ret=false;
		if(color){
			if(en.checkShare(x+1, y+1)||en.checkShare(x-1, y+1)){
				ret=true;
			}
		}
			else{
				if(en.checkShare(x+1, y-1)||en.checkShare(x-1, y-1)){
					ret=true;
				}
			}
		return ret;
		}
	public String name(){
		if(color){
			return "p";
		}
		else{
			return "P";
		}
	}
	}

