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

	@Override
	public boolean checkMove(int a, int b, ChessList l) {
	if(Math.abs(x-a)!=Math.abs(y-b)){
		return false;
	}else{
		if(x>a){
			if(y>b){
				int tempX=x-1;
				int tempY=y-1;
				while(tempX>a&&tempY>b){
					if(l.checkSpace(tempX, tempY)!=null){
						return false;
					}
					tempX--;
					tempY--;
				}
			}else{
				int tempX=x-1;
				int tempY=y+1;
				while(tempX>a&&tempY<b){
					if(l.checkSpace(tempX, tempY)!=null){
						return false;
					}
					tempX--;
					tempY++;
				}
			}
		}else{
			if(y>b){
				int tempX=x+1;
				int tempY=y-1;
				while(tempX<a&&tempY>b){
					if(l.checkSpace(tempX, tempY)!=null){
						return false;
					}
					tempX++;
					tempY--;
				}
			}else{
				int tempX=x+1;
				int tempY=y+1;
				while(tempX<a&&tempY<b){
					if(l.checkSpace(tempX, tempY)!=null){
						return false;
					}
					tempX++;
					tempY++;
				}
			}
		}
		if(l.checkSpace(a, b)!=null){
			if(l.checkSpace(a, b).color==color){
				return false;
			}
		}
		return true;
		}
	}
	@Override
	public int[][] path(int a, int b, ChessList l) {
		int[][] ret=new int[size][2];
		if(checkMove(a,b,l)){
			int tempX=x;
			int tempY=y;
			int i=0;
			if(x>a){
				if(y>b){
					while(tempX>a&&tempY>b){
						ret[i][0]=tempX;
						ret[i][1]=tempY;
						tempX--;
						tempY--;
						i++;
					}
				}else{
					while(tempX>a&&tempY<b){
						ret[i][0]=tempX;
						ret[i][1]=tempY;
						tempX--;
						tempY++;
						i++;
					}
				}
			}else{
				if(y>b){
					while(tempX<a&&tempY>b){
						ret[i][0]=tempX;
						ret[i][1]=tempY;
						tempX++;
						tempY--;
						i++;
					}
				}else{
					while(tempX<a&&tempY<b){
						ret[i][0]=tempX;
						ret[i][1]=tempY;
						tempX++;
						tempY++;
						i++;
					}
				}
			}
		}
		return ret;
	}

}

