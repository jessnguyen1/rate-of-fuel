from datetime import datetime

class FuelHistory:
	def __init__(self, gallons, address, date, price, amount_due):
		self.gallons = gallons
		self.address = address
		self.date = date
		self.price = price
		self.amount_due = amount_due

# List of states for address validation purposes
states = [
	"Alabama",
	"Alaska",
	"Arizona",
	"Arkansas",
	"California",
	"Colorado",
	"Connecticut",
	"Delaware",
	"Florida",
	"Georgia",
	"Hawaii",
	"Idaho",
	"Illinois",
	"Indiana",
	"Iowa",
	"Kansas",
	"Kentucky",
	"Louisiana",
	"Maine",
	"Maryland",
	"Massachusetts",
	"Michigan",
	"Minnesota",
	"Mississippi",
	"Missouri",
	"Montana",
	"Nebraska",
	"Nevada",
	"New Hampshire",
	"New Jersey",
	"New Mexico",
	"New York",
	"North Carolina",
	"North Dakota",
	"Ohio",
	"Oklahoma",
	"Oregon",
	"Pennsylvania",
	"Rhode Island",
	"South Carolina",
	"South Dakota",
	"Tennessee",
	"Texas",
	"Utah",
	"Vermont",
	"Virginia",
	"Washington",
	"West Virginia",
	"Wisconsin",
	"Wyoming",
]

states_short = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HA", "ID", "IL", "IN", "IA", "KA", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Data validation function
def validate(gallons, address, date, price, amount_due):
	if gallons <= 0:
		raise Exception("Gallons must be a non-zero positive integer.")
	
	a = address.split(", ")
	if len(a) != 4:
		raise Exception("Invalid address format.")
	else:
		if a[2] not in states and a[2] not in states_short:
			raise Exception("Invalid state.")

		if len(a[3]) == 10:
			b = a[3].split("-")
			if len(b) != 2:
				raise Exception("Invalid ZIP code format.")
			else:
				if not (len(b[0]) == 5 and len(b[1]) == 4):
					raise Exception("Invalid ZIP code format.")
				
				try:
					i = int(b[0])
					i = int(b[1])
				except:
					raise Exception("Invalid ZIP code format.")
		elif len(a[3]) == 5:
			try:
				i = int(a[3])
			except:
				raise Exception("Invalid ZIP code format.")
		else:
			raise Exception("Invalid ZIP code format.")
	
		try:
			t = datetime.strptime(date, "%Y-%m-%d")
		except:
			raise Exception("Invalid date format.")

		if type(price) != float:
			raise Exception("Invalid price type.")
		elif price < 0:
			raise Exception("Invalid price (must be positive).")

		if type(amount_due) != float:
			raise Exception("Invalid amount due type.")
		elif price < 0:
			raise Exception("Invalid amount due (must be positive).")

# Data retrieval to be implemented at a later assignment, once the database is set up
# This is an array of FuelHistory
history = []

# Example values, real data will be pulled from the database
gallons = 30
address = "3514 Hickory Street, Ogden, Utah, 84414"
date = "2014-05-17"
price = 42.50
amount_due = 45.00
