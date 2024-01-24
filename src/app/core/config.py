from pydantic import Field, BaseSettings


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"

    PROJECT_NAME:str = Field("puzzle-pharse-server")

    OPENAI_API_KEY:str = Field("", env='OPENAI_API_KEY')

    class Config:
        casse_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()

if __name__ == '__main__':
    print(settings)