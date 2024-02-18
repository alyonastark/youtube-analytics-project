import os
from googleapiclient.discovery import build

class Video:

    api_key = os.getenv('YOU_TUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        """Экземпляр инициализируется id канала"""
        self.video_id = video_id
        self.video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()


    def __str__(self):
        return self.video_title

    @property
    def video_title(self):
        """Геттер для получения названия видео"""
        try:
            return self.video['items'][0]['snippet']['title']
        except IndexError:
            return None
    @property
    def video_view_count(self):
        """Геттер для получения количества просмотров видео"""
        try:
            return self.video['items'][0]['statistics']['viewCount']
        except IndexError:
            return None

    @property
    def video_like_count(self):
        """Геттер для получения количества лайков видео"""
        try:
            return self.video['items'][0]['statistics']['likeCount']
        except IndexError:
            return None

    @property
    def video_url(self):
        """Геттер для получения url видео"""
        try:
            video_url = f"https://www.youtube.com/watch?v={self.video['items'][0]['id']}"
            return self.video_url
        except IndexError:
            return None


class PLVideo:

    api_key = os.getenv('YOU_TUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id, playlist_id):
        """Экземпляр инициализируется id канала и плейлиста"""
        self.video_id = video_id
        self.playlist_id = playlist_id
        self.video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()

    def __str__(self):
        return self.video_title

    @property
    def video_title(self):
        """Геттер для получения названия видео"""
        return self.video['items'][0]['snippet']['title']

    @property
    def video_url(self):
        """Геттер для получения url видео"""
        video_url = f"https://www.youtube.com/watch?v={self.video['items'][0]['id']}"
        return self.video_url

    @property
    def video_view_count(self):
        """Геттер для получения количества просмотров видео"""
        return self.video['items'][0]['statistics']['viewCount']

    @property
    def video_like_count(self):
        """Геттер для получения количества лайков видео"""
        return self.video['items'][0]['statistics']['likeCount']


