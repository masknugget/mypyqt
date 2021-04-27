import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QCheckBox, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.sound_effect = QSoundEffect(self)
        self.sound_effect.setSource(QUrl.fromLocalFile('sound.wav'))    # 1
        self.sound_effect.setVolume(1.0)                                # 2

        self.play_btn = QPushButton('Play Sound', self)
        self.play_btn.clicked.connect(self.sound_effect.play)

        self.slider = QSlider(Qt.Horizontal, self)                      # 3
        self.slider.setRange(0, 10)
        self.slider.setValue(10)
        self.slider.valueChanged.connect(self.set_volume_func)

        self.checkbox = QCheckBox('Mute', self)                         # 4
        self.checkbox.stateChanged.connect(self.mute_func)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.play_btn)
        self.h_layout.addWidget(self.checkbox)
        self.v_layout.addWidget(self.slider)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def set_volume_func(self):
        self.sound_effect.setVolume(self.slider.value()/10)

    def mute_func(self):
        if self.sound_effect.isMuted():
            self.sound_effect.setMuted(False)
        else:
            self.sound_effect.setMuted(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())