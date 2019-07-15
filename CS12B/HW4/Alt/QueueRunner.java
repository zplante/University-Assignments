import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class QueueRunner {

	public static void main(String[] args) throws IOException {
		//finds input.txt and creates analysis.txt
				Scanner input= new Scanner(new File("input.txt"));
				File out = new File("output.txt");
				out.createNewFile();
				FileWriter wrt = new FileWriter("output.txt");
			
				
				String line =new String();
				while(input.hasNextLine()){
					Queue list=new Queue();
					line=input.nextLine();
					for(int i=0;i<line.length();i++){
						if(line.charAt(i)=='('||line.charAt(i)==')'||line.charAt(i)==','){
							if(i==0){
								line=line.substring(1);
								i--;
							}else if(i==line.length()-1){
								line=line.substring(0, i);
							}else{
								line=line.substring(0, i)+line.substring(i+1);
								i--;
							}
						}
					}
					
					String[] data=line.split("\\s+");
					int count=0;
					while(count<data.length){
					list.print();
						if(data[count].equalsIgnoreCase("d")){
							Node del=list.DeleteMax();
							if(del!=null){
								wrt.write(del.id+" ");
							}else{
							wrt.write("null ");
						}
							count++;
						}else{
							list.Insert(Integer.parseInt(data[count]),Integer.parseInt(data[count+1]));
							count+=2;
						}
					}
					wrt.write("\n");
				}
				input.close();
				wrt.close();
	}
}

