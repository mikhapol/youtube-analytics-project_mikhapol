from googleapiclient.discovery import build

from src.channel import api_key

youtube = build('youtube', 'v3', developerKey=api_key)
# playlist_id = 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
# playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50).execute()
# print(playlist_videos)


# 'https://www.youtube.com/watch?v= O7qf7f2hL2E &list= PLYJ-k_bGDRR0M1wicLSF8z_fRELvMZfxR'

# 'https://www.youtube.com/watch?v= BBotskuyw_M'

# 'https://www.youtube.com/watch?v=' + self.video_id  # ссылка на видео

playlist_id = 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50).execute()
print(playlist_videos)
video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
print(video_ids)
