from functools import reduce

"""Calculate sum of the three months' income"""


def calculate_income(code, excel_data):
	income_first_month, income_second_month, income_third_month = [], [], []
	sum_income_m1, sum_income_m2, sum_income_m3 = 0, 0, 0
	for i in excel_data:
		if i[1] == code:
			income_first_month.append(float(i[7]))
			sum_income_m1 = reduce(lambda x, y: x + y, income_first_month)
			
			income_second_month.append(float(i[8]))
			sum_income_m2 = reduce(lambda x, y: x + y, income_second_month)
			
			income_third_month.append(float(i[9]))
			sum_income_m3 = reduce(lambda x, y: x + y, income_third_month)
	
	return sum_income_m1, sum_income_m2, sum_income_m3


"""Calculate sum of the last months' income"""


def calculate_income_last_month(code, excel_data):
	income = []
	sum_income = 0
	for i in excel_data:
		
		if i[1] == code:
			income.append(float(i[9]))
			sum_income = reduce(lambda x, y: x + y, income)
	return sum_income


"""Calculate change of income between the last month and the previous one"""


def calculate_change(code, excel_data):
	income_second_month, income_third_month = [], []
	sum_income_m2, sum_income_m3 = 0, 0
	for i in excel_data:
		if i[1] == code:
			income_second_month.append(float(i[8]))
			sum_income_m2 = reduce(lambda x, y: x + y, income_second_month)
			
			income_third_month.append(float(i[9]))
			sum_income_m3 = reduce(lambda x, y: x + y, income_third_month)
	
	return round(abs(sum_income_m3 - sum_income_m2))
