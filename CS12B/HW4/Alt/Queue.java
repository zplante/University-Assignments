
public class Queue {
	Node head=null;
	
	public void Insert(int a,int b){
		if(head==null){
			head=new Node(a,b);
		}else{
		Node trav=head;
		while(trav.next!=null){
			trav=trav.next;
		}
		trav.next=new Node(a,b);
		}
	}
	public Node DeleteMax(){
		if(head==null){
			return null;
		}else{
			Node ret=head;
			int max=head.pri;
			Node trav=head;
			while(trav!=null){
				if(max<trav.pri){
					max=trav.pri;
					ret=trav;
				}
				trav=trav.next;
			}
			if(ret==head){
				head=head.next;
			}else{
				trav=head;
				while(trav.next!=null){
					if(trav.next==ret){
						trav.next=trav.next.next;
					}else{
					trav=trav.next;
					}
				}
			}
			return ret;
		}
	}
	public void print(){
		Node trav=head;
			if(trav==null){
				System.out.print("null");
			}else{
				while(trav!=null){
					System.out.print(trav.id+" "+trav.pri+" ");
					trav=trav.next;
			}
		}
			System.out.println("");
	}
}
