import sys
from linebot import LineBotApi

import os

try:
    channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'YOUR_SECRET'
except:
    raise Exception("Can't get access token")

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

# Example: https://github.com/line/line-bot-sdk-python#set_rich_menu_imageself-rich_menu_id-content_type-content-timeoutnone
# Document https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image

content_type = 'image/png'  # Just support JPEG or PNG, check your image type

try:
    with open('richmenu/template.png', 'rb') as f:
        line_bot_api.set_rich_menu_image('richmenu-3514661b0c16b00d8fb380b1a9a4c901', content_type, f)
except Exception as e:
    print(e)

print('Set default success.') 
