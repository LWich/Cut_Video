from subprocess import Popen, PIPE


class FFMpegBuilder:
    """
    Build FFMpeg execution command
    """

    def __init__(self) -> None:
        self.__commands = ['ffmpeg']
    
    def add_time_off(self, time: str):
        self.__commands.append('-ss')
        self.__commands.append(time)
        return self
    
    def add_duration(self, time: str):
        self.__commands.append('-t')
        self.__commands.append(time)
        return self
    
    def add_source(self, source: str):
        self.__commands.append('-i')
        self.__commands.append(source)
        return self
    
    def add_codec(self, codec: str):
        self.__commands.append('-c')
        self.__commands.append(codec)
        return self
    
    def add_loglevel(self, level: str):
        self.__commands.append('-loglevel')
        self.__commands.append(level)
        return self
    
    def add_hide_banner(self):
        self.__commands.append('-hide_banner')
        return self
    
    def build(self, filename: str) -> Popen:
        self.__commands.append(filename)

        return Popen(self.__commands,
                  stdout=PIPE,
                  stderr=PIPE)

    @property
    def command(self):
        return ' '.join(self.__commands)
