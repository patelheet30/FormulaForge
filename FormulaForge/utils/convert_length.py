def convert_length(
    length: float,
    from_unit: str,
    to_unit: str,
) -> float:
    """
    Converts length from one unit to another. (Meters, Yards, Feet, Miles, Inches, Nautical Miles)
    
    Parameters
    ----------
    length : float
        The length to convert.
    from_unit : str
        The unit to convert from.
    to_unit : str
        The unit to convert to.
        
    Returns
    -------
    float
        The converted length.
    """
    
    if from_unit == "Meters":
        if to_unit == "Yards":
            converted_length = length * 1.09361
        elif to_unit == "Feet":
            converted_length = length * 3.28084
        elif to_unit == "Miles":
            converted_length = length * 0.000621371
        elif to_unit == "Inches":
            converted_length = length * 39.3701
        elif to_unit == "Nautical Miles":
            converted_length = length * 0.000539957
        else:
            converted_length = length
    elif from_unit == "Yards":
        if to_unit == "Meters":
            converted_length = length * 0.9144
        elif to_unit == "Feet":
            converted_length = length * 3
        elif to_unit == "Miles":
            converted_length = length * 0.000568182
        elif to_unit == "Inches":
            converted_length = length * 36
        elif to_unit == "Nautical Miles":
            converted_length = length * 0.000493737
        else:
            converted_length = length
    elif from_unit == "Feet":
        if to_unit == "Meters":
            converted_length = length * 0.3048
        elif to_unit == "Yards":
            converted_length = length * 0.333333
        elif to_unit == "Miles":
            converted_length = length * 0.000189394
        elif to_unit == "Inches":
            converted_length = length * 12
        elif to_unit == "Nautical Miles":
            converted_length = length * 0.000164579
        else:
            converted_length = length
    elif from_unit == "Miles":
        if to_unit == "Meters":
            converted_length = length * 1609.34
        elif to_unit == "Yards":
            converted_length = length * 1760
        elif to_unit == "Feet":
            converted_length = length * 5280
        elif to_unit == "Inches":
            converted_length = length * 63360
        elif to_unit == "Nautical Miles":
            converted_length = length * 0.868976
        else:
            converted_length = length
    elif from_unit == "Inches":
        if to_unit == "Meters":
            converted_length = length * 0.0254
        elif to_unit == "Yards":
            converted_length = length * 0.0277778
        elif to_unit == "Feet":
            converted_length = length * 0.0833333
        elif to_unit == "Miles":
            converted_length = length * 0.0000157828
        elif to_unit == "Nautical Miles":
            converted_length = length * 0.0000137149
        else:
            converted_length = length
    else:
        if to_unit == "Meters":
            converted_length = length * 1852
        elif to_unit == "Yards":
            converted_length = length * 2025.37
        elif to_unit == "Feet":
            converted_length = length * 6076.12
        elif to_unit == "Miles":
            converted_length = length * 1.15078
        elif to_unit == "Inches":
            converted_length = length * 72913.4
        else:
            converted_length = length
            
    return converted_length