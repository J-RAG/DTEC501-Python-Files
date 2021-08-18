# Lab 8-1-1 question 2
# By Julan Ray Avila Gutierrez, jra0108@arastudent.ac.nz

AREACODE_LENGTH = 3
EXT_NUMBER_LENGTH = 4
def validate_phone_number(area_code, extension_number, starting_digits):
    """
        Returns a Tuple of (True, phonenumber) if Phone number passes all validation criterias
        Else returns tuple of False and no number.
    """

    # Validation Criteria Checks
    if all([
        # Numbers only Validations
        "".join(map(str, starting_digits)).isdigit(),
        str(area_code).isdigit(),
        str(extension_number).isdigit(),
        # Length Validations
        len(str(area_code))== AREACODE_LENGTH,
        len(str(extension_number)) == EXT_NUMBER_LENGTH,
        # Starting Number Validation
        str(extension_number)[0] in "".join(map(str, starting_digits))
        ]):
            return True, "".join(map(str, (area_code, extension_number))) 
    return False,

# Valid extension
print(validate_phone_number(area_code = 940, extension_number = 9001, starting_digits = (8,9)))
print(validate_phone_number(area_code = "740", extension_number = "3002", starting_digits = (5,3)))
print(validate_phone_number(area_code = 740, extension_number = "7002", starting_digits = ("7",8)))
print(validate_phone_number(area_code = "940", extension_number = 6002, starting_digits = ("5",6)))
print(validate_phone_number(area_code = "940", extension_number = 9003, starting_digits = (8,9)))
print(validate_phone_number(area_code = "940", extension_number = 8004, starting_digits = (8,)))
print(validate_phone_number(area_code = "940", extension_number = "9005", starting_digits = (9,)))
print(validate_phone_number(area_code = "940", extension_number = 7005, starting_digits = (1,3,5,6,7,9)))
# Short area codes
print(validate_phone_number(area_code = 94, extension_number = 901, starting_digits = (8,9)))
print(validate_phone_number(area_code = "94", extension_number = "901", starting_digits = (8,9)))
print(validate_phone_number(area_code = 94, extension_number = "901", starting_digits = (8,9)))
print(validate_phone_number(area_code = "94", extension_number = 901, starting_digits = (8,9)))
# Invalid area code
print(validate_phone_number(area_code = "Z4", extension_number = 901, starting_digits = (1,"4")))
print(validate_phone_number(area_code = "9Q", extension_number = 901, starting_digits = ("4",5)))
# Invalid extension
print(validate_phone_number(area_code = "840", extension_number = "Z01", starting_digits = (1,"5")))
print(validate_phone_number(area_code = "850", extension_number = "9O1", starting_digits = ("6",5)))
# Invalid starting digit
print(validate_phone_number(area_code = "201", extension_number = 901, starting_digits = (1,"A")))
print(validate_phone_number(area_code = "202", extension_number = 201, starting_digits = ("Z",5)))
