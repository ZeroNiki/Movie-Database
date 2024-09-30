from dotenv import load_dotenv
import os


load_dotenv(".env_dev")

DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
