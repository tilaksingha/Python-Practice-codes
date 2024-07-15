# Get user input for principal, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest per month
interest_per_month = (principal * rate * time) / 1200

# Calculate total amount
total_amount = principal + interest_per_month

# Print the results
print("Simple Interest per month:", interest_per_month)
print("Total Amount:", total_amount)