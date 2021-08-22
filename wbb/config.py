if not __name__.endswith("config"):
    import sys
    print("ogei"
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)
    
class Config(object):
    LOGGER = True
    get_int_key = ""
    get_str_key = ""
    OWNER_ID = "1917528355" 
    OWNER_USERNAME = "kaykay"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database module
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
