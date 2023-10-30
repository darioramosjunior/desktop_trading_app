from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTabWidget, QWidget, QVBoxLayout
import sys
from watchlist_tab import WatchlistTab
from analytics_tab import AnalyticsTab
from news_tab import NewsTab
from database import Database

database = Database()
database.create_watchlist_table()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Futures Trading App")
        self.setMinimumSize(800,600)
        # self.setStyleSheet("""
        #             QMainWindow {
        #                 background-color: #303030;
        #                 color: #ffffff;
        #             }
        #             QPushButton {
        #                 background-color: #202020;
        #                 color: #ffffff;
        #                 border: 1px solid #505050;
        #             }
        #             QPushButton:hover {
        #                 background-color: #404040;
        #             }
        #         """)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a tab widget
        tab_widget = QTabWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(tab_widget)
        central_widget.setLayout(central_layout)

        # Create and add tabs to the tab widget
        watchlist_tab = WatchlistTab()
        analytics_tab = AnalyticsTab()
        news_tab = NewsTab()

        tab_widget.addTab(watchlist_tab, "Watchlist")
        tab_widget.addTab(news_tab, "News")
        tab_widget.addTab(analytics_tab, "Performance")

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
