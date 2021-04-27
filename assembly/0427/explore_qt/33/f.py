import sys
from PyQt5.Qt import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.player = QMediaPlayer(self)            # 1
        self.media_content = QMediaContent(QUrl.fromLocalFile('/Users/louis/Downloads/music.mp3'))  # 2
        # self.player.setMedia(QMediaContent(QUrl('http://example.com/music.mp3')))
        self.player.setMedia(self.media_content)    # 3
        self.player.setVolume(80)                   # 4
        self.player.play()                          # 5


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
