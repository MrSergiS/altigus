from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv


load_dotenv()


@dataclass
class DatabaseConfig:
    database: str         
    host: str
    user: str
    password: str
    port: str


@dataclass
class BotConfig:
    token: str


def bot_config() -> BotConfig:
    return BotConfig(token=getenv('BOT_TOKEN'))


def db_config() -> DatabaseConfig:
    return DatabaseConfig(
        database=getenv('POSTGRES_DB'),
        host=getenv('POSTGRES_HOST'),
        user=getenv('POSTGRES_USER'),
        password=getenv('POSTGRES_PASSWORD'),
        port=getenv('POSTGRES_PORT')
    )
