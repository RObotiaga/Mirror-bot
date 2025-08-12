# --- ОБЯЗАТЕЛЬНЫЕ ПЕРЕМЕННЫЕ ---
BOT_TOKEN = "8404032653:AAEXaI0axTbNLTQPWWCdzuUMd3gtZF4BnTw"
OWNER_ID = 936853523
TELEGRAM_API = 26255081
TELEGRAM_HASH = "6c19a3de08b8e26fe524a81537c2d1d0"

# --- СЕССИЯ ПОЛЬЗОВАТЕЛЯ (КРИТИЧЕСКИ ВАЖНО) ---
USER_SESSION_STRING = "AgGQnukAMW7kfmUhvr5VuC1c4qNrtbdtQa4tv68HSa3U0vrJN9A-HlLL8KvS0eUtXf0ebH9gOe7r4vxSqwhHJZUcPJtT3Nu5aJWVg_eAwocxwDm1kdjN0FFLHdIvdpyh5w8n6y82-HcicJI6rGciHlnUgWhI4pzuWzmaBsC3Btm4UfSKeAZBav3iDLfZtxzE4kFGeStx50wy0gq25Pd43MSXUEhA_rS93xtyV0Fu39zT2xR9L1FXYMMdEJ3xCTgoRSwmVQh85CcUzv-yASstSxeuZtI5Ncbd0DsqN0S-dUCRdwaf44fGmWOEoWQMTi4lQ59Y5bYofQNI-JAxrsO_6zsL1G_ShAAAAAHYCyvDAA"

# --- БАЗА ДАННЫХ (ОЧЕНЬ РЕКОМЕНДУЕТСЯ) ---
# Настоятельно рекомендую создать бесплатную базу на mongodb.com и вставить сюда строку подключения,
# иначе бот будет терять все пользовательские настройки и задачи после каждого перезапуска.
DATABASE_URL = ""

# --- НАСТРОЙКИ ЗАГРУЗКИ В TELEGRAM (LEECH) ---
LEECH_SPLIT_SIZE = 2097152000
AS_DOCUMENT = False
MEDIA_GROUP = True
HYBRID_LEECH = True
LEECH_DUMP_CHAT = "pm"

# --- НАСТРОЙКИ ЗАГРУЗЧИКОВ ---
TORRENT_TIMEOUT = 30
BASE_URL = "http://ladiesman217.com"
BASE_URL_PORT = 80 # Стандартный порт для HTTP. Убедитесь, что он открыт на вашем сервере.

# --- НАСТРОЙКИ ОЧЕРЕДИ ---
QUEUE_DOWNLOAD = 5
QUEUE_ALL = 0 # Оставлено 0, так как не было указано. Рекомендуется установить значение >= QUEUE_DOWNLOAD.
QUEUE_UPLOAD = 0

# --- ОСТАЛЬНЫЕ НЕОБЯЗАТЕЛЬНЫЕ ПЕРЕМЕННЫЕ ---
TG_PROXY = {}
CMD_SUFFIX = ""
AUTHORIZED_CHATS = ""
SUDO_USERS = ""
STATUS_LIMIT = 4
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 15
FILELION_API = ""
STREAMWISH_API = ""
EXCLUDED_EXTENSIONS = ""
INCOMPLETE_TASK_NOTIFIER = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SUBSTITUTE = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}
# GDrive Tools
GDRIVE_ID = ""
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""
# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""
# JDownloader
JD_EMAIL = ""
JD_PASS = ""
# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    }
]
# Nzb search
HYDRA_IP = ""
HYDRA_API_KEY = ""
# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "master"
# Leech
EQUAL_SPLITS = False
USER_TRANSMISSION = False
LEECH_FILENAME_PREFIX = ""
THUMBNAIL_LAYOUT = ""
# qBittorrent/Aria2c
WEB_PINCODE = False
# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0
# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]
# ПРИМЕЧАНИЕ: Переменная TZ (часовой пояс) обычно устанавливается как переменная окружения,
# например, в файле stack.env или docker-compose.yml, а не в этом файле.
# Пример для stack.env:
# TZ=Europe/Moscow