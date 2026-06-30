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
        self.name = name
        self.video_count = video_count

    def __str__(self) -> str:
        return f"Channel: {self.name}, Videos: {self.video_count}"

def main():
    channel = YouTubeChannel("UVUCS1410", 150)
    print(channel)

if __name__ == "__main__":
    main()
