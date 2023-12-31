def convert_speed(
    speed: float,
    from_unit: str,
    to_unit: str,
) -> float:
    """
    Converts speed from one unit to another. (Kilometers per hour, Miles per hour, Meters per second, Knots)

    Parameters
    ----------
    speed : float
        The speed to convert.
    from_unit : str
        The unit to convert from.
    to_unit : str
        The unit to convert to.

    Returns
    -------
    float
        The converted speed.
    """

    if from_unit == "Kilometers per hour":
        if to_unit == "Miles per hour":
            converted_speed = speed * 0.621371
        elif to_unit == "Meters per second":
            converted_speed = speed * 0.277778
        elif to_unit == "Knots":
            converted_speed = speed * 0.539957
        else:
            converted_speed = speed
    elif from_unit == "Miles per hour":
        if to_unit == "Kilometers per hour":
            converted_speed = speed * 1.60934
        elif to_unit == "Meters per second":
            converted_speed = speed * 0.44704
        elif to_unit == "Knots":
            converted_speed = speed * 0.868976
        else:
            converted_speed = speed
    elif from_unit == "Meters per second":
        if to_unit == "Kilometers per hour":
            converted_speed = speed * 3.6
        elif to_unit == "Miles per hour":
            converted_speed = speed * 2.23694
        elif to_unit == "Knots":
            converted_speed = speed * 1.94384
        else:
            converted_speed = speed
    else:
        if to_unit == "Kilometers per hour":
            converted_speed = speed * 1.852
        elif to_unit == "Miles per hour":
            converted_speed = speed * 1.15078
        elif to_unit == "Meters per second":
            converted_speed = speed * 0.514444
        else:
            converted_speed = speed

    return converted_speed
