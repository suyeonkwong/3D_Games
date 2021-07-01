class Animal:
    def __init__(self):
        self.age = 0
        
    def aging(self):
        self.age += 1
        
class Human(Animal) :
    def __init__(self):
        print("생성자")
        super().__init__()
        self.skill_speak = 0
    
    def learnSpeak(self,step=1):
        self.skill_speak += step
        
    def __del__(self):
        print("소멸자")
        
    def __str__(self):
        return("{},{}".format(self.age, self.skill_speak))
        
if __name__ == "__main__":
    ani = Animal()
    print(ani.age)
    ani.aging()
    print(ani.age)
    
    hum = Human()
    print(hum)
    hum.aging()
    hum.learnSpeak(5)
    print(hum)
                