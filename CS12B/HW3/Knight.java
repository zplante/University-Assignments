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

	@Override
	public boolean checkMove(int a, int b, ChessList l) {
		int disX=Math.abs(x-a);
		int disY=Math.abs(y-b);
		if((disX==1&&disY==2)||(disX==2&&disY==1)){
			if(l.checkSpace(a, b)==null){
				return true;
			}else if(l.checkSpace(a, b).color!=color){
				return true;
			}else{
				return false;
			}
		}else{
					return false;
				}
			}

	@Override
	public int[][] path(int a, int b, ChessList l) {
		int[][] ret = new int[1][2];
		ret[0][0]=x;
		ret[0][1]=y;
		return ret;
	}

}

