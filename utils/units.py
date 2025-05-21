import pint
import re

ureg = pint.UnitRegistry()

def detect_conversion(input_str):
    try:
        # The speech recognition often mishears the word 'to' as 2. Fixing that here. 
        # NOTE: i cannot directly replace 2 in the input string because it might also be a number in the conversion itself.
        # hence regex is required here
        if '2' in input_str:
            speech_error_pattern = r'convert\s+(\d+(\.\d+)?)\s*([a-zA-Z]+)\s+2\s+([a-zA-Z\s]+)'
            _match = re.match(speech_error_pattern, input_str)
            if _match:
                input_str = input_str.replace('2', 'to')
                print('replaced `2` with `to`')
        
        if 'into' in input_str:
            input_str = input_str.replace('into', 'to')
            
        pattern = r'convert\s+(\d+(\.\d+)?)\s*([a-zA-Z]+)\s+to\s+([a-zA-Z\s]+)'
        match = re.match(pattern, input_str)
        
        if not match:
            return None, None, None
        

        value = float(match.group(1))
        source_unit = match.group(3)
        target_unit = match.group(4)
        
        return value, source_unit, target_unit
    except Exception as e:
        print(e)
        return "There was an error. Please try again.", e, None

def perform_conversion(value, source_unit, target_unit):
    try:
        source_quantity = value * ureg(source_unit)
        target_quantity = source_quantity.to(target_unit)
        
        return target_quantity.magnitude, target_quantity.units
    
    except pint.errors.DimensionalityError as de:
        print(de)
        return "error_conversion_not_possible", de
    except pint.UndefinedUnitError as ue:
        return "error_unit_undefined", ue


def custom_round(number):
    # Check if the number is very small or very large
    if abs(number) < 0.01 or abs(number) > 1000000:
        formatted_number = "{:.2e}".format(number)  # Report in scientific notation
        # Remove the ".00" from very small and very large numbers
        formatted_number = formatted_number.replace(".00", "")
        return formatted_number
    elif abs(number) < 0.01 and abs(number) != 0:
        # Convert small non-zero numbers to scientific notation
        return "{:.2e}".format(number)
    else:
        # Round to 2 decimal places if the number is not a whole number
        rounded_number = round(number, 2)
        if rounded_number % 1 == 0:
            return str(int(rounded_number))  # Convert to integer if it's a whole number
        else:
            return "{:.2f}".format(rounded_number)
         
def sci_not(number):
    # convert the e+09 or etc to spoken values. 10 raised to 9, etc
    number = str(number)
    if "e" in number:
        mantissa, exponent = number.split("e")
        sign = exponent[0]
        if exponent[1] == "0":
            exponent = exponent[2]
        
        if sign == "-":
            exponent = "negative " + exponent
        else:
            exponent = exponent.replace("+", '')
        return mantissa + " into 10 to the power of " + exponent
    else:
        return number
    
def convert(query):
    value, source_unit, target_unit = detect_conversion(query)

    if value is None:
        return "Invalid input. Please try again."
    
    converted_value, converted_unit = perform_conversion(value, source_unit, target_unit)

    if converted_value == "error_conversion_not_possible":
        return f"conversion not possible from {source_unit} to {target_unit}. Please check your units."
    elif converted_value == "error_unit_undefined":
        return converted_unit + " please try again." #converted_unit stores the error message
    
    # clean up the output
    # remove ".0" from the values if it exists there
    if converted_value % 1 == 0:
        converted_value = int(converted_value)
    if value % 1 == 0:
        value = int(value)   

    converted_value = sci_not(custom_round(converted_value))
    
    return f"{value} {source_unit} is {converted_value} {converted_unit}"
