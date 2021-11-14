# The user provides the message and a tuple of two integers, the way that the
# range of the first element and the second should have the inputted number
# inside or an empty tuple, returning the number without checking any range
def int_input(message: str, range_nums: tuple = ()) -> int:
    # Check if the input is an integer or not
    try:
        value_to_return: int = int(input(message))
    except ValueError:
        raise Exception("Error: Input received is not a number")

    # Case of empty tuple
    if len(range_nums) == 0:
        return value_to_return
    # Case of tuple of one integer
    elif len(range_nums) == 1:
        raise Exception("Only one element in range. Expected two.")
    # Case of tuple of more than two integers
    elif len(range_nums) < 2:
        raise Exception("More than two elements in range. Expected two.")
    # Case of tuple of two elements
    else:
        # Some element is not an integer
        if type(range_nums[0]) != int or type(range_nums[1]) != int:
            raise Exception("Element of range is not an integer")
        else:
            # Range not valid because the init is grater than the end
            if range_nums[0] > range_nums[1]:
                raise ValueError("The first number of the range cannot be "
                                 "greater than the second")
            # Valid range
            elif range_nums[0] <= value_to_return <= range_nums[1]:
                return value_to_return
            else:
                raise Exception("Error: Input not in range")
