# Simple Account Points Calculation Test

print("Account Points Calculator")

# Input values
login_points = int(input("Enter login points: "))
purchase_points = int(input("Enter purchase points: "))
bonus_points = int(input("Enter bonus points: "))

# Calculate total points
total_points = login_points + purchase_points + bonus_points

# Display result
print("Total Account Points:", total_points)

# Simple status check
if total_points >= 100:
    print("Status: Gold Account")
elif total_points >= 50:
    print("Status: Silver Account")
else:
    print("Status: Basic Account")
