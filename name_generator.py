# © 2024 Rinmiolc All rights reserved.
# Version 1.0.1(2024.6.15)
# This software is licensed under the MIT License.
# You may obtain a copy of the License at
# https://opensource.org/licenses/MIT


import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QClipboard
from PyQt5.QtGui import QIcon

def load_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.read().strip().split(',')
    # 去除空格
    names = [name.strip() for name in names if name.strip()]
    return names

def create_name(surnames, names):
    surname = random.choice(surnames)
    name = random.choice(names)
    return f"{surname}{name}"

class NameGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('名字生成器')
        icon = QIcon('favicon.ico')
        self.setWindowIcon(icon)
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(400, 240)
        self.setMaximumSize(400, 240)

        # 设置全局字体为微软雅黑
        font = QFont('Microsoft YaHei', 16)

        self.result = QLineEdit(self)
        self.result.setReadOnly(True)
        self.result.setFixedSize(300, 50)
        self.result.setFont(font)
        self.result.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result)

        self.generate_button = QPushButton('生成', self)
        self.generate_button.setFixedSize(100, 50)
        self.generate_button.setFont(font)
        self.generate_button.clicked.connect(self.generate_name)
        self.layout.addWidget(self.generate_button, alignment=Qt.AlignCenter)

        self.copy_button = QPushButton('复制', self)
        self.copy_button.setFixedSize(100, 50)
        self.copy_button.setFont(font)
        self.copy_button.clicked.connect(self.copy_name)
        self.layout.addWidget(self.copy_button, alignment=Qt.AlignCenter)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        author_font = QFont('Microsoft YaHei', 10)
        self.author_label = QLabel('© 2024 Rinmiolc. All rights reserved.', self)
        self.author_label.setFont(author_font)
        self.author_label.setStyleSheet("color: grey;")
        self.layout.addWidget(self.author_label, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        self.surnames = load_names('NameLibrary/surname.txt')
        self.names = load_names('NameLibrary/name.txt')

    def generate_name(self):
        full_name = create_name(self.surnames, self.names)
        self.result.setText(full_name)

    def copy_name(self):
        clipboard = QApplication.clipboard()
        full_name = self.result.text()
        if full_name:
            clipboard.setText(full_name)
        else:
            QMessageBox.warning(self, "警告", "还没有生成名字")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NameGeneratorApp()
    ex.show()
    sys.exit(app.exec_())
