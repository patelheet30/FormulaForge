import arc
import base64
import aiohttp


from FormulaForge.bot import MyModal
from FormulaForge.bot import modal_client
from FormulaForge.Models.url import URLBuilder, convert_new_line_to_url_encoding


latex_images = arc.GatewayPlugin("latex_images")


@latex_images.include
@arc.slash_command(
    name="latex_to_image", description="Convert LaTeX (Math Mode) to an image."
)
async def latex_to_image(
    ctx: arc.GatewayContext,
    is_transparent: arc.Option[
        bool,
        arc.BoolParams(
            name="transparent",
            description="Whether the background of the formula image will be transparent or not.",
        ),
    ],
    rect_or_square: arc.Option[
        str,
        arc.StrParams(
            name="rect_or_square",
            description="Whether the formula image will be a rectangle or a square.",
            choices=["Rectangle", "Square"],
        ),
    ],
    bg_color: arc.Option[
        str | None,
        arc.StrParams(
            name="bg_color",
            description="The background color of the formula image. Defaults to gray",
            choices=["White", "Black", "Red", "Gray", "Blue"],
        ),
    ] = "Gray",
    text_color: arc.Option[
        str | None,
        arc.StrParams(
            name="text_color",
            description="The text color of the formula image. Defaults to white",
            choices=["White", "Black", "Red", "Gray", "Blue"],
        ),
    ] = "White",
    fontsize: arc.Option[
        int | None,
        arc.IntParams(
            name="fontsize",
            description="The fontsize of the formula image. Defaults to 16px",
            choices={
                "8px": 8,
                "12px": 12,
                "16px": 16,
                "20px": 20,
                "24px": 24,
                "28px": 28,
                "32px": 32,
            },
        ),
    ] = 16,
) -> None:
    if is_transparent:
        is_transparent = True
    else:
        is_transparent = False
    rect_or_square = rect_or_square
    bg_color = bg_color
    text_color = text_color
    font_size = fontsize

    modal = MyModal(title="FormulaForge")
    builder = modal.build_response(modal_client)
    await ctx.respond_with_builder(builder)
    modal_client.start_modal(modal)

    await modal.wait()

    if modal.last_context is None:
        return

    formula = convert_new_line_to_url_encoding(modal.formula.value)  # type: ignore

    paramless_url = URLBuilder(f"http://0.0.0.0:80/latex_formula/{formula}")
    final_url = paramless_url(
        transparent=is_transparent,
        rect_or_square=rect_or_square,
        background_color=bg_color,
        text_color=text_color,
        font_size=font_size,
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url=final_url) as resp:
            response = await resp.json()

    image_bytes = base64.b64decode(response["image"])

    await modal.last_context.edit_response(content=None, attachment=image_bytes)


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(latex_images)


@arc.unloader
def unload(client: arc.GatewayClient) -> None:
    client.remove_plugin(latex_images)
