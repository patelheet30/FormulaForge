import arc
import hikari

from FormulaForge.utils.convert_energy import convert_energy
from FormulaForge.utils.convert_length import convert_length
from FormulaForge.utils.convert_mass import convert_mass
from FormulaForge.utils.convert_speed import convert_speed
from FormulaForge.utils.convert_temp import convert_temperature


unit_converter = arc.RESTPlugin("unit_converter")

unit_convert_group = unit_converter.include_slash_group(
    "unit_convert",
    "Unit Converter Commands. (Temperature, Speed, Mass, Energy, Length)",
)

dict_of_unit_symbols = {
    "Celsius": "°C",
    "Fahrenheit": "°F",
    "Kelvin": "K",
    "Meters Per Second": "m/s",
    "Kilometers Per Hour": "km/h",
    "Miles Per Hour": "mph",
    "Knots": "kn",
    "Grams": "g",
    "Kilograms": "kg",
    "Pounds": "lb",
    "Ounces": "oz",
    "Joules": "J",
    "Calories": "cal",
    "Foot-Pound": "ft-lb",
    "Electronvolts": "eV",
    "Meters": "m",
    "Miles": "mi",
    "Yards": "yd",
    "Feet": "ft",
    "Inches": "in",
    "Nautical Miles": "nmi",
}


def get_unit_symbol(unit: str) -> str:
    return dict_of_unit_symbols[unit]


def embed_builder(value, from_unit, to_unit, converted_value):
    embed = hikari.Embed(
        title="Unit Conversion",
        description=f"Converted {value}{get_unit_symbol(from_unit)} to {converted_value}{get_unit_symbol(to_unit)}",
        color=0x00FF00,
    )
    return embed


@unit_convert_group.include
@arc.slash_subcommand(name="temperature", description="Convert temperature.")
async def temperature(
    ctx: arc.RESTContext,
    temperature: arc.Option[
        float,
        arc.FloatParams(
            name="temperature",
            description="The temperature to convert.",
        ),
    ],
    from_unit: arc.Option[
        str,
        arc.StrParams(
            name="from_unit",
            description="The unit to convert from.",
            choices=["Celsius", "Fahrenheit", "Kelvin"],
        ),
    ],
    to_unit: arc.Option[
        str,
        arc.StrParams(
            name="to_unit",
            description="The unit to convert to.",
            choices=["Celsius", "Fahrenheit", "Kelvin"],
        ),
    ],
) -> None:
    await ctx.respond(
        embed=embed_builder(
            temperature,
            from_unit,
            to_unit,
            convert_temperature(temperature, from_unit, to_unit),
        )
    )


@unit_convert_group.include
@arc.slash_subcommand(name="speed", description="Convert speed.")
async def speed(
    ctx: arc.RESTContext,
    speed: arc.Option[
        float,
        arc.FloatParams(
            name="speed",
            description="The speed to convert.",
        ),
    ],
    from_unit: arc.Option[
        str,
        arc.StrParams(
            name="from_unit",
            description="The unit to convert from.",
            choices=[
                "Meters Per Second",
                "Kilometers Per Hour",
                "Miles Per Hour",
                "Knots",
            ],
        ),
    ],
    to_unit: arc.Option[
        str,
        arc.StrParams(
            name="to_unit",
            description="The unit to convert to.",
            choices=[
                "Meters Per Second",
                "Kilometers Per Hour",
                "Miles Per Hour",
                "Knots",
            ],
        ),
    ],
) -> None:
    await ctx.respond(
        embed=embed_builder(
            speed, from_unit, to_unit, convert_speed(speed, from_unit, to_unit)
        )
    )


@unit_convert_group.include
@arc.slash_subcommand(name="mass", description="Convert mass.")
async def mass(
    ctx: arc.RESTContext,
    mass: arc.Option[
        float,
        arc.FloatParams(
            name="mass",
            description="The mass to convert.",
        ),
    ],
    from_unit: arc.Option[
        str,
        arc.StrParams(
            name="from_unit",
            description="The unit to convert from.",
            choices=["Grams", "Kilograms", "Pounds", "Ounces"],
        ),
    ],
    to_unit: arc.Option[
        str,
        arc.StrParams(
            name="to_unit",
            description="The unit to convert to.",
            choices=["Grams", "Kilograms", "Pounds", "Ounces"],
        ),
    ],
) -> None:
    await ctx.respond(
        embed=embed_builder(
            mass, from_unit, to_unit, convert_mass(mass, from_unit, to_unit)
        )
    )


@unit_convert_group.include
@arc.slash_subcommand(name="energy", description="Convert energy.")
async def energy(
    ctx: arc.RESTContext,
    energy: arc.Option[
        float,
        arc.FloatParams(
            name="energy",
            description="The energy to convert.",
        ),
    ],
    from_unit: arc.Option[
        str,
        arc.StrParams(
            name="from_unit",
            description="The unit to convert from.",
            choices=["Joules", "Calories", "Foot-Pound", "Electronvolts"],
        ),
    ],
    to_unit: arc.Option[
        str,
        arc.StrParams(
            name="to_unit",
            description="The unit to convert to.",
            choices=["Joules", "Calories", "Foot-Pound", "Electronvolts"],
        ),
    ],
) -> None:
    await ctx.respond(
        embed=embed_builder(
            energy, from_unit, to_unit, convert_energy(energy, from_unit, to_unit)
        )
    )


@unit_convert_group.include
@arc.slash_subcommand(name="length", description="Convert length.")
async def length(
    ctx: arc.RESTContext,
    length: arc.Option[
        float,
        arc.FloatParams(
            name="length",
            description="The length to convert.",
        ),
    ],
    from_unit: arc.Option[
        str,
        arc.StrParams(
            name="from_unit",
            description="The unit to convert from.",
            choices=["Meters", "Miles", "Yards", "Feet", "Inches", "Nautical Miles"],
        ),
    ],
    to_unit: arc.Option[
        str,
        arc.StrParams(
            name="to_unit",
            description="The unit to convert to.",
            choices=["Meters", "Miles", "Yards", "Feet", "Inches", "Nautical Miles"],
        ),
    ],
) -> None:
    await ctx.respond(
        embed=embed_builder(
            length, from_unit, to_unit, convert_length(length, from_unit, to_unit)
        )
    )


@arc.loader
def load(client: arc.RESTClient) -> None:
    client.add_plugin(unit_converter)


@arc.unloader
def unload(client: arc.RESTClient) -> None:
    client.remove_plugin(unit_converter)
