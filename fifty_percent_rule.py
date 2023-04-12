import sys
import os


def fifty_percent_rule(monthly_mortgage, expected_rent):
	"""
	Rough estimate for how much a rental will cashflow

	ARGUMENTS:
	-------------------------------------------------
	monthly_payment (int): They monthly mortgage payment
		includes only principal and interest

	projected_rent (int): The gross rent potential
		of the property


	RETURNS:
	-------------------------------------------------
	monthly_cashflow (int): estimated monthly casflow

	"""

	monthly_cashflow = .50 * expected_rent - monthly_mortgage
	print("""

	FIFTY PERCENT RULE:
	-------------------------------------------------

	Expected Cashflow: {0}

	Assuming the following: 
		Expected Rent: {1}
		Monthly mortgage: principal & interest = {2}
		All other expenses = 50 pct of expected rent

	""".format(monthly_cashflow, expected_rent, monthly_mortgage))
	return monthly_cashflow


if __name__ == '__main__':
	monthly_mortgage = int(sys.argv[1])
	expected_rent = int(sys.argv[2])

	fifty_percent_rule(monthly_mortgage=monthly_mortgage, expected_rent=expected_rent)
