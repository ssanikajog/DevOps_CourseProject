# Program to manage employee leave

def check_leave(emp_id, days, leave_balance):
    if emp_id not in leave_balance:
        return "Employee not found", None

    if days <= 0:
        return "Invalid number of leave days", leave_balance[emp_id]

    if leave_balance[emp_id] >= days:
        leave_balance[emp_id] -= days
        return "Leave Approved", leave_balance[emp_id]
    else:
        return "Leave Rejected (Insufficient balance)", leave_balance[emp_id]


if __name__ == "__main__":
    import sys

    print("=== Online Leave Management System ===")

    # Initial leave balance
    leave_balance = {
        "E001": 20,
        "E002": 15,
        "E003": 10
    }

    try:
        # If user gives input through command line
        if len(sys.argv) == 4:
            emp_id = sys.argv[1]
            emp_name = sys.argv[2]
            days = int(sys.argv[3])
        else:
            # Take user input interactively
            emp_id = input("Enter Employee ID: ")
            emp_name = input("Enter Employee Name: ")
            days = int(input("Enter Number of Leave Days: "))

        print("\n=== Program Parameters ===")
        print(f"Employee ID   : {emp_id}")
        print(f"Employee Name : {emp_name}")
        print(f"Leave Days    : {days}")

        status, remaining = check_leave(emp_id, days, leave_balance)

        print("\n=== Leave Status ===")
        print(f"Status            : {status}")

        if remaining is not None:
            print(f"Remaining Leaves  : {remaining}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
