from PyQt6.QtWidgets import QWidget, QVBoxLayout
from watchlist_item import WatchlistItem, Columns


class WatchlistTab(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        columns = Columns()
        coin1 = WatchlistItem()
        coin1.set_row_id(1)
        coin2 = WatchlistItem()
        coin2.set_row_id(2)
        coin3 = WatchlistItem()
        coin3.set_row_id(3)
        coin4 = WatchlistItem()
        coin4.set_row_id(4)
        coin5 = WatchlistItem()
        coin5.set_row_id(5)
        coin6 = WatchlistItem()
        coin6.set_row_id(6)
        coin7 = WatchlistItem()
        coin7.set_row_id(7)
        coin8 = WatchlistItem()
        coin8.set_row_id(8)
        coin9 = WatchlistItem()
        coin9.set_row_id(9)
        coin10 = WatchlistItem()
        coin10.set_row_id(10)

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

