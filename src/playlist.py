from src.video import PLVideo


class PlayList():
    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id
        self.url = 'https://www.youtube.com/playlist?list=' + self.playlist_id


