import base64
import io

import matplotlib
import matplotlib.pyplot as plt
from fastapi import FastAPI

matplotlib.rcParams["mathtext.fontset"] = "cm"

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/latex_formula/{formula}")
async def generate_latex_formula(
    formula: str,
    transparent: bool = False,
    rect_or_square: str = "square",
    background_color: str = "gray",
    text_color: str = "white",
    font_size: int = 16,
):
    if rect_or_square.lower() == "rectangle":
        fig = plt.figure(dpi=300, facecolor=background_color, figsize=(4, 1))
    else:
        fig = plt.figure(
            dpi=300,
            facecolor=background_color,
        )

    multiline_formula = r"""{}""".format(formula)
    fig.text(
        x=0.5,
        y=0.5,
        s=f"""{multiline_formula}""",
        fontsize=font_size,
        horizontalalignment="center",
        verticalalignment="center",
        color=text_color,
    )

    image_bytes = io.BytesIO()
    plt.savefig(image_bytes, format="png", transparent=transparent)
    plt.close()

    image_bytes64 = base64.b64encode(image_bytes.getvalue()).decode("utf-8")

    return {"image": image_bytes64, "formula": formula}
