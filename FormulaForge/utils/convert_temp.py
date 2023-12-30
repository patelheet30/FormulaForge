def convert_temperature(
    temperature: float,
    from_unit: str,
    to_unit: str,
) -> float:
    """
    Converts temperature from one unit to another. (Celsius, Fahrenheit, Kelvin)
    
    Parameters
    ----------
    temperature : float
        The temperature to convert.
    from_unit : str
        The unit to convert from.
    to_unit : str
        The unit to convert to.
        
    Returns
    -------
    float
        The converted temperature.
    """
    
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            converted_temperature = (temperature * 9/5) + 32
        elif to_unit == "Kelvin":
            converted_temperature = temperature + 273.15
        else:
            converted_temperature = temperature
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            converted_temperature = (temperature - 32) * 5/9
        elif to_unit == "Kelvin":
            converted_temperature = (temperature - 32) * 5/9 + 273.15
        else:
            converted_temperature = temperature
    else:
        if to_unit == "Celsius":
            converted_temperature = temperature - 273.15
        elif to_unit == "Fahrenheit":
            converted_temperature = (temperature - 273.15) * 9/5 + 32
        else:
            converted_temperature = temperature
    
    return converted_temperature