class Sentiment:
    def __init__(self) -> None:
        self.current_emoji = '😭'

    def update_current_emoji(self, emoji):
        self.current_emoji = emoji

    def get_current_emoji(self):
        return self.current_emoji
