from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv


@dataclass
class DatabaseConfig:
    database: str         
    db_host: str         
    db_user: str        
    db_password: str   


@dataclass
class TgBot:
    token: str           


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config() -> Config:
    load_dotenv()

    return Config(
        tg_bot=TgBot(
            token=getenv('BOT_TOKEN'),
        ),
        db=DatabaseConfig(
            database=getenv('DATABASE'),
            db_host=getenv('DB_HOST'),
            db_user=getenv('DB_USER'),
            db_password=getenv('DB_PASSWORD')
        )
    )
