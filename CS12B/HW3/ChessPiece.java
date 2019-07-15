
public abstract class ChessPiece {
	
	//add blocking to move and attack funtions
	int x;
	int y;
	int size;
	boolean color;
	
	public ChessPiece(int a,int b, int c, boolean temp){
		x=a;
		y=b;
		size=c;
		color=temp;
	}
	
	
	public boolean checkShare(ChessPiece en){
		boolean ret=false;
		if(en.x==x&&en.y==y){
			ret=true;
		}
		return ret;
	}
	public boolean checkShare(int m,int n){
		return (x==m&&y==n);
	}

	public abstract boolean checkAttack(ChessPiece en);
	
	public abstract boolean checkMove(int a, int b, ChessList l);
	
	public abstract int[][] path(int a, int b, ChessList l);
	
	
	public boolean isWhiteKing(){
		return false;
	}
	public boolean isBlackKing(){
		return false;
	}
	public abstract String name();
	public String toString(){
		return x+" "+y;
	}
	public void move(int a,int b){
		x=a;
		y=b;
	}
}
