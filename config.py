import os

from dotenv import load_dotenv


load_dotenv()

DEFAULT_PATH = os.getenv('DEFAULT_PATH')
NEW = os.getenv('NEW')
ORIGINAL = os.getenv('ORIGINAL')
