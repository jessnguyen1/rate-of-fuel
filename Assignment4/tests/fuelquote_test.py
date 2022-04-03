import sys
sys.path.append("../authentication")
import fuelquote

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
	fuelquote.FuelHistory(32.00, "201 Brighton Ct, Greenwood, Indiana, 46143", "2014-03-17", 40.00, 45.00),
	fuelquote.FuelHistory(-2, "1126 Woodworth Rd, Skaneateles, New York, 13152", "1989-07-12", 31.25, 33.75),
	fuelquote.FuelHistory(18.5, "????343?fd", "1989-07-12", 31.25, 33.75),
	fuelquote.FuelHistory(10.00, "306 Old Mill Rd, High Point, NC, 27265", "2022-03-04", "31.25", 33.75),
	fuelquote.FuelHistory(10.00, "306 Old Mill Rd, High Point, NC, 27265", "20222-03-04", 31.25, 33.75),
	fuelquote.FuelHistory(81.27, "A, A, A, 11111", "2019-04-18", 12.8, 19.7),
	fuelquote.FuelHistory(4.0, "319 W Springfield Rd, Springfield, Pennsylvania, 19064", "1991-11-30", 103.40, -7),
	fuelquote.FuelHistory(0.0, "1802 Adams Pl, Hillsborough, North Carolina, 27278", "2012-03-08", 87.3, 88.3),
	fuelquote.FuelHistory(28.5, "706 NE 6th St, Greenfield, Iowa, 50849", "2006-12-09", 99.5, 102.75)
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
