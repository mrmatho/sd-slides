def validate_name(name):
    '''
    Validates that the name is a string between 2 and 25 characters long.
    @param name: The name to validate
    @return: A tuple (is_valid, error_message)'''
    if not isinstance(name, str):
        return False, "Name must be a string"
    if len(name) < 2 or len(name) > 25:
        return False, "Name must be between 2 and 25 characters"
    return True, ""

# Example usage
name = None
while name is None:
    name_input = input("Enter your name: ")
    is_valid, error_message = validate_name(name_input)
    if is_valid:
        name = name_input  # Convert input to integer if valid
    else:
        print(f"Invalid name: {error_message}")