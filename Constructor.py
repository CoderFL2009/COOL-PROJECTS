class Person:
    #Constructor to initialiazation attributes
    def __init__(self, name, age):
        self.name = name #Initialize the 'name' attribute
        self.age = age #Initialize the 'age' attribute

    #method to dsplay person details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

#Creating an instance of the person class
person1 = Person("Myna", 3) #Constructor is called with name="Myna" and age="3"
person2 = Person("Nina", 2) #Constructor is called with name="Nina" and age="2"
person3 = Person("Tina", 2) #Constructor is called with name="Tina" and age="2"

#Accessing methods
person1.display_info() #Output Name: Myna, Age: 3
person2.display_info() #Output Name: Nina, Age: 2
person3.display_info() #Output Name: Tyna, Age: 2
