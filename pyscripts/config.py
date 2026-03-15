import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw")

# Ensure directories exist
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# Database Configuration
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

# Kaggle Dataset
DATASET_NAME = os.getenv("KAGGLE_DATASET")

# SQLAlchemy Connection String
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"