import sys
sys.path.append("../authentication")
import userfuelquote.py

def test_except(test, number, success):
	try:
		fuelquote.validate(test.gallons, test.address, test.date, test.price, test.amount_due)
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
	userfuelquote.FuelHistory(30.00, "7516 Rockaway Blvd, Queens, New York, 11412", "1989-07-12", 31.25, 33.75),
	userfuelquote.FuelHistory(3.0, "171 Banker St, Brooklyn, New York, 11222", "2000-07-12", 31.25, 33.75),
	userfuelquote.FuelHistory(18.5, "7216 W 87th St, Bridgeview, IL, 60455", "1990-08-12", 31.25, 33.75),
	userfuelquote.FuelHistory(15.00, "3929 John St, High Point, NC, 27265", "2022-02-09", "31.25", 40.75),
	userfuelquote.FuelHistory(10.00, "306 Old Mill Rd, High Point, NC, 27265", "2022-03-04", 31.25, 33.75),
	userfuelquote.FuelHistory(81.27, "20720 Autumn Terrace Ln, Katy, Texas 77450", "2019-04-18", 15.9, 19.7),
	userfuelquote.FuelHistory(4.0, "319 W Springfield Rd, Springfield, Pennsylvania, 19064", "1991-11-30", 103.40, -7),
	userfuelquote.FuelHistory(0.0, "1802 Adams Pl, Hillsborough, North Carolina, 27278", "2012-03-08", 87.3, 88.3),
	userfuelquote.FuelHistory(28.5, "1201 S Hayes St Suite B, Arlington, VA, 22202", "2009-12-09", 90.5, 100.75)
]


# Validation should pass with no errors
test_except(test_cases[0], 1, True)

# Validation failed due to negative gallons requested
test_except(test_cases[1], 2, False)

# Validation failed due to invalid address
test_except(test_cases[2], 3, False)

# Validation failed due to invalid data type for price
test_except(test_cases[3], 4, False)

# Validation failed due to incorrect date
test_except(test_cases[4], 5, False)

# Validation failed due to non-existent US state (A)
test_except(test_cases[5], 6, False)

# Validation failed due to negative amount due
test_except(test_cases[6], 7, False)

# Validation failed due to zero gallons requested
test_except(test_cases[7], 8, False)

# Validation should pass with no errors
test_except(test_cases[8], 9, True)