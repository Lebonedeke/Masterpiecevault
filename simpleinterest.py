principal_amount = int(input('Insert the Principal amount: '))
years = int(input('Enter the number of Years: '))
interst_rate = float(input("Interest rate :"))

simple_interest = principal_amount * (interst_rate/ 100) * years

print(f'Simple Interest is : {simple_interest}')

monthly_interest = simple_interest / 12
print(f'the interest accumulated each month is : {monthly_interest}')