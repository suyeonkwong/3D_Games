package day14;

public class MyRef {
	
	public static void changeVal(int a) {
		a = 5;
	}
	
	public static void changeRef(int[] a) {
		a[0] = 5;
	}
	
	public static void main(String[] args) {
	
		int a = 0;
		int[] b = {0};
		
		System.out.println(a);
		System.out.println(b[0]);
		changeVal(a);
		changeRef(b);
		System.out.println(a); //주소지(reference값이 아님)가 아님. 자바는 String까지가 value값이고 뒤에 arrayList부터 reference값임.
		System.out.println(b[0]);
	}
}
