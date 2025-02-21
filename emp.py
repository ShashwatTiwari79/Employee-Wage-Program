import random

def check_attendance():
    print("Welcome to employee wages computation program")
    attendance = random.choice([0,1,2])
    if attendance == 2:
        print("The employee is present for the full day")
    elif attendance == 1:
        print("The employee is present for the half day")
    else:
        print("The employee is absent")
    return attendance
def emp_daily_wage():
    wage_per_hour = 20
    emp_check = check_attendance()
    if emp_check == 2:
        daily_wage = wage_per_hour*8
        print(f"The employee is present for the entire day so daily wage is : {daily_wage}")
    if emp_check == 1:
        daily_wage = wage_per_hour*4
        print("The employee is present for the half day")
    else:
        daily_wage = 0
        print(f"The employee was absent for the entire day so daily wage is : {daily_wage}")
if __name__ == "__main__":
    emp_daily_wage()

