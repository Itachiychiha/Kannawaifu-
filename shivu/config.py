class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6662904064"
    sudo_users = "6402009857", "6662904064"
    GROUP_ID = -1002078556251
    TOKEN = "6826276106:AAHdXZH2StDYxgzBV2Bk6galkD6Ba96JinY"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "rising_stars2"
    UPDATE_CHAT = "database2002"
    BOT_USERNAME = "siesta217_bot"
    CHARA_CHANNEL_ID = "-1002143589279"
    api_id = 24658337
    api_hash = "bf99242dbb7f3501f28d39f0a0383cbf"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
