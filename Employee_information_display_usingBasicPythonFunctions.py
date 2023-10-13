Emp_name = input("Name\t")
id = int(input("Employement id\t"))
salary = int(input("Salary\t"))
dob = input("Date of birth\t")
job_location = input("Current work location\t")
gender = input("Gender\t")
date_of_joining =input("Date of joining\t")
blood_group=input("Blood group\t")
experience = float(input("Total no of experience\t"))
contact_info= int(input("Mobile number\t"))
Address=input("Address\t")
Aadhar_id=int(input("Enter last four digits of aadhar no\t"))

class tcs:
    def __init__(self):
        self.Emp_name = Emp_name
        self.id = id
        self.salary = salary
        self.job_location = job_location
        self.dob = dob
    def show(self):
        self.Emp_name = self.Emp_name.partition(" ")
        first_name = self.Emp_name[0]
        last_name = self.Emp_name[2]
        print(f"Hi my first name is {first_name} \nmy last name is {last_name} \nI born on {self.dob} \nMy Employment id is TCS"+ str(self.id), "\nMy salary is",round(float(self.salary),2), f"\nMy job loacation is {self.job_location}")
class hcl(tcs):
    def __init__(self):
        super().__init__()
        self.gender = gender
        self.date_of_joining = date_of_joining
        self.blood_group = blood_group
    def show(self):
        self.salary = self.salary - (self.salary*0.1)
        print(f"My name is {self.Emp_name} \nI am a {self.gender} employee with Employement id HCL"+str(self.id),f"\nMy Blood group id {self.blood_group} also i joined on {self.date_of_joining} with a net salary of {self.salary}")
class infy(tcs):
    def __init__(self):
        super().__init__()
        self.experience = experience
        self.contact_info = contact_info
        self.Address = Address
        self.Aadhar_id = Aadhar_id
    def show(self):
      self.salary = str(self.salary*12)+"LPA"
      self.Aadhar_id = "XXXX XXXX "+str(Aadhar_id)
      print(f"My name is {self.Emp_name} \nI reside at {self.Address} \nMy employement id is INFY"+str(self.id),f" \nMy salary is {self.salary} \nMy contact number is {self.contact_info}\nI have provided Aadhar as identity proof and my id is +",str(self.Aadhar_id))
print("--------TCS--------")
tcs=tcs()
tcs.show()
print("--------HCL--------")
hcl=hcl()
hcl.show()
print("--------INFY--------")
infy=infy()
infy.show()