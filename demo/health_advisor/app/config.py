import openai
from .env import OPENAI_API_KEY

class Config:
    openai_key = OPENAI_API_KEY
    
    @staticmethod
    def get_openai_key():
        return Config.openai_key

