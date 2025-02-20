import random

def check_attendance():
    print("Welcome to employee wages computation program")
    attendance = random.choice([1,0])
    if attendance == 1:
        print("The employee is present")
    else:
        print("The employee is absent")
if __name__ == "__main__":
    check_attendance()


