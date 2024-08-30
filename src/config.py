from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
