import random

def check_attendance():
    
    attendance = random.choice([0,1,2])
    
    return attendance
def emp_daily_wage():
    wage_per_hour = 20
    emp_check = check_attendance()
    match emp_check:
        case 2 :
            daily_wage = wage_per_hour*8
            
        case 1:
            daily_wage = wage_per_hour*4
           
        case _:
            daily_wage = 0
    return daily_wage
def emp_monthly_wage():
    total_wage = 0
    a = []
    for i in range(20):
        a.append(check_attendance())
        everyday_wage = emp_daily_wage()
        total_wage = everyday_wage+total_wage
    print("The total working days list for 20 days where 2 is for fulltime , 1 for parttime and 0 for absent:-")
    print(f"{a}")
    print(f"Total wage for 20 days={total_wage}")


    
if __name__ == "__main__":
    print("Welcome to employee wages computation program")
    emp_monthly_wage()

