import random
class Employee:
    def __init__(self):
        self.total_hours = 0
        self.total_days_present = 0
        self.total_wage = 0
    def check_attendance(self):
        """ 
        Description: taking random choice of employees attendance where 0 = absent , 1 = part time , 2 = full time
        parameters: no parameters
        return: returns the random value of attendance of an employee"""
        attendance = random.choice([0,1,2])
        return attendance
# calculating employees daily working hours and daily wage
    def emp_daily_wage(self):
        """
        Description: Checks whether the employee is present or not and based on that calculates its daily wage and number of hours worked
        Parameters: None
        Return : returns the daily wage , hours worked and employees attendance
        """
        emp_check = self.check_attendance()
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
    def emp_monthly_wage(self):
        """
        Description: Calculates wages till a condition of total working hours or days is reached for a month
        Parameters: None
        Returns: print the details of an employee
        """
        days_in_month = 1
        num_days = []
        while self.total_hours<=100 and self.total_days_present<=20 and days_in_month<=30:
            daily_wage,daily_hours,status = self.emp_daily_wage()
            if status > 0:
                self.total_hours += daily_hours
                num_days.append(status)
                self.total_days_present += 1
            else:
                num_days.append(status)
            days_in_month += 1
            self.total_wage += daily_wage
        print(f"The record of all the days = {num_days}")
        print(f"Total number of days the employee was present = {self.total_days_present}")
        print(f"Total number of hours the employee did the job = {self.total_hours}")
        print(f"The total wage = {self.total_wage}")
            

if __name__ == "__main__":
    print("Welcome to employee wages computation program")
    employee = Employee()
    employee.emp_monthly_wage()

