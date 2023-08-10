def parse_video_id(url: str) -> str:
    """
    Parsing the video id from url

    Args:
        url (str): URL of YouTube video

    Returns:
        str: video id or empty string
    """
    id_index = url.find('watch?v=')
    
    return '' if id_index < 0 else url[id_index+8:]