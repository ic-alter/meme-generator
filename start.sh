docker run -d \
  --name=meme-generator \
  -p 2233:2233 \
  --restart always \
  -v /home/ubuntu/byy/bot/meme-generator/meme_generator:/app/meme_generator \
  -v /home/ubuntu/byy/bot/meme-generator/meme-generator-contrib:/data \
  -v /home/ubuntu/byy/bot/meme-generator/meme_emoji:/meme_emoji \
  -e MEME_DIRS='["/data/memes","/meme_emoji/aircraft_cup","/meme_emoji/emoji"]' \
  -e MEME_DISABLED_LIST='[]' \
  -e GIF_MAX_SIZE=10.0 \
  -e GIF_MAX_FRAMES=100 \
  -e BAIDU_TRANS_APPID='20250328002317685' \
  -e BAIDU_TRANS_APIKEY='hu_ZbpCDuTtvwRh3OwWb' \
  -e LOG_LEVEL='INFO' \
  meetwq/meme-generator:main


  # 添加新表情包后，需要移除原来的镜像