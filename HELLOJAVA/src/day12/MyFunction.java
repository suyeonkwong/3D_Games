package day12;

public class MyFunction {
	
	public static void printNum() {
		for(int i=0; i<10000; i++) {
			System.out.print(i);
			if(i%100==0) {
				System.out.println();
			}
		}
	}
	
	public static void printChar() {
		for(int i=0; i<10000; i++) {
			System.out.print((char)i);
			if(i%100==0) {
				System.out.println();
			}
		}
	}
	public static void main(String[] args) {
		printNum();
		printChar();
	}
	
	
}
