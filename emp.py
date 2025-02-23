import random
class Employee:
    @classmethod
    def check_attendance(cls):
        """ 
        Description: taking random choice of employees attendance where 0 = absent , 1 = part time , 2 = full time
        parameters: no parameters
        return: returns the random value of attendance of an employee"""
        attendance = random.choice([0,1,2])
        return attendance
# calculating employees daily working hours and daily wage
    @classmethod
    def emp_daily_wage(cls,wage_per_hour):
        """
        Description: Checks whether the employee is present or not and based on that calculates its daily wage and number of hours worked
        Parameters: None
        Return : returns the daily wage , hours worked and employees attendance
        """
        emp_check = cls.check_attendance()
        hours_worked = 0
        daily_wage = 0
        match emp_check:
            case 2 :
                hours_worked = 8
            
            case 1:
                hours_worked = 4
           
            case _:
                hours_worked = 0
        daily_wage = hours_worked*wage_per_hour
        return daily_wage,hours_worked,emp_check
# calculating employee monthly wage
    @classmethod
    def emp_monthly_wage(cls,company_name,wage_per_hour,max_working_days,max_working_hours):
        """
        Description: Calculates wages till a condition of total working hours or days is reached for a month
        Parameters: None
        Returns: print the details of an employee
        """
        days_in_month = 1
        total_hours = 0
        total_days_present = 0
        total_wage = 0
        num_days = []
        while total_hours<=max_working_hours and total_days_present<=max_working_days and days_in_month<=31:
            daily_wage,daily_hours,status = cls.emp_daily_wage(wage_per_hour)
            if status > 0:
                total_hours += daily_hours
                num_days.append(status)
                total_days_present += 1
            else:
                num_days.append(status)
            days_in_month += 1
            total_wage += daily_wage
        print(f"Company Name :- {company_name}")
        print(f"The record of all the days = {num_days}")
        print(f"Total number of days the employee was present = {total_days_present}")
        print(f"Total number of hours the employee did the job = {total_hours}")
        print(f"The total wage = {total_wage}")
            

if __name__ == "__main__":
    print("Welcome to employee wages computation program")
    employee = Employee()
    num_companies = int(input("Enter the number of companies: "))
    for i in range(num_companies):
        company_name = input("Enter the company name: ")
        wage_per_hour = int(input("Enter wage per hour: "))
        max_working_days = int(input("Enter max working days in a month: "))
        max_working_hours = int(input("Enter max working hours in a month: "))

        employee.emp_monthly_wage(company_name, wage_per_hour, max_working_days, max_working_hours)



