from googleapiclient.discovery import build
import os
import isodate
import datetime


class PlayList:

    api_key = os.getenv('YOU_TUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        """Экземпляр инициализируется id плейлиста"""
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(id=self.playlist_id,
                                                            part='snippet',
                                                            ).execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails',
                                               maxResults=50,
                                               ).execute()
        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()

    @property
    def title(self):
        """Геттер для получения названия плейлиста"""
        return self.playlist['items'][0]['snippet']['title']

    @property
    def url(self):
        """Геттер для получения ссылки на плейлист"""
        return f'https://www.youtube.com/playlist?list={self.playlist_id}'

    @property
    def total_duration(self):
        """Возвращает объект класса datetime.timedelta с общей длительностью плейлиста"""
        total_duration = datetime.timedelta(0)
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео"""
        like_count = 0
        best_video = []
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > like_count:
                like_count = int(video['statistics']['likeCount'])
                best_video = video
        return f'https://youtu.be/{best_video['id']}'


