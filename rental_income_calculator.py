def location_inputs(state):
	"""
	Returns city/state inputs
	"""
	city_state_inputs = {}
	if state == 'TN':
		city_state_inputs['property_tax'] = 0.049
		city_state_inputs['vacancy_rates'] = 0.07
		city_state_inputs['growth'] = 0.03


	print("""

	LOCATION INPUT
	----------------------------------

	You choose the assumptions from: {0} 

	This implies the following:

	{1} property tax
	{2} vacancy rates
	{3} growth in rent, expenses, labor etc.
	----------------------------------
		""".format(state,
			city_state_inputs['property_tax'],
			city_state_inputs['vacancy_rates'],
			city_state_inputs['growth']
			)
	)	
	return city_state_inputs

def financing_inputs(type_of_financing):
	"""
	Dictionary of financing inputs
	"""
	financing_inputs = {}
	if type_of_financing == 'conventional':
		financing_inputs['interest_rate'] = 0.06
		financing_inputs['points'] = 0.01
		financing_inputs['term'] = 30
		financing_inputs['down_payment'] = .25

	elif type_of_financing == 'preferred_lender':
		financing_inputs['interest_rate'] = 0.6
		financing_inputs['points'] = 0.03
		financing_inputs['term'] = 30
		financing_inputs['down_payment'] = .15

	elif type_of_financing == 'home_equity_loan':
		financing_inputs['interest_rate'] = 0.07
		financing_inputs['points'] = 0.00
		financing_inputs['term'] = 20
		financing_inputs['down_payment'] = 0

	print("""

	FINANCING INPUT
	----------------------------------

	You choose: {0} to finance the property

	This means that you will adhere to these terms:

	{1} interest rate
	{2} loan points
	{3} year term
	{4} down payment
	----------------------------------
		""".format(type_of_financing,
			financing_inputs['interest_rate'],
			financing_inputs['points'],
			financing_inputs['term'],
			financing_inputs['down_payment']
			)
	)
	return financing_inputs


def calc_revenue(estimated_rent, hold_period):
	num_months = hold_period * 12
	revenue = []
	for i in range(num_months):
		revenue.append(estimated_rent)
	print(revenue)
	return revenue

def calc_fixed_expenses(home_price, hold_period):
	fixed_expenses = []
	return fixed_expenses

def calc_variable_expenses():
	variable_expenses = []
	return variable_expenses

def analyze_investment():
	metrics = {}
	return metrics


def rental_income_calculator(type_of_financing):
	"""
	Returns calculator results
	"""
	location = location_inputs(state='TN')
	financing = financing_inputs(type_of_financing=type_of_financing)
	calc_revenue(estimated_rent=2300, hold_period=1)
	return None

if __name__ == '__main__':
	rental_income_calculator(type_of_financing='conventional')
