from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsDropShadowEffect, QGridLayout, QLineEdit, QComboBox, QTextEdit, QHBoxLayout, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtCore import Qt


class IndexManage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.indexUI()

    def indexUI(self):
        menu_layout = QVBoxLayout()

        menu_layout.addStretch()

        menu_search = QPushButton("Search")
        menu_search.setProperty('class', 'menu_button')
        self.addShadow(menu_search)
        menu_layout.addWidget(menu_search, alignment=Qt.AlignmentFlag.AlignCenter)

        menu_add = QPushButton("Add")
        menu_add.setProperty('class', 'menu_button')
        self.addShadow(menu_add)
        menu_layout.addWidget(menu_add, alignment=Qt.AlignmentFlag.AlignCenter)

        menu_setting = QPushButton("Setting (گشادیم میشه)")
        menu_setting.setProperty('class', 'menu_button')
        self.addShadow(menu_setting)
        menu_layout.addWidget(menu_setting, alignment=Qt.AlignmentFlag.AlignCenter)

        menu_exit = QPushButton("Exit")
        menu_exit.setProperty('class', 'menu_button')
        self.addShadow(menu_exit)
        menu_layout.addWidget(menu_exit, alignment=Qt.AlignmentFlag.AlignCenter)

        menu_layout.addStretch()

        footer = QLabel("------------------------------------------")
        footer.setProperty('class', 'footer')
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        menu_layout.addWidget(footer)

        footer_creator = QLabel("Created by: Mahdi Khosrojerdi")
        footer_creator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_creator.setProperty('class', 'footer')
        menu_layout.addWidget(footer_creator)

        self.setLayout(menu_layout)
        self.applyStylesheet('static/index.css')

    def initUI(self):
        self.setProperty('class', 'body')
        self.setWindowTitle("CNC Search")
        self.setGeometry(100, 100, 300, 600)

    def applyStylesheet(self, filename):
        # خواندن فایل CSS
        with open(filename, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)

    def addShadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(Qt.GlobalColor.black)
        shadow.setOffset(5, 5)
        widget.setGraphicsEffect(shadow)

if __name__ == "__main__":
    app = QApplication([])
    index_manage = IndexManage()
    index_manage.show()
    app.exec()