# initiate a class
class employee: 
    # special method/magic method/ dunder method - constructor
    def __init__(self):
       self.id = (123)
       self.salary = 50000
       self.designation = "SDE"

    def travel (self, destination):
        print (f"Employee is now travelling to {destination}")

# CREATE an obj/instance of the class
# printing a attributes
sam = employee()
# print (sam.id)

#calling a method
sam.travel("pune")