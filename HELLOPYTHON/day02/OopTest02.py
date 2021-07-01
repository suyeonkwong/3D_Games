class Dog:
    def __init__(self):
        self.flag_bark = True
        
    def do_surgery(self):
        self.flag_bark = False
        
class Bird:
    def __init__(self):
        self.skill_fly = 0
    def learn(self):
        self.skill_fly += 1
        
class GaeSae(Dog, Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)

if __name__ == "__main__":
    job = GaeSae()
    print(job.flag_bark)
    print(job.skill_fly)
    job.do_surgery()
    job.learn()
    job.learn()
    job.learn()
    print(job.flag_bark)
    print(job.skill_fly)
   
    
        
    