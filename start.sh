docker run -d \
  --name=meme-generator \
  -p 2233:2233 \
  --restart always \
  -v /home/ubuntu/byy/bot/meme-generator/meme_generator:/app/meme_generator \
  -v /home/ubuntu/byy/bot/meme-generator/meme-generator-contrib:/data \
  -v /home/ubuntu/byy/bot/meme-generator/meme_emoji:/meme_emoji \
  -v /home/ubuntu/byy/bot/meme-generator/meme_emoji_nsfw:/meme_emoji_nsfw \
  -v /home/ubuntu/byy/bot/meme-generator/meme-generator-jj:/meme-generator-jj \
  -v /home/ubuntu/byy/bot/meme-generator/tudou-meme:/tudou-meme \
  -e MEME_DIRS='["/data/memes","/meme_emoji/emoji","/meme-generator-jj/memes","/meme_emoji_nsfw/emoji","/tudou-meme/memes"]' \
  -e MEME_DISABLED_LIST='[]' \
  -e GIF_MAX_SIZE=10.0 \
  -e GIF_MAX_FRAMES=100 \
  -e BAIDU_TRANS_APPID='20250328002317685' \
  -e BAIDU_TRANS_APIKEY='hu_ZbpCDuTtvwRh3OwWb' \
  -e LOG_LEVEL='INFO' \
  ghcr.io/memecrafters/meme-generator:0.1.14


  # 添加新表情包后，需要移除原来的容器
  # 原来的镜像是  meetwq/meme-generator:main