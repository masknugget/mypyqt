import sys
from PyQt5.Qt import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.playlist = QMediaPlaylist(self)                    # 1
        self.player = QMediaPlayer(self)
        self.player.setPlaylist(self.playlist)

        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('/Users/louis/Downloads/music1.mp3')))  # 2
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('/Users/louis/Downloads/music2.mp3')))
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('/Users/louis/Downloads/music3.mp3')))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)      # 3
        self.playlist.setCurrentIndex(2)                        # 4

        self.player.setVolume(80)                               # 5
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
