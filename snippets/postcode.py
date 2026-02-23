def postcode_validate(postcode):
    """
    @param: postcode - the postcode input to be validated
    @return: Tuple(is_valid: boolean, message: string)
    """
    # Type Check
    if not isinstance(postcode, str):
        return False, "Postcode should be a string"
    # Range Check
    if len(postcode) != 4:
        return False, "Postcode should be 4 digits long"
    # Validating can be turned into an integer
    try:
        int(postcode)
    except(ValueError):
        return False, "Postcode should be able to be converted to integer"
    
    return True, ""

postcodes = ["1234", 1234, "123A", "123", "12345", True]

for code in postcodes:
    valid, msg = postcode_validate(code)
    if valid:
        print(f"Postcode {code} valid")
    else:
        print(f"Postcode {code} invalid. {msg}")
