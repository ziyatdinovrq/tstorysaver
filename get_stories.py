#!/usr/bin/python3.8

from pyrogram import Client, filters

api_id = "xxx"
api_hash = "xx"
bot_token = "xxx"
app = Client("my_account", api_id=api_id, api_hash=api_hash)
#app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
channel_id = input('Input channel ID (where need to get story): ')
target_chid = input('Input channel ID (target): ')

app.start()
             # send to me from bot story
for story in app.get_peer_stories(channel_id):
    print(story)
    if str(story.media) == "MessageMediaType.PHOTO":
        app.download_media(story.photo.file_id)
        app.send_photo(target_chid, app.download_media(story.photo.file_id))
    elif str(story.media) == "MessageMediaType.VIDEO":
        app.download_media(story.video.file_id)
        app.send_video(target_chid, app.download_media(story.video.file_id))

app.stop()
