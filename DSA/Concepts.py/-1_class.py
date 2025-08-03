class Human:
    #defining properties/objects 
    def __init__(self, name, occupation):
        self.name = name #creating name object
        self.occupation = occupation
    # methods
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots film")
         
 #instance, no need to pass self
Ameya = Human("Ameya", "actor")
Ameya.do_work()