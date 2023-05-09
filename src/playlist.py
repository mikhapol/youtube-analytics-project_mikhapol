import datetime, isodate

from googleapiclient.discovery import build
from src.video import api_key


class PlayList:
    """
    Класс PlayList, который инициализируется id плейлиста и имеет следующие публичные атрибуты:
       # название плейлиста
       # ссылку на плейлист
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id
        playlists = self.youtube.playlists().list(id=self.playlist_id,
                                                  part='contentDetails,snippet',
                                                  maxResults=50,
                                                  ).execute()
        self.title = playlists["items"][0]["snippet"]["title"]

    @property
    def total_duration(self):
        """
        Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста
        (обращение как к свойству, использовать @property)
        """
        # получить данные по видеороликам в плейлисте
        playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails',
                                                            maxResults=50).execute()
        # получить все id видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)).execute()

        # вывести длительности видеороликов из плейлиста
        total_duration = datetime.timedelta()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """
        Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков).
        """
        # переменная со словарём, в котором сравнивается наиболшее количество лайков и присваивается url
        best_video = {
            "like_count": 0,
            "url": ""
                      }
        plist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails',
                                                         maxResults=50).execute()
        # цикл поиска наибольшего количества лайков
        for video in plist_videos["items"]:

            video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                        id=video["contentDetails"]["videoId"]).execute()
            # сравнивание количества лайков и добавление в нулевой элемент словаря
            if best_video["like_count"] < int(video_response["items"][0]["statistics"]["likeCount"]):
                best_video["url"] = 'https://youtu.be/' + video_response["items"][0]["id"]
                best_video["like_count"] = int(video_response["items"][0]["statistics"]["likeCount"])
        return best_video["url"]
