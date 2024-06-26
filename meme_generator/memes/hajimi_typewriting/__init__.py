import random
from pathlib import Path

from pil_utils import BuildImage
from pydantic import Field

from meme_generator import MemeArgsModel, MemeArgsParser, MemeArgsType, add_meme
from meme_generator.exception import TextOverLength

img_dir = Path(__file__).parent / "images"


def hajimi_typewriting(images, texts: list[str], args):
    text = texts[0]
    total_num = 21
    num = 1

    params = [
        ((1000,200), (359,0), ((18,0), (298,240), (263,284), (0,54)))
    ]
    size, loc, points = params[num - 1]
    frame = BuildImage.open(img_dir / f"{num:02d}.jpg")
    text_img = BuildImage.new("RGBA", size)
    padding = 5
    try:
        text_img.draw_text(
            (padding, padding, size[0] - padding, size[1] - padding),
            text,
            max_fontsize=80,
            min_fontsize=20,
            allow_wrap=True,
            lines_align="center",
            spacing=10,
            #fontname="FZShaoEr-M11S",
            fill="#000000",
        )
    except ValueError:
        raise TextOverLength(text)
    frame.paste(text_img.perspective(points), loc, alpha=True)
    return frame.save_png()


add_meme(
    "hajimi_typewriting",
    hajimi_typewriting,
    min_texts=1,
    max_texts=1,
    default_texts=["我超爱你"],
    keywords=["猫猫打字", "哈基米打字"],
)
