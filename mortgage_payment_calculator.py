import sys
import os
import numpy as np
from scipy.optimize import fsolve


def monthly_payment(loan_amount, int_rate, years):
	"""
	Calculates the monthly payment on a loan

	ARGUMENTS:
	--------------------------------------
	loan_amount (int): amount borrowed
	int_rate (float): yearly interest rate
	years (int): term of loan 

	RETURNS:
	--------------------------------------
	pmt_amount (singleton): monthly payment


	"""
	
	fv = 0
	pv = loan_amount
	int_rate = int_rate	
	years = years

	rate = int_rate / 12
	nper = years * 12
	

	def f(pmt):
		return fv + pv*(1 + rate)**nper + pmt*(1 + rate*0) / rate*((1 + rate)**nper - 1)
	
	pmt_amt = int(fsolve(f, [100], xtol=0.000001))

	print("""

	Monthly Mortgage Estimate

	-------------------------
	
	The Monthly Payment is {0}

	For a loan with the following parameters:

	Loan Amount: {1}
	Yearly Interest Rate: {2}
	Term of Loans: {3} years
	-------------------------

	""".format(pmt_amt, loan_amount, int_rate, years))


	return pmt_amt

if __name__ == '__main__':
	loan_amount = int(sys.argv[1])
	int_rate = float(sys.argv[2])
	years = int(sys.argv[3])

	monthly_payment(loan_amount=loan_amount,int_rate=int_rate,years=years)
