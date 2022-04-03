import sys
sys.path.append("../authentication")
import usercredentials.py

def test_except(test, number, success):
	try:
		profilemanagement.validate(test.userID, test.userPassword)
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
	usercredentials.ClientProfileManagement("JohnSmith23", "hunter2"),
	usercredentials.ClientProfileManagement("seveneleven*&(", "hunter2"),
	usercredentials.ClientProfileManagement("QuincyTraaaaaaaaaaaaaaaaaaaaaan", "????343?fd"),
	usercredentials.ClientProfileManagement("CorinneHarwood32", ""),
	usercredentials.ClientProfileManagement("", "hunter2"),
	usercredentials.ClientProfileManagement("GabriellaHodgso43n", "543543544gsfggsrgrgdrg"),
]


# Validation should pass with no errors
test_except(test_cases[0], 1, True)

# Validation failed due invalid chars in username
test_except(test_cases[1], 2, False)

# Validation failed due to username being over 50 chars
test_except(test_cases[2], 3, False)

# Validation failed due to empty password
test_except(test_cases[3], 4, False)

# Validation failed due to empty username
test_except(test_cases[4], 5, False)

# Validation failed due to password being over 50 chars
test_except(test_cases[5], 6, False)
