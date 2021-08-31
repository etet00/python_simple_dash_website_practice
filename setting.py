import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
DB_USERNAME = os.getenv("DB_USERNAME")  # 通常固定不變之參數以全大寫命名
DB_PASSWORD = os.getenv("DB_PASSWORD")
