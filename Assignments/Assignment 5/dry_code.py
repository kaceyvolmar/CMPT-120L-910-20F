check_per = 0.85
save_per = 0.15
zero = 0.0


def saturdays_bank_transactions(transactions):
	checkings = 1590.80
	savings = 1096.25

	for num in transactions:
		if num >= zero:
			check = num * check_per
			save = num * save_per
			checkings += check 
			savings += save

		else: 
			check += num
			checkings -= check



	return checkings, savings

if __name__ == "__main__":
    transations = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transations)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\n", "Your new savings balance is:", '${:.2f}'.format(round(new_balance[1], 2)))
