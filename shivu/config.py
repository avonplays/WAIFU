class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = 6289029511
    OWNER_USERNAME = "Yash_747"
    sudo_users = "6289029511"
    GROUP_ID = -1002288846111
    TOKEN = "7667702659:AAHPIU2yQEMrbOu696qO93VaKcg92h6j5DM"
    mongo_url = "mongodb+srv://Avon:Avon@avon.fstai.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/9d64f0c5a9c2cccbd71db.jpg"]
    SUPPORT_CHAT = "eldian_network"
    UPDATE_CHAT = "eldian_network"
    BOT_USERNAME = "Yumiko_x_bot"
    CHARA_CHANNEL_ID = "-1002165537292"
    api_id = "27323120"
    api_hash = "8e82c0f9e36066f84ad663ab11ab0637"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
