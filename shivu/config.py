class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1886390680"
    sudo_users = "1886390680"
    GROUP_ID = -1002133191051
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://tanjiro1564:tanjiro1564@cluster0.pp5yz4e.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "makimagrabberXrobot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = "25064357"
    api_hash = "cda9f1b3f9da4c0c93d1f5c23ccb19e2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
