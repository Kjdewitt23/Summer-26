"""
Complete Lab 3 and update the following information:

Author: Kollin DeWitt
Date: 6/30/2026
"""
class YouTubeChannel:
    def __init__(self, name: str ="", video_count: int =0):
        """
        name: the channel title  
        video_count: number of videos uploaded to this channel  
        """
        self._name = name
        self.__video_count = video_count

    def __str__(self) -> str:
        return f"Channel: {self._name}, Videos: {self.__video_count}"
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name) -> None:
        self._name = name

    def get_video_count(self) -> int:
        return self.__video_count
    
    def set_video_count(self, video_count) -> None:
        if video_count >= 0:
            self.__video_count = video_count
    

def main():
    channel = YouTubeChannel("UVUCS1410", 150)
    print(channel.get_name(), channel.get_video_count())
    channel.set_name('Cool Channel')
    channel.set_video_count(400)
    print(channel.get_name(), channel.get_video_count())

    print(channel._name) # For reflection question 1

    #print(channel.__video_count) # For reflection question 2 - Throws error
    print(channel._YouTubeChannel__video_count) # This works because it's calling the mangled name.


if __name__ == "__main__":
    main()
