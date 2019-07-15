
public class Queen extends ChessPiece {

	public Queen(int a, int b,int c, boolean temp) {
		super(a, b,c, temp);
		
	}

	@Override
	public boolean checkAttack(ChessPiece en) {
		if(en.x==x){
			return true;
		}
		else if(en.y==y){
			return true;
		}
		else{
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
		}
	return false;
	}
	public String name(){
		if(color){
			return "q";
		}
		else{
			return "Q";
		}
	}

	@Override
	public boolean checkMove(int a, int b, ChessList l) {
		int tempX=0;
		int tempY=0;
		if(x==a||y==b){
		if(x==a){
			if(y>b){
				tempY=y-1;
				while(tempY>b){
					if(l.checkSpace(x, tempY)!=null){
						return false;
					}
					tempY--;
				}
			}
			else{
				tempY=y+1;
				while(tempY<b){
					if(l.checkSpace(x, tempY)!=null){
						return false;
					}
					tempY++;
				}
			}
		}
		else if(y==b){
			if(x>a){
				tempX=x-1;
				while(tempX>a){
					if(l.checkSpace(tempX, y)!=null){
						return false;
					}
					tempX--;
				}
			}
			else{
				tempX=x+1;
				while(tempX<a){
					if(l.checkSpace(tempX, y)!=null){
						return false;
					}
					tempX++;
				}
			}
		}
		if(l.checkSpace(a, b)!=null){
			if(color==l.checkSpace(a, b).color){
				return false;
			}
		}
		}
		else{
			if(Math.abs(x-a)!=Math.abs(y-b)){
				return false;
			}else{
				if(x>a){
					if(y>b){
						tempX=x-1;
						tempY=y-1;
						while(tempX>a&&tempY>b){
							if(l.checkSpace(tempX, tempY)!=null){
								return false;
							}
							tempX--;
							tempY--;
						}
					}else{
						tempX=x-1;
						tempY=y+1;
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
						tempX=x+1;
						tempY=y-1;
						while(tempX<a&&tempY>b){
							if(l.checkSpace(tempX, tempY)!=null){
								return false;
							}
							tempX++;
							tempY--;
						}
					}else{
						tempX=x+1;
						tempY=y+1;
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
				}	
	}
		return true;
	}
	@Override
	public int[][] path(int a, int b, ChessList l) {
		int[][] ret = new int[size][2];
		if(checkMove(a,b,l)){
			if(x==a){
				int tempY=y;
				if(y>b){
					int i=0;
					while(tempY>b){
						ret[i][0]=x;
						ret[i][1]=tempY;
						tempY--;
						i ++;
					}
				}
				else{
					int i=0;
					while(tempY>b){
						ret[i][0]=x;
						ret[i][1]=tempY;
						tempY++;
						i ++;
					}
				}
			}
			else if(y==b){
				int tempX=x;
				if(x>a){
					int i=0;
					while(tempX>b){
						ret[i][0]=tempX;
						ret[i][1]=y;
						tempX--;
						i ++;
					}
				}
				else{
					int i=0;
					while(tempX>b){
						ret[i][0]=tempX;
						ret[i][1]=y;
						tempX++;
						i ++;
					}
				}
				}else{
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
		}
		return ret;
	}
	
}

