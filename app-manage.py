from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGraphicsDropShadowEffect, QGridLayout, QLineEdit, QComboBox, QTextEdit, QHBoxLayout, QListWidget, QFileDialog
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
        menu_search.clicked.connect(IndexManage.search_show)

        menu_add = QPushButton("Add")
        menu_add.setProperty('class', 'menu_button')
        self.addShadow(menu_add)
        menu_layout.addWidget(menu_add, alignment=Qt.AlignmentFlag.AlignCenter)
        menu_add.clicked.connect(IndexManage.data_show)

        menu_setting = QPushButton("Setting (گشادیم میشه)")
        menu_setting.setProperty('class', 'menu_button')
        self.addShadow(menu_setting)
        menu_layout.addWidget(menu_setting, alignment=Qt.AlignmentFlag.AlignCenter)
        menu_setting.clicked.connect(IndexManage.setting_show)

        menu_exit = QPushButton("Exit")
        menu_exit.setProperty('class', 'menu_button')
        self.addShadow(menu_exit)
        menu_layout.addWidget(menu_exit, alignment=Qt.AlignmentFlag.AlignCenter)
        menu_exit.clicked.connect(IndexManage.exit_app)

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

    def exit_app(self):
        index_manage.close()

    def data_show(self):
        index_manage.close()
        data_manage.show()
    
    def search_show(self):
        index_manage.close()
        search_manage.show()
    
    def setting_show(self):
        pass

# -----------------------------------------------

class DataManage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dataUI()
        self.applyStylesheet("static/data.css")

    def dataUI(self):
        main_layout = QVBoxLayout()

        file_input = QPushButton("انتخاب فایل")
        self.addShadow(file_input)
        file_input.setProperty('class', 'file_input')
        main_layout.addWidget(file_input)
        file_input.clicked.connect(DataManage.chose_file_show)

        field_layout = QGridLayout()
        field_layout.setProperty('class', 'field_layout')

        controler_input = QComboBox()
        self.addShadow(controler_input)
        controler_input.setProperty('class', 'controler_input')
        controler_label = QLabel("کنترلر:")
        self.addShadow(controler_label)
        controler_label.setProperty('class', 'controler_label')
        controler_input.addItem("فانوک")
        controler_input.addItem("زیمنس")
        field_layout.addWidget(controler_label, 0, 1)
        field_layout.addWidget(controler_input, 0, 0)

        model_controler_input = QLineEdit()
        self.addShadow(model_controler_input)
        model_controler_input.setProperty('class', 'model_controler_input')
        model_controler_label = QLabel("مدل کنترلر:")
        self.addShadow(model_controler_label)
        model_controler_label.setProperty('class', 'model_control_label')
        field_layout.addWidget(model_controler_label, 1, 1)
        field_layout.addWidget(model_controler_input, 1, 0)

        title_label = QLabel("عنوان:")
        self.addShadow(title_label)
        title_label.setProperty('class', 'title_label')
        title_input = QLineEdit()
        self.addShadow(title_input)
        title_input.setProperty('class', 'title_input')
        field_layout.addWidget(title_label, 2, 1)
        field_layout.addWidget(title_input, 2, 0)

        descriotion_label = QLabel("توضیحات:")
        self.addShadow(descriotion_label)
        descriotion_label.setProperty('class', 'descriotion_label')
        descriotion_input = QTextEdit()
        self.addShadow(descriotion_input)
        descriotion_input.setProperty('class', 'descriotion_input')
        field_layout.addWidget(descriotion_label, 3, 1)
        field_layout.addWidget(descriotion_input, 3, 0)

        save_btn = QPushButton("save")
        self.addShadow(save_btn)
        save_btn.setProperty('class', 'save-btn')
        field_layout.addWidget(save_btn)
        save_btn.clicked.connect(DataManage.save)

        back_btn = QPushButton("back")
        self.addShadow(back_btn)
        back_btn.setProperty('class', 'back-btn')
        field_layout.addWidget(back_btn)
        back_btn.clicked.connect(DataManage.back_index)

        self.setLayout(main_layout)
        main_layout.addLayout(field_layout)

    def addShadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(Qt.GlobalColor.black)
        shadow.setOffset(5, 5)

        widget.setGraphicsEffect(shadow)

    def initUI(self):
        self.setProperty('class', 'body')
        self.setWindowTitle("Add Data")
        self.setGeometry(100, 100, 300, 600)

    def applyStylesheet(self, filename):
        with open(filename, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)

    def back_index(self):
        data_manage.close()
        index_manage.show()

    def save(self):
        pass

    def chose_file_show(self):
        pass

#------------------------------------------

class SearchManage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.searchUI()
        self.applyStylesheet("static/search.css")

    def searchUI(self):
        search_main_layout = QVBoxLayout()

        search_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.addShadow(self.search_input)
        self.search_input.setPlaceholderText("جستجو...")
        self.search_input.setProperty('class', 'search_input')
        search_layout.addWidget(self.search_input)

        search_button = QPushButton("جستجو")
        self.addShadow(search_button)
        search_button.setProperty('class', 'search_button')
        search_layout.addWidget(search_button)

        search_main_layout.addLayout(search_layout)

        result_list = QListWidget()
        result_list.setProperty('class', 'result_list')
        self.addShadow(result_list)
        search_main_layout.addWidget(result_list)

        footer_layout = QGridLayout()

        data_add_btn = QPushButton("افزودن اطلاعات")
        self.addShadow(data_add_btn)
        data_add_btn.setProperty('class', 'data_add_btn')
        footer_layout.addWidget(data_add_btn, 0, 0)
        data_add_btn.clicked.connect(SearchManage.data_show)

        back_btn = QPushButton("back")
        back_btn.setProperty('class', 'back_btn')
        self.addShadow(back_btn)
        footer_layout.addWidget(back_btn, 0, 2)
        back_btn.clicked.connect(SearchManage.back_index)

        search_main_layout.addLayout(footer_layout)

        self.setLayout(search_main_layout)

    def addShadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(Qt.GlobalColor.black)
        shadow.setOffset(2, 2)

        widget.setGraphicsEffect(shadow)

    def initUI(self):
        self.setProperty('class', 'body')
        self.setWindowTitle("صفحه جستجو")
        self.setGeometry(100, 100, 300, 600)

    def applyStylesheet(self, filename):
        with open(filename, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)

    def back_index(self):
        search_manage.close()
        index_manage.show()

    def data_show(self):
        search_manage.close()
        data_manage.show()

if __name__ == "__main__":
    app = QApplication([])
    index_manage = IndexManage()
    data_manage = DataManage()
    search_manage = SearchManage()
    index_manage.show()
    app.exec()