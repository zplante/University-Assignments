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


	@Override
	public boolean checkMove(int a, int b, ChessList l) {
		int disX=Math.abs((x-a));
		int disY=Math.abs((y-b));
		if(color){
			if(b>y){
			if(y==2){
				if(disX==0&&disY==2){
					if(l.checkSpace(a, b)==null&&l.checkSpace(a, b-1)==null){
						return true;
					}
				}
				else if(disX==0&&disY==1){
					if(l.checkSpace(a, b)==null){
						return true;
					}
				}
			}else{
				if(disX==0&&disY==1){
					if(l.checkSpace(a, b)==null){
						return true;
					}
				}
			}
			if(disX==1&&disY==1){
				if(l.checkSpace(a, b)!=null){
					if(color!=l.checkSpace(a, b).color){
						return true;
					}
				}
			}
				
			}
		}else{
			if(b<y){
			if(y==(size-1)){
				if(disX==0&&disY==2){
					if(l.checkSpace(a, b)==null&&l.checkSpace(a, b+1)==null){
						return true;
					}
				}
				else if(disX==0&&disY==1){
					if(l.checkSpace(a, b)==null){
						return true;
					}
				}
			}else{
				if(disX==0&&disY==1){
					if(l.checkSpace(a, b)==null){
						return true;
					}
			}
			}
			if(disX==1&&disY==1){
				if(l.checkSpace(a, b)!=null){
					if(color!=l.checkSpace(a, b).color){
						return true;
					}
				}
			}
		
	}
	}
		return false;
}


	@Override
	public int[][] path(int a, int b, ChessList l) {
		int[][] ret = new int[1][2];
		ret[0][0]=x;
		ret[0][1]=y;
		return ret;
	}
}



