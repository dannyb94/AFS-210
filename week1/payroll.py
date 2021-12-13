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
            regPay = 40 * emp.hourly
            otPay = (hrsWrkd - 40) * (emp.hourly * 1.5)
            return regPay + otPay
            # return ((hrsWrkd * emp.hourly) * 1.5)

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

fname = input("Employee first name: ")
lname = input("Employee last name: ")
empId = int(input("Employee Id#: "))
hourly = float(input("Employee pay rate: "))
hrsWrkd = float(input("Hours worked: "))
# sumOfHrs = str(float(hourly * hrsWrkd))

employee1 = employee(fname, lname, empId, hourly)
# print(sumOfHrs)
print("Hola " + employee1.getFname() + " " + employee1.getLname() + ". You'll be paid " + str(employee1.pay(hrsWrkd)) + " for the week.")