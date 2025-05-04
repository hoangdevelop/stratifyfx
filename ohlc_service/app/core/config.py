from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    TWELVE_API_KEY = os.getenv("TWELVE_API_KEY")
    FASTFOREX_API_KEY = os.getenv("FASTFOREX_API_KEY")

    @property
    def database_url(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
