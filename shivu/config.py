class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = 1886390680
    OWNER_USERNAME = "jinwoo_sung4"
    sudo_users = ""
    GROUP_ID = -1002216206408
    TOKEN = "7505230606:"
    mongo_url = "mongodb+srv://:@cluster0."
    PHOTO_URL = ["https://telegra.ph/file/9d64f0c5a9c2cccbd71db.jpg"]
    SUPPORT_CHAT = "eldian_network"
    UPDATE_CHAT = "eldian_network"
    BOT_USERNAME = "makimagrabberbot"
    CHARA_CHANNEL_ID = "-1002208868825"
    api_id = ""
    api_hash = ""

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
