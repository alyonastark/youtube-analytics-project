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

    def __str__(self):
        """Возвращает название и адрес канала"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Складывает количество подписчиков каналов"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """Метод для вычитания, показывает разницу между количеством подписчиков"""
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        """Метод для сравнения, возвращает True, если количество подписчиков первого канала больше чем у другого"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """Метод для сравнения, возвращает True, если количество подписчиков первого канала больше или равно другому"""
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        """Метод для сравнения, возвращает True, если количество подписчиков первого канала меньше чем у другого"""
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """Метод для сравнения, возвращает True, если количество подписчиков первого канала меньше или равно другому"""
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        """Метод для сравнения, возвращает True, если количество подписчиков у двух канало одинаковое"""
        return self.subscriber_count == other.subscriber_count

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
        channel_url = f"https://www.youtube.com/channel/{self.channel['items'][0]['id']}"
        return channel_url

    @property
    def subscriber_count(self):
        """Геттер для получения количества подписчиков канала"""
        return int(self.channel['items'][0]['statistics']['subscriberCount'])

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










