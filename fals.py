principal = float(input("Enter the principal amount originally deposited: $"))
annual_interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
compounding_frequency = int(input("Enter the number of times interest is compounded per year: "))
years = int(input("Enter the number of years the account will earn interest: "))
amount = principal * (1 + (annual_interest_rate / compounding_frequency))**(compounding_frequency * years) 

print(f"After {years} years, your account will have ${amount:.2f}.")