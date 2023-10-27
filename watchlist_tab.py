from PyQt6.QtWidgets import QWidget, QVBoxLayout
from watchlist_item import WatchlistItem, Columns


class WatchlistTab(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        columns = Columns()
        coin1 = WatchlistItem()
        coin2 = WatchlistItem()
        coin3 = WatchlistItem()
        coin4 = WatchlistItem()
        coin5 = WatchlistItem()
        coin6 = WatchlistItem()
        coin7 = WatchlistItem()
        coin8 = WatchlistItem()
        coin9 = WatchlistItem()
        coin10 = WatchlistItem()

        layout.addWidget(columns)
        layout.addWidget(coin1)
        layout.addWidget(coin2)
        layout.addWidget(coin3)
        layout.addWidget(coin4)
        layout.addWidget(coin5)
        layout.addWidget(coin6)
        layout.addWidget(coin7)
        layout.addWidget(coin8)
        layout.addWidget(coin9)
        layout.addWidget(coin10)

        self.setLayout(layout)

        self.show()

