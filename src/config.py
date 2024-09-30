from dotenv import load_dotenv
import os


load_dotenv(".env_dev")

DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

TEST_DATABASE = os.getenv("TEST_DATABASE")
TEST_USER = os.getenv("TEST_USER")
TEST_HOST = os.getenv("TEST_HOST")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
TEST_PORT = os.getenv("TEST_PORT")
