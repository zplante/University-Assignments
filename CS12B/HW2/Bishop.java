public class Bishop extends ChessPiece {

	public Bishop(int a, int b, int c, boolean temp) {
		super(a, b, c, temp);
	}

	@Override
	public boolean checkAttack(ChessPiece en) {
		int tempX=x;
		int tempY=y;
	while(tempX>=0&&tempY>=0){
		if(en.checkShare(tempX,tempY)){
			return true;
		}
		tempX--;
		tempY--;
	}
	tempX=x;
	tempY=y;
while(tempX<size&&tempY>=0){
	if(en.checkShare(tempX,tempY)){
		return true;
	}
	tempX++;
	tempY--;
}
	tempX=x;
	tempY=y;
while(tempX>=0&&tempY<size){
if(en.checkShare(tempX,tempY)){
	return true;
}
	tempX--;
	tempY++;
}
	tempX=x;
	tempY=y;
while(tempX<size&&tempY<size){
if(en.checkShare(tempX,tempY)){
	return true;
}
	tempX++;
	tempY++;
}

return false;
	}
	public String name(){
		if(color){
			return "b";
		}
		else{
			return "B";
		}
	}

}

