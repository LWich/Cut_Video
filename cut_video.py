import os

from ffmpeg_builder import FFMpegBuilder
from get_video_urls import get_video_urls
from parse_video_id import parse_video_id

def cut_video(url: str, **kwargs) -> str | None:
    """
    Сuts the video and saves it to a file

    Args:
        url (str): URL of YouTube video

    Returns:
        str | None: returns err or None
    """
    video_id = parse_video_id(url)
    
    try:
        urls = get_video_urls(url)

        builder = FFMpegBuilder()\
            .add_loglevel('error')\
            .add_hide_banner()

        time_off = kwargs.get('time_off')
        duration = kwargs.get('duration')
        codec = kwargs.get('codec')

        for url in urls:
            if time_off is not None:
                builder.add_time_off(time_off)
            builder.add_source(url)
        
        if duration is not None:
            builder.add_duration(duration)
        
        if codec is not None:
            builder.add_codec(codec)

        format = kwargs.get('format') or 'mkv'
        path_prefix = kwargs.get('path_prefix') or '.'

        if not os.path.exists(path_prefix):
            os.mkdir(path_prefix)

        file_path = f'{path_prefix}/{video_id}.{format}'

        if os.path.exists(file_path):
            os.remove(file_path)
        
        p = builder.build(filename=file_path)

        _, err = p.communicate()

        if len(err):
            return err.decode('utf-8')
    except ValueError as err:
        return err.__str__()
    
    return None