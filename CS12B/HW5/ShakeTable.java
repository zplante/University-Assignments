import java.util.ArrayList;

public class ShakeTable {
	ArrayList<Node> tab[];
	boolean sorted=false;
	public ShakeTable(int n){
		tab=new ArrayList[n];
	}
	
	public void Insert(String s){
		int length=s.length();
		if(tab[length]==null){
			tab[length]= new ArrayList<Node>();
		}
		boolean added=false;
		for(int i=0;i<tab[length].size();i++){
			if(tab[length].get(i).word.equals(s)){
				tab[length].get(i).times+=1;
				added=true;
			}
		}
		if (!added){
			Node temp=new Node(s);
			tab[length].add(temp);
		}
		
	}
	public int frequency(String s){
		int ret =0;
		int length = s.length();
		if(tab[length]!=null){
		for(int i=0;i<tab[length].size();i++){
			if(tab[length].get(i).word.equalsIgnoreCase(s)){
				ret=tab[length].get(i).times;
			}
		}
		}
		return ret;
	}
	public void sort(){
		for(ArrayList<Node> list:tab){
			if(list!=null){
				for(int i=0;i<list.size();i++){
					int min=list.get(i).times;
					int place = i;
					for(int j=i;j<list.size();j++){
						if(list.get(j).times<min){
							min=list.get(j).times;
							place=j;
						}
					}
					list.add(i,list.remove(place));
				}
			}
		}
		sorted=true;
	}
	public String mostCommon(int len, int num){
		String ret="";
		if(!sorted){
			System.out.println("method cannot be preformed on an unsorted table");
		}else{
			if(tab[len]!=null){
				int i=0;
				int count=1;
				while(i<tab[len].size()&&count<=num){
					if(count==num||i==tab[len].size()-1){
						ret+=tab[len].get(i).word;
						count++;
					}else{
						ret+=tab[len].get(i).word+" ";
						count++;
				}
					i++;
			}
		}
	}
		return ret;
}
}
