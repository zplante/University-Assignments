import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Client {

	public static void main(String[] args) throws IOException {
		Scanner input= new Scanner(new File("input.txt"));
		Scanner text= new Scanner(new File("shakespeare.txt"));
		File out = new File("analysis.txt");
		out.createNewFile();
		FileWriter wrt = new FileWriter("analysis.txt");
		ShakeTable tab=new ShakeTable(50);
		String shake=new String();
		while(text.hasNextLine()){
		shake = text.nextLine();
				String[] data=shake.split("\\s+");
				for(String s:data){
					s=clean(s);
			if(!s.equals(s.toUpperCase())){
			tab.Insert(s.toLowerCase());
			}
				}
		}
		tab.sort();
		while(input.hasNextLine()){
			String line=input.nextLine();
			if(line.contains(" ")){
				String[] data=line.split("\\s+");
				wrt.write(tab.mostCommon(Integer.parseInt(data[0]), Integer.parseInt(data[1])));
			}else{
				wrt.write(""+tab.frequency(line));
			}
			wrt.write("\n");
		}
		
		
		
		wrt.close();
		input.close();
		text.close();
	}
public static boolean isAlpha(String s){
		String alpha="abcdefghijklmnopqrstuvwxyz'- ";
		for(int i=0;i<alpha.length()-1;i++){
			if(s.equalsIgnoreCase(alpha.substring(i, i+1))){
				return true;
			}
		}

		return false;
	}
	public static String clean(String s){
		String ret=s;
		String comp=new String();
		for(int i=0;i<ret.length();i++){
			if(i==ret.length()-1){
				comp=ret.substring(i);
			}else{
				comp=ret.substring(i, i+1);
			}
			if(!isAlpha(comp)){
				if(i==0){
					ret=ret.substring(1);
				}else if(i==ret.length()-1){
					ret=ret.substring(0,i);
				}else{
					ret=ret.substring(0,i)+ret.substring(i+1);
				}
				i--;
			}
		}
		return ret;
	}
}
