public class Rook extends ChessPiece{

	public Rook(int a, int b, int c, boolean temp) {
		super(a, b, c, temp);
	}

	@Override
	public boolean checkAttack(ChessPiece en) {
		boolean ret = false;
		if(en.x==x||en.y==y){
			ret =true;
		}
		return ret;
	}
	public String name(){
		if(color){
			return "r";
		}
		else{
			return "R";
		}
	}
}

