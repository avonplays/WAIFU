class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1886390680"
    OWNER_USERNAME = "sung_jinwo4"
    sudo_users = "1886390680"
    GROUP_ID = -1002043902352
    TOKEN = "7505230606:AAEDisjieqKN4JP1rgwq0ZnXpY2jQ8sVYfU"
    mongo_url = "mongodb+srv://tanjiro1564:tanjiro1564@cluster0.pp5yz4e.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/137a87fdf32461815dd68.jpg", "https://telegra.ph/file/9d64f0c5a9c2cccbd71db.jpg"]
    SUPPORT_CHAT = "SOULS_SOCIETYY"
    UPDATE_CHAT = "SOUL_NETWORKS"
    BOT_USERNAME = "makimagrabberXrobot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = "25064357"
    api_hash = "cda9f1b3f9da4c0c93d1f5c23ccb19e2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
