package day12;

public class MyThre {
	public static void printNum() {
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				for(int i=0; i<10000; i++) {
					System.out.print(i);
					if(i%100==0) {
						System.out.println();
					}
				}
				
			}
		}).start();
	}
	
	public static void printChar() {
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				for(int i=0; i<10000; i++) {
					System.out.print((char)i);
					if(i%100==0) {
						System.out.println();
					}
				}
				
			}
		}).start();
	}
	
	public static void main(String[] args) {
		printNum();
		printChar();
	}
}
