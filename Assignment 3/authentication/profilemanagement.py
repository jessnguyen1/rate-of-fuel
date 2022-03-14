from datetime import datetime

class ClientProfileManagement:
	def __init__(self, name, address, address2, city, state, zipcode):
		self.name = name
		self.address1 = address
		self.address2 = address2
		self.city = city
		self.state = state
		self.zipcode = zipcode

# List of states for address validation purposes

states_short = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HA", "ID", "IL", "IN", "IA", "KA", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Data validation function
def validate(name, address, address2, city, state, zipcode):
	if zipcode <= 0 or type(zipcode) != int or len(zipcode) > 9:
		raise Exception("Zipcode must be a real number greater than zero and length must not exceed 9.")

	if len(name) > 50 or len(name < 0):
		raise Exception("Name length must not exceed 50 nor be empty.")
	else: 
		if type(name) != str:
			raise Exception("Name must be string.")
  
	if len(address1) > 100 or len(address1) < 0:
		raise Exception("Address1 length must not exceed 100 nor be empty.")
          
	if len(address2) > 100 or len(address2) < 0:
		raise Exception("Address2 length must not exceed 100 nor be empty.")

	if state not in states_short:
		raise Exception("Invalid state.")


# Example values, real data will be pulled from the database
name = "John Smith"
address1 = "3514 Hickory Street"
address2 = "Apt 304"
city = "Houston"
state = "TX"
zipcode = 43223
