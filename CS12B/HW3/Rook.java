
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

	@Override
	public boolean checkMove(int a, int b, ChessList l) {
		if(x!=a&&y!=b){
			return false;
		}
		if(x==a){
			int tempY;
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
			int tempX;
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
				}
		}
		return ret;
	}
}

