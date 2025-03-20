from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QDir
from gui import Ui_MainWindow
import resources_rc
import os
import string

def get_root_drives():
    drives = []
    for drive in string.ascii_uppercase:
        if os.path.exists(f"{drive}:/"):
            drives.append(f"{drive}:/")
    return drives

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("InvestAcc Filing System")
        self.setWindowIcon(QIcon(":newPrefix/app.ico"))
        tray_icon = QSystemTrayIcon(self)
        tray_icon.setIcon(QIcon(":/newPrefix/app.ico"))
        tray_icon.show()
        self.ui.sb_minimise_but.clicked.connect(lambda: self.change_sb(1))
        self.ui.sb_maximise_but.clicked.connect(lambda: self.change_sb(0))
        self.ui.sb_home_but.clicked.connect(lambda: self.change_widget(0))
        self.ui.sb_max_home_but.clicked.connect(lambda: self.change_widget(0))
        self.ui.sb_min_search_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.sb_max_search_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.sb_min_file_but.clicked.connect(lambda: self.change_widget(7))
        self.ui.sb_max_file_but.clicked.connect(lambda: self.change_widget(7))
        self.ui.home_search_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.home_file_but.clicked.connect(lambda: self.change_widget(7))
        self.ui.search_select_back_but.clicked.connect(lambda: self.change_widget(0))
        self.ui.search_select_advisers_but.clicked.connect(lambda: self.change_widget(2))
        self.ui.search_select_sipp_but.clicked.connect(lambda: self.change_widget(3))
        self.ui.search_select_ssas_but.clicked.connect(lambda: self.change_widget(4))
        self.ui.search_select_flexi_but.clicked.connect(lambda: self.change_widget(5))
        self.ui.search_advisers_back_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.search_advisers_but.clicked.connect(lambda: self.change_widget(6))
        self.ui.search_sipp_back_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.search_sipp_but.clicked.connect(lambda: self.change_widget(6))
        self.ui.search_ssas_back_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.search_ssas_but.clicked.connect(lambda: self.change_widget(6))
        self.ui.search_flexi_back_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.search_flexi_but.clicked.connect(lambda: self.change_widget(6))
        self.ui.search_results_back_but.clicked.connect(lambda: self.change_widget(1))
        self.ui.filing_back_but.clicked.connect(lambda: self.change_widget(0))
        self.ui.filing_select_storage.addItems([" ","Advisers", "SIPP", "SSAS", "Flexi"])
        self.ui.filing_select_storage.currentIndexChanged.connect(self.change_file)
        self.ui.filing_select_storage.setCurrentIndex(0)
        self.ui.filing_loc_stacked_widget.setCurrentIndex(0)
        self.populate_combobox()


    def populate_combobox(self):
        self.ui.filing_select_dir.clear()
        drives = get_root_drives() if os.name =="nt" else ["/"]
        
        for drive in drives:
            self.ui.filing_select_dir.addItem(drive)

    def change_sb(self, page_index):
        self.ui.sidebar.setCurrentIndex(page_index)
    
    def change_widget(self, page_index):
        self.ui.main_stacked_widget.setCurrentIndex(page_index)

    def change_file(self):
        index = self.ui.filing_select_storage.currentIndex()
        self.ui.filing_loc_stacked_widget.setCurrentIndex(index)



if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(":newPrefix/app.ico"))
    window = MainApp()
    window.show()
    app.exec_()