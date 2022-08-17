string = "10/0/0"

emp_strubg = ""

for m in string:
    if m.isdigit():
        emp_strubg = emp_strubg + m
emp_strubg = int(emp_strubg)

print("numbers are: ", type(emp_strubg))