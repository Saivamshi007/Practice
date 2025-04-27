#single inheritance
class Accessories():
    def __init__(self,pads,wipers):
        self.pads = pads
        self.wipers = wipers
    def get_accessories(self):
        return f"Accessories are number of Pads:{self.pads} and Wipers:{self.wipers}"

class Car(Accessories):
    type = "Luxury"
    def __init__(self,name,model,pads,wipers):
        super().__init__(pads,wipers)
        self.name = name
        self.model = model
    @property
    def get_details(self):
        return f"Care name and model are {self.name}, {self.model}"


#Multi-level inheritance

class Showroom(Car):
    def __init__(self,showroomname,location,carname,model,pads,wipers):
        super().__init__(carname,model,pads,wipers)
        self.location = location
        self.showroomname = showroomname
    def get_showroomdetails(self):
        return f"Show room name:{self.showroomname} and Location:{self.location}"
    
#muliple inheritance

class Employee():
    def __init__(self, name, id):
        self._name = name
        self.__id = id

    def getemployeedetails(self):
        return f"Name and id of the employee is {self.name}, {self.id}"

# car1 = Car("Venue","Compact SUV",2,4)
# print(car1.get_details)

showroom = Showroom("Sai Enterprises","Hyderabad","Venue","Compact SUV",2,4)
print(showroom.get_showroomdetails(), showroom.get_details,showroom.get_accessories())
print(showroom.__dict__)
emp = Employee("sai",125)
print(emp.__id)