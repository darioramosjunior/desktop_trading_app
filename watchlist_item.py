from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QPlainTextEdit


class WatchlistItem(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        coin = QLineEdit()
        coin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        watch_price = QLineEdit()
        watch_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trigger_condition = QComboBox()
        trigger_condition.addItems(["        > / =      ", "          < / =        "])

        trigger_price = QLineEdit()
        trigger_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        status = QLabel("       ALERT      ")  # TO-DO: To set dynamically
        status.setStyleSheet("border: 0.5px solid black;")

        port_size = QLineEdit()
        port_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

        var_percentage = QLineEdit()
        var_percentage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cut_percentage = QLineEdit()
        cut_percentage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cut_percentage.setToolTip("Percentage change between Entry & Cut in the chart")

        pos_size = 8000
        position_size = QLabel(f"        {pos_size} USD        ")
        position_size.setAlignment(Qt.AlignmentFlag.AlignCenter)
        position_size.setStyleSheet("border: 1px solid black;")

        calculate_button = QPushButton("Calculate")

        layout.addWidget(coin)
        layout.addWidget(watch_price)
        layout.addWidget(trigger_condition)
        layout.addWidget(trigger_price)
        layout.addWidget(status)
        layout.addWidget(port_size)
        layout.addWidget(var_percentage)
        layout.addWidget(cut_percentage)
        layout.addWidget(position_size)
        layout.addWidget(calculate_button)

        self.show()


class Columns(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        column1_label = QLabel("   Coin Name   ")
        column1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column2_label = QLabel("  Watch Price  ")
        column2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column3_label = QLabel("   Condition   ")
        column3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column4_label = QLabel(" Trigger Price ")
        column4_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column5_label = QLabel("    Status     ")
        column5_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column6_label = QLabel("Port Size (USD)")
        column6_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column7_label = QLabel("    VAR (%)    ")
        column7_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column8_label = QLabel("    CUT (%)    ")
        column8_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column8_label.setToolTip("Percentage change between Entry & Cut in the chart")
        column9_label = QLabel(" Position Size ")
        column9_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # For column & row value alignment purpose only
        column10_label = QLabel("               ")

        layout.addWidget(column1_label)
        layout.addWidget(column2_label)
        layout.addWidget(column3_label)
        layout.addWidget(column4_label)
        layout.addWidget(column5_label)
        layout.addWidget(column6_label)
        layout.addWidget(column7_label)
        layout.addWidget(column8_label)
        layout.addWidget(column9_label)
        layout.addWidget(column10_label)

        self.show()