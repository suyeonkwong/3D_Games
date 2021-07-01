package day02;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println(hum.age);
		System.out.println(hum.skill_speak);
		hum.aging();
		hum.learnSpeak(5);
		System.out.println(hum.age);
		System.out.println(hum.skill_speak);
		
	}
}
