from subprocess import Popen, PIPE


def get_video_urls(url: str=None) -> list:
    """
    Generate url for video in google player

    Args:
        url (str, optional): URL of YouTube video. Defaults to None.

    Raises:
        ValueError: URL can`t be None
        ValueError: URL is not a valid

    Returns:
        list: list of urls (video, audio)
    """
    if url is None:
        raise ValueError('URL can`t be None')

    p = Popen(['yt-dlp', '-g', url],
              stdout=PIPE,
              stderr=PIPE)
    
    out_b, err_b = p.communicate(timeout=3)

    if len(err_b):
        raise ValueError('URL is not a valid')

    out = out_b.decode('utf-8')

    return out.split('\n')[:-1] 
