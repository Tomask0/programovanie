class Time:
    def __init__(self, hours, minutes):
        self.hours = hours   
        self.minutes = minutes

    def display(self):
        print(self.hours, self.minutes)   
    
    def getTime(self):
        print(self.hours, self.minutes)   

    def add(self, newHours, newMinutes):
        self.hours = self.hours + newHours
        self.minutes = self.minutes + newMinutes

        if self.minutes > 59:
            self.hours += self.minutes//60
            self.minutes = self.minutes - (60*(self.minutes//60))

        if self.minutes < 0:
            self.minutes *= -1 

            self.hours -= (self.minutes//60)
            self.minutes = 60 - (self.minutes%60) 
            
            self.display()

cas = Time(10, 00)
cas.display() 
cas.add(0, -60) 
#cas.display() 