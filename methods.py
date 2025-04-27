class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @staticmethod
    def get_details(name,age):
        return name+age
        
cal = Student("sai",34)
cal1 = Student.get_details("vamshi","23")
print(cal)
print(cal1)