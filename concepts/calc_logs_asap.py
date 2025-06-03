import math
import decimal
decimal.getcontext().prec = 100

def get_scientific(num):
    num = decimal.Decimal(num)
    
    # Calculate length of the number in a 'naive' way, without using the log
    # Using log10 here would kind of defeat the point
    # Because the length never exceeds 10, counting them manually is always possible
    length = len(str(math.floor(num))) - 1
    mantissa = num / (10 ** length)
    
    return mantissa, length

def count_digits(num, precision: int):
    assert(precision > 0)
    
    mantissa, exponent = get_scientific(num ** 10)
    
    # Apply the trick here by doing the calculation iteratively
    for _ in range(precision - 1):
        # Use the properties of exponents
        # (m x 10^exp)^10 = m^10 x 10^(10 * exp)
        mantissa = mantissa ** 10
        exponent *= 10
        
        mantissa, new_exponent = get_scientific(mantissa)
        # Calculate the contribution of the new mantissa to the exponent and add it
        exponent += new_exponent

    return exponent
    
def logarithm(num, precision):
    # Count the number of digits
    n_digits = count_digits(num, precision)
    # Divide by the exponent
    result = n_digits / decimal.Decimal(10 ** precision)
    
    return f"{result:.{precision}f}"
