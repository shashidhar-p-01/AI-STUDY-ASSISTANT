from pathlib import Path 
import os 
from dotenv import load_dotenv

load_dotenv() # loads variables from .env

PROJECT_ROOT = Path(__file__).resolve().parent.parent # Project root directory

#application settings 
APP_NAME = os.getenv("APP_NAME" , "AI STUDY ASSISTANT")
DATABASE_PATH = os.getenv("DATABASE_PATH" , "data/database/study.db")
DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER" , "ollama")
LOG_LEVEL = os.getenv("LOG_LEVEL" , "INFO")
