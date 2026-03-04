#Get details of load
money_owed = float(input('How much money do you owe?\n'))
apr = float(input('What is the APR percentage of the loan?\n'))
payment = float(input('How much is the monthly payment?\n'))
months = int(input('How many months is the loan for?\n'))

monthly_rate = apr/100/12

for i in range(months):
    # Calculate interest to pay
    interest_paid = money_owed*monthly_rate

    # Add interest
    money_owed = money_owed + interest_paid

    # Make payment
    money_owed = money_owed - payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end = ' ')
    print('Now I owe', money_owed)