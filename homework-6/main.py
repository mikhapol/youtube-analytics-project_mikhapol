from src.video import Video

if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.title_video is None
    assert broken_video.like_count is None

    # broken_video_2 = Video('9lO06Zxhu88')
    # print(broken_video_2.title_video)
    # print(broken_video_2.like_count)
    #
    # broken_video_3 = Video('broken_video_id')
    # print(broken_video_3.title_video)
    # print(broken_video_3.like_count)
