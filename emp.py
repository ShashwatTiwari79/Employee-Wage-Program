import random

def check_attendance():
    # taking random choice of employees attendance where 0 = absent , 1 = part time , 2 = full time
    attendance = random.choice([0,1,2])
    
    return attendance
# calculating employees daily working hours and daily wage
def emp_daily_wage():
    emp_check = check_attendance()
    hours_worked = 0
    daily_wage = 0
    match emp_check:
        case 2 :
            hours_worked = 8
            
        case 1:
            hours_worked = 4
           
        case _:
            hours_worked = 0
    daily_wage = hours_worked*20
    return daily_wage,hours_worked,emp_check
# calculating employee monthly wage
def emp_monthly_wage():
    total_wage = 0
    num_days = []
    total_hours = 0
    total_days_present = 0
    days_in_month = 1
    while total_hours<=100 and total_days_present<=20 and days_in_month<=30:
        daily_wage,daily_hours,status = emp_daily_wage()
        if status > 0:
            total_hours += daily_hours
            num_days.append(status)
            total_days_present += 1
        else:
            num_days.append(status)
        days_in_month += 1
        total_wage = total_wage+daily_wage
    print(f"The record of all the days = {num_days}")
    print(f"Total number of days the employee was present = {total_days_present}")
    print(f"Total number of hours the employee did the job = {total_hours}")
    print(f"The total wage = {total_wage}")
            

if __name__ == "__main__":
    print("Welcome to employee wages computation program")
    emp_monthly_wage()

