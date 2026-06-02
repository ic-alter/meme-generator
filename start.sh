docker run -d \
  --name=meme-generator \
  -p 2233:2233 \
  --restart always \
  -v /sdb/icalter/bot/meme-generator/meme_generator:/app/meme_generator \
  -v /sdb/icalter/bot/meme-generator/meme-generator-contrib:/data \
  -v /sdb/icalter/bot/meme-generator/meme_emoji:/meme_emoji \
  -v /sdb/icalter/bot/meme-generator/crazy_emoji:/meme_emoji_nsfw \
  -v /sdb/icalter/bot/meme-generator/tudou-meme:/tudou-meme \
  -e MEME_DIRS='["/data/memes","/meme_emoji/emoji","/meme_emoji_nsfw/emoji","/tudou-meme/meme"]' \
  -e MEME_DISABLED_LIST='[]' \
  -e GIF_MAX_SIZE=10.0 \
  -e GIF_MAX_FRAMES=100 \
  -e BAIDU_TRANS_APPID='20250328002317685' \
  -e BAIDU_TRANS_APIKEY='hu_ZbpCDuTtvwRh3OwWb' \
  -e LOG_LEVEL='INFO' \
  ghcr.io/memecrafters/meme-generator:0.1.14


  # 添加新表情包后，需要移除原来的容器
  # 原来的镜像是  meetwq/meme-generator:main
  #-v /sdb/icalter/bot/bot/meme-generator/meme-generator-jj:/meme-generator-jj \