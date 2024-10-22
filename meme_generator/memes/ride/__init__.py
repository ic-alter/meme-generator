from typing import List
from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from pil_utils import BuildImage
from meme_generator.utils import save_gif 

img_dir = Path(__file__).parent / "images"

def ride(images: List[BuildImage], texts, args):
    self_loc = (175, 9)  # 自己头像的坐标
    user_loc = (60, 115)  # 用户头像的坐标

    # 处理头像：调整大小并转换成圆形
    self_head = images[0].convert("RGBA").resize((122, 122), keep_ratio=True).circle()

    # 将用户头像旋转 13 度
    user_head = images[1].convert("RGBA").resize((122, 122), keep_ratio=True).circle().rotate(13)

    # 创建帧
    frames: List[BuildImage] = []
    for i in range(3):
        # 加载背景图
        frame = BuildImage.open(img_dir / f"{i}.png")  # 使用多张图片
        frame.paste(user_head, user_loc, alpha=True)  # 添加用户头像
        frame.paste(self_head, self_loc, alpha=True)  # 添加自己头像
        frames.append(frame)

    # 直接返回保存为 GIF 格式的结果
    return save_gif([frame.image for frame in frames], duration=0.05)

add_meme(
    "ride",
    ride,
    min_images=2,
    max_images=2, 
    keywords=["骑"],
    date_created=datetime(2024, 10, 3),
    date_modified=datetime(2024, 10, 3),
)