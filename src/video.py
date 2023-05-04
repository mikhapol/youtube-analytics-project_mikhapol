from googleapiclient.discovery import build

from src.channel import api_key


class Video:
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id) -> None:
        self.video_id = video_id  # id видео
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id).execute()
        self.title_video = video_response["items"][0]["snippet"]["title"]  # название видео
        self.url_video = 'https://www.youtube.com/watch?v=' + self.video_id  # ссылка на видео
        self.view_count = video_response["items"][0]["statistics"]["viewCount"]  # количество просмотров
        self.like_count = video_response["items"][0]["statistics"]["likeCount"]  # количество лайков
        # print(video_response)

    def __str__(self):
        return self.title_video


class PLVideo(Video):
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id, playlist_id) -> None:
        super().__init__(video_id)  # id видео
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id).execute()
        self.title_video = video_response["items"][0]["snippet"]["title"]  # название видео
        self.url_video = 'https://www.youtube.com/watch?v=' + self.video_id  # ссылка на видео
        self.view_count = video_response["items"][0]["statistics"]["viewCount"]  # количество просмотров
        self.like_count = video_response["items"][0]["statistics"]["likeCount"]  # количество лайков
        # playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50).execute()
        self.playlist_id = playlist_id  # id плейлиста
        self.url_video_pl = 'https://www.youtube.com/watch?v=' + self.video_id + '&list=' + self.playlist_id  # ссылка на видео
