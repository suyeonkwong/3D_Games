package day02;

public class Human extends Animal{
	int skill_speak = 0;
	
	public void learnSpeak() {
		skill_speak++;
	}
	
	public void learnSpeak(int step) {
		skill_speak += step;
	}
	
}
