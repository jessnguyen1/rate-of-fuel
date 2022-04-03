import sys
sys.path.append("../authentication")
import profilemanagement.py

def test_except(test, number, success):
	try:
		profilemanagement.validate(test.name, test.address1, test.address2, test.city, test.state, test.zipcode)
	except Exception as e:
		print(e)
		if success:
			print(f"TEST CASE {number} FAILED\n")
		else:
			print(f"TEST CASE {number} PASSED\n")
	else:
		print("No exceptions.")
		if success:
			print(f"TEST CASE {number} PASSED\n")
		else:
			print(f"TEST CASE {number} FAILED\n")

# Test cases
test_cases = [
	profilemanagement.ClientProfileManagement("John Smith", "306 Old Mill Rd, High Point", "Apt 302", "Houston", "TX", 27265),
	profilemanagement.ClientProfileManagement("Alaina Barbacoa Apple Korean BBQ Fitness Gram Pacer Test", "306 Old Mill Rd, High Point", "Apt 302", "Houston", "TX", 27265),
	profilemanagement.ClientProfileManagement("Quincy Tran", "????343?fd", "Apt 302", "Richmond", "VA", 12325),
	profilemanagement.ClientProfileManagement("Corinne Harwood", "253 Coleman Avenue", "Apt 308", "South Pointy Pencil Apple Bottom Jeans With the Boots and the Fur", "FL", 54334),
	profilemanagement.ClientProfileManagement("Enzo Weir", "2399 Adonais Way, High Point", "Apt 66", "Bear Claw", "AR", 65445),
	profilemanagement.ClientProfileManagement("Gabriella Hodgson", "A, A, A, 11111", "Apt 302", "Rutherford", "CA", "incorrect value"),
	profilemanagement.ClientProfileManagement("Maude Roberson", "3453 Melody Lane", "Apt of the crazy cat lady on the other side of the road", "Carrollway", "SC", -7),
	profilemanagement.ClientProfileManagement("Rizwan Newton", "1802 Adams Pl, Hillsborough Scottish Paper Projectile Mad Infrastructure", "Apt 2", "Corona", "NC", 75687),
	profilemanagement.ClientProfileManagement("Roberta Villa", "706 NE 6th St", "Apt 43", "Iowa", 25425)
]


# Validation should pass with no errors
test_except(test_cases[0], 1, True)

# Validation failed due to name being over 50 chars
test_except(test_cases[1], 2, False)

# Validation failed due to invalid address
test_except(test_cases[2], 3, False)

# Validation failed due to city being over 100 chars
test_except(test_cases[3], 4, False)

# Validation failed due to invalid data type for zipcode
test_except(test_cases[4], 5, False)

# Validation failed due to address 2 being over 100 chars
test_except(test_cases[5], 6, False)

# Validation failed due to invalid zipcode (negative)
test_except(test_cases[6], 7, False)

# Validation failed due to address 1 being over 100 chars
test_except(test_cases[7], 8, False)

# Validation should pass with no errors
test_except(test_cases[8], 9, True)