class Time:
    def __init__(self, hours, minutes):
        self.hours = hours   
        self.minutes = minutes

    def convertMinutes(self):
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
    
    def display(self):
        print(self.hours, self.minutes)   
    
    def getTime(self):
        print(self.hours, self.minutes)   

    def add(self, newHours, newMinutes):
        self.hours = self.hours + newHours
        self.minutes = self.minutes + newMinutes
        cas.convertMinutes() 

cas = Time(10, 00)
cas.display() 
cas.add(2, -80)  
cas.display() 