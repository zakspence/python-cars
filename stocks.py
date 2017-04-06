

class Stocks:

	def __init__(self):
		self.stockDict = {'GM': 'General Motors', 'EK': 'Eastman Kodak', 'CAT': 'Caterpillar', 'AET': 'Aetna Inc', 'AMZN': 'Amazon.com Inc', 'WMT': 'Wal-Mart Stores Inc'}
		self.purchases = [('GM', 20, '12-28-1985', 24), ('CAT', 95, '03-18-1999', 30), ('WMT', 58, '06-06-1966', 12), ('AMZN', 200, '01-23-2000', 30), ('GM', 50, '12-28-2007', 19)]

	def print_purchase_history(self):
		print('\nPurchase History')
		print('------------------------------')
		counter = 0
		for purchase in self.purchases:
			number_of_shares = purchase[1]
			price_per_share = purchase[3]
			company_name = self.stockDict[purchase[0]]
			print('{}: You bought {} shares of {} at {} per share'.format(counter, number_of_shares, company_name, price_per_share))
			counter += 1
		print('------------------------------')
		print('End of Report\n')

	def print_all_investments(self):
		all_investments = dict()
		for purchase in self.purchases:
			company = purchase[0]
			number_of_shares = purchase[1]
			if company in all_investments:
				all_investments[company] += number_of_shares
			else:
				all_investments[company] = number_of_shares
		print('\nAll Holdings')
		print('------------------------------')
		for key, val in all_investments.items():
			print('{} stocks with {}'.format(val, key))