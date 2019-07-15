public class Vector{
	//Assignment 5
	//Zachary Plante, zplante@ucsc.edu
	//This is the  class for the data type Vector and a program to test it
			
	//default constructors based on extending Object class
	double x; //horizontal vector
	double y; //vertical vector
	
	public Vector(double a,double b){
		x=a;
		y=b;
	}
	
	public String toString(){
		String about="Magnitude: "+Magnitude()+"\n";
		about+="Angle: "+GetAngle()+" rads\n";
		about+="Horizontal Magnitude: "+x+"\n";
		about+="Vertical Magnitude: "+y+"\n";
		return about;
	}
	
	//returns the Horizontal Magnitude of the vector
	public double GetX(){
		return x;
	}
	//returns the Vertical Magnitude of the vector
	public double GetY(){
		return y;
	}
	
	//returns the angle of the vector
	public double GetAngle(){
		return Math.atan2(y,x);
	}
	
	//adds the Vector with another one, creating a new Vector
	//GRADED METHOD
	public Vector SumOfVectors(Vector temp){
		double horz= x +temp.GetX();
		double vert= y +temp.GetY();
		return new Vector(horz,vert);
	}
	
	//subtracts a Vector from the Vector to create a new one
	//GRADED METHOD
	public Vector DiffOfVectors(Vector temp){
		double horz= x -temp.GetX();
		double vert= y -temp.GetY();
		return new Vector(horz,vert);
	}
	
	//returns the Magnitude of the Vector
	//GRADED METHOD
	public double Magnitude(){
		double mag = Math.sqrt((x*x)+(y*y));
		return mag;
	}
	
	//returns the Product Vector of the Vector and a scalar value
	//GRADED METHOD
	public Vector Scale(double scalar){
		double horz= x*scalar;
		double vert= y*scalar;
		return new Vector(horz,vert);
	}
	
	//returns the Dot Product of two Vectors
	//GRADED METHOD
	public double DotProd(Vector temp){
		return ((x*temp.GetX())+(y*temp.GetY()));
	}
	
	//returns the angle between the Vector and another
	//GRADED METHOD
	public double AngelBetween(Vector temp){
		double dot=DotProd(temp);
		dot= dot/Magnitude();
		dot= dot/temp.Magnitude();
		return Math.acos(dot);
	}
	
	//tests the Vector class
	public static void main(String args[]){
		Vector vec1=new Vector(3.5,4);
		Vector vec2=new Vector(5,9);
		//demonstrates the toString and describes example Vectors
		System.out.println("Vector 1\n"+vec1.toString());
		System.out.println("Vector 2\n"+vec2.toString());
		
		//tests the addition and subtraction methods
		Vector vecTest;
		vecTest=vec1.SumOfVectors(vec2);
		System.out.println("Adding Vector 1 and Vector 2 results in Vector 3 where");
		System.out.println("Vector 3\n"+vecTest.toString());
		
		vecTest=vec2.DiffOfVectors(vec1);
		System.out.println("Subtracting Vector 1 from Vector 2 results in Vector 4 where");
		System.out.println("Vector 4\n"+vecTest.toString());
		
		//tests Magnitude method
		double n = vec1.Magnitude();
		System.out.println("If the Magnitude of Vector 1 was equal to some varialbe n, n="+n+"\n");
		
		//tests Scalar Product method
		vecTest = vec1.Scale(1.2);
		System.out.println("Vector 1 multiplied (scaled) by 1.2 equals Vector 5 where");
		System.out.println("Vector 5\n"+vecTest.toString());
		
		//tests Dot Product method
		double dotp=vec1.DotProd(vec2);
		System.out.println("The Dot Product of Vectors 1 and 2 is "+dotp+"\n");
		
		//tests Angel Between Method
		double angle = vec1.AngelBetween(vec2);
		System.out.println("The angle between Vectors 1 and 2 is "+angle+" rads");
		
	}

}

