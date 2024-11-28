from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = [int(admin) for admin in env.list("ADMINS")]
CHANNEL_IDS = env.str("CHANNEL_IDS")
IP = env.str("ip")  # Xosting ip manzili
