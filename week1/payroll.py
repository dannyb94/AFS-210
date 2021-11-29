class employee:
    def __init__(emp, fname, lname, empId, hourly):
        emp.fname = fname
        emp.lname = lname
        emp.empId = empId
        emp.hourly = hourly

    def pay(emp, hrsWrkd):
        emp.hrsWrkd = hrsWrkd
        if hrsWrkd <= 40:
            return hrsWrkd * emp.hourly
        if hrsWrkd > 40:
            return ((hrsWrkd * emp.hourly) * 1.5)

    def getFname(emp):
        return emp.fname

    def getLname(emp):
        return emp.lname

    def getEmpId(emp):
        return emp.empId

    def getHourly(emp):
        return emp.hourly

# TESTING
    # employee1 = employee("Sam", "Anthah", 3001, 17.25)
    # employee2 = employee("Aneidra", "Wade", 3004, 34.12)

    # print(employee1.getHourly())
    # print(employee1.getLname())
    # print(str(hrs))
    # print(employee1.pay(10))
    # print(employee1.pay(42))

# fname = input("Employee first name: ")
# lname = input("Employee last name: ")
# empId = input("Employee Id#: ")
hourly = float(input("Employee pay rate: "))
hrsWrkd = int(input("Hours worked: "))
sumOfHrs = str(float(hourly * hrsWrkd))

print(sumOfHrs)
# print("Hola " + fname + " " + lname + ". You'll be paid " + sumOfHrs + " for the week.")





# newEmployee = employee(firstName, lastName, empID, hourlyPay)

# print(firstName + " " + lastName + " worked " + str(hours) + " hours this week and earned " + str(newEmployee.pay(hours)))



# Sample Output:

# Please enter the Employee's ID: 1
# Please enter the Employee's First Name: John
# Please enter the Employee's Last Name: Doe
# Please enter the Employee's Hourly Pay Rate: 17.50
# How many hours did John work this week? 26.25
# John Doe's  paycheck amount is $459.38

 
# Please enter the Employee's ID: 28
# Please enter the Employee's First Name: Jane
# Please enter the Employee's Last Name: Robinson
# Please enter the Employee's Hourly Pay Rate: 24.00
# How many hours did Jane work this week? 46.25
# Jane Robinson's paycheck amount is $1185.00