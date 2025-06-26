import math
from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import (
    Maker,
    make_gif_or_combined_gif,
)

img_dir = Path(__file__).parent / "images"


def flick(images: list[BuildImage], texts, args):
    def maker(i: int) -> Maker:
        def make(imgs: list[BuildImage]):
            img = imgs[0].convert("RGBA").square().resize((240, 240))

            if i < 3:
                return img
            elif i < 12:
                hand = BuildImage.open(img_dir / f"{i - 3}.png")
                return img.paste(hand, (0, 0), alpha=True)
            else:
                # 模拟“抖动”而非真实的 shader 扭曲
                width, height = img.size
                amplitude = width / 12.0
                omega = 2.0 * math.pi / 5.0
                decay = 0.1
                t = i - 3
                damping = math.exp(-decay * t)
                offset = int(amplitude * math.sin(omega * t) * damping)
                angle = 5 * math.sin(omega * t) * damping  # 旋转角度（近似）

                rotated = img.rotate(angle, resample=2, expand=False)
                frame = BuildImage.new("RGBA", img.size, (255, 255, 255, 0))
                frame.paste(rotated, (offset, 0), alpha=True)
                if i == 12:
                    hand = BuildImage.open(img_dir / f"{i - 3}.png")
                    frame.paste(hand, (0, 0), alpha=True)
                return frame

        return make

    return make_gif_or_combined_gif(images, maker, 30, 0.05)


add_meme(
    "flick",
    flick,
    min_images=1,
    max_images=1,
    keywords=["弹", "脑瓜崩"],
    date_created=datetime(2025, 6, 22),
    date_modified=datetime(2025, 6, 26),
)