def convert_energy(
    energy: float,
    from_unit: str,
    to_unit: str,
) -> float:
    """
    Converts energy from one unit to another. (Joules, Calories, Foot-Pound, Electronvolts)
    
    Parameters
    ----------
    energy : float
        The energy to convert.
    from_unit : str
        The unit to convert from.
    to_unit : str
        The unit to convert to.
        
    Returns
    -------
    float
        The converted energy.
    """
    
    if from_unit == "Joules":
        if to_unit == "Calories":
            converted_energy = energy * 0.239006
        elif to_unit == "Foot-Pound":
            converted_energy = energy * 0.737562
        elif to_unit == "Electronvolts":
            converted_energy = energy * 6.2415e+18
        else:
            converted_energy = energy
    elif from_unit == "Calories":
        if to_unit == "Joules":
            converted_energy = energy * 4.184
        elif to_unit == "Foot-Pound":
            converted_energy = energy * 3.08596
        elif to_unit == "Electronvolts":
            converted_energy = energy * 2.6132e+19
        else:
            converted_energy = energy
    elif from_unit == "Foot-Pound":
        if to_unit == "Joules":
            converted_energy = energy * 1.35582
        elif to_unit == "Calories":
            converted_energy = energy * 0.324048
        elif to_unit == "Electronvolts":
            converted_energy = energy * 8.462e+18
        else:
            converted_energy = energy
    else:
        if to_unit == "Joules":
            converted_energy = energy * 1.6022e-19
        elif to_unit == "Calories":
            converted_energy = energy * 3.8293e-20
        elif to_unit == "Foot-Pound":
            converted_energy = energy * 1.1817e-19
        else:
            converted_energy = energy
    
    return converted_energy