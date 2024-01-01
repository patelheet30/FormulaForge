import os

import arc
import hikari
import miru


class MyModal(miru.Modal[miru.GW]):
    formula = miru.TextInput[miru.GW](
        label="Formula",
        placeholder="Remember to add $ in Math Mode https://www1.cmc.edu/pages/faculty/aaksoy/latex/latexthree.html",
        required=True,
        style=hikari.TextInputStyle.PARAGRAPH,
    )

    async def callback(self, context: miru.ModalContext[miru.GW]) -> None:
        await context.respond("Processing...")


TOKEN = os.environ["TOKEN"]

bot = hikari.GatewayBot(token=TOKEN, logs="DEBUG")
modal_client = miru.GatewayClient(bot)
client = arc.GatewayClient(bot)


@client.include
@arc.slash_command(name="ping", description="Ping the bot.")
async def ping_slash(ctx: arc.GatewayContext) -> None:
    await ctx.respond("Pong!")


client.load_extensions_from("./FormulaForge/Extensions")
