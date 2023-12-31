from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QTabBar  # Import QTabBar
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
        self.setMinimumSize(800, 600)

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

        # Style the tab bar to make tab titles visible
        tab_bar = tab_widget.tabBar()
        tab_bar.setStyleSheet("""
            QTabBar::tab {
                background-color: #404040;
                color: #FFFFFF;
                font-weight: bold;
                border: 1px solid black;
                width: 150px;
                padding: 6px;
            }
            QTabBar::tab:selected {
                background-color: #555555;
            }
        """)

        # Apply a dark theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2B2B2B;
                color: #FFFFFF;
            }
            QWidget {
                background-color: #2B2B2B;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #404040;
                color: #FFFFFF;
                border: 1px solid black;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QLineEdit, QComboBox, QLabel {
                background-color: #404040;
                color: #FFFFFF;
                border: 1px solid black;
                padding: 5px;
            }
        """)

        # Set the border of the tab widget content
        tab_widget.setStyleSheet("""
                    QTabWidget::pane {
                        border: 1px solid #404040; /* Set the border color to match the background */
                    }
                """)

        self.show()


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    app.exec()
