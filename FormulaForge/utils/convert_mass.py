def convert_mass(
    mass: float,
    from_unit: str,
    to_unit: str,
) -> float:
    """
    Converts mass from one unit to another. (Kilograms, Grams, Pounds, Ounces)
    
    Parameters
    ----------
    mass : float
        The mass to convert.
    from_unit : str
        The unit to convert from.
    to_unit : str
        The unit to convert to.
        
    Returns
    -------
    float
        The converted mass.
    """
    
    if from_unit == "Kilograms":
        if to_unit == "Grams":
            converted_mass = mass * 1000
        elif to_unit == "Pounds":
            converted_mass = mass * 2.20462
        elif to_unit == "Ounces":
            converted_mass = mass * 35.274
        else:
            converted_mass = mass
    elif from_unit == "Grams":
        if to_unit == "Kilograms":
            converted_mass = mass / 1000
        elif to_unit == "Pounds":
            converted_mass = mass / 453.592
        elif to_unit == "Ounces":
            converted_mass = mass / 28.3495
        else:
            converted_mass = mass
    elif from_unit == "Pounds":
        if to_unit == "Kilograms":
            converted_mass = mass / 2.20462
        elif to_unit == "Grams":
            converted_mass = mass * 453.592
        elif to_unit == "Ounces":
            converted_mass = mass * 16
        else:
            converted_mass = mass
    else:
        if to_unit == "Kilograms":
            converted_mass = mass / 35.274
        elif to_unit == "Grams":
            converted_mass = mass * 28.3495
        elif to_unit == "Pounds":
            converted_mass = mass / 16
        else:
            converted_mass = mass
    
    return converted_mass
