import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YOU_TUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(channel)

    @property
    def title(self):
        """Геттер для получения названия канала"""
        return self.channel['items'][0]['snippet']['title']

    @property
    def channel_id(self):
        """Геттер для получения id канала"""
        return self.channel['items'][0]['id']

    @property
    def channel_description(self):
        """Геттер для получения описания канала"""
        return self.channel['items'][0]['snippet']['description']

    @property
    def url(self):
        """Геттер для получения url канала"""
        return self.channel['items'][0]['snippet']['thumbnails']['default']['url']

    @property
    def subscriber_count(self):
        """Геттер для получения количества подписчиков канала"""
        return self.channel['items'][0]['statistics']['subscriberCount']

    @property
    def video_count(self):
        """Геттер для получения количества видео на канале"""
        return self.channel['items'][0]['statistics']['videoCount']

    @property
    def view_count(self):
        """Геттер для получения количества просмотров канала"""
        return self.channel['items'][0]['statistics']['viewCount']

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с Youtube API"""
        return cls.youtube

    def to_json(self, file_name='moscowpython.json'):
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.channel, file)










