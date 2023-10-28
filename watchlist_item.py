from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton


class WatchlistItem(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.coin = QLineEdit()
        self.coin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.watch_price = QLineEdit()
        self.watch_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.trigger_condition = QComboBox()
        self.trigger_condition.addItems(["> / =", "< / ="])

        self.trigger_price = QLineEdit()
        self.trigger_price.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status = QLabel("ALERT")  # TO-DO: To set dynamically
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setStyleSheet("border: 0.5px solid black;")

        self.port_size = QLineEdit()
        self.port_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.var_percentage = QLineEdit()
        self.var_percentage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.cut_percentage = QLineEdit()
        self.cut_percentage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cut_percentage.setToolTip("Percentage change between Entry & Cut in the chart")

        self.position_size = QLabel("USD")
        self.position_size.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.position_size.setStyleSheet("border: 1px solid black;")

        calculate_button = QPushButton("Calculate")
        clear_button = QPushButton("Clear")

        # Connections
        calculate_button.clicked.connect(self.calculate_pos_size)
        clear_button.clicked.connect(self.clear_row)

        layout.addWidget(self.coin)
        layout.addWidget(self.watch_price)
        layout.addWidget(self.trigger_condition)
        layout.addWidget(self.trigger_price)
        layout.addWidget(self.status)
        layout.addWidget(self.port_size)
        layout.addWidget(self.var_percentage)
        layout.addWidget(self.cut_percentage)
        layout.addWidget(self.position_size)
        layout.addWidget(calculate_button)
        layout.addWidget(clear_button)

        layout.setStretchFactor(self.coin, 1)
        layout.setStretchFactor(self.watch_price, 1)
        layout.setStretchFactor(self.trigger_condition, 1)
        layout.setStretchFactor(self.trigger_price, 1)
        layout.setStretchFactor(self.status, 1)
        layout.setStretchFactor(self.port_size, 1)
        layout.setStretchFactor(self.var_percentage, 1)
        layout.setStretchFactor(self.cut_percentage, 1)
        layout.setStretchFactor(self.position_size, 1)
        layout.setStretchFactor(calculate_button, 1)
        layout.setStretchFactor(clear_button, 1)

        self.show()

    def calculate_pos_size(self):
        port_size = float(self.port_size.text())
        var_percentage = float(self.var_percentage.text())
        var = port_size * (var_percentage / 100)
        cut_percentage = float(self.cut_percentage.text())
        pos_size = var / (cut_percentage / 100)
        formatted_pos_size = "{:.2f} USD".format(pos_size)
        self.position_size.setText(formatted_pos_size)

    def clear_row(self):
        self.coin.setText("")
        self.watch_price.setText("")
        self.trigger_condition.setCurrentIndex(0)
        self.trigger_price.setText("")
        self.port_size.setText("")
        self.var_percentage.setText("")
        self.cut_percentage.setText("")
        self.position_size.setText("USD")
        print("Clear Row")


class Columns(QWidget):

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        column1_label = QLabel("Coin Name")
        column1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column2_label = QLabel("Watch Price")
        column2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column3_label = QLabel("Condition")
        column3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column4_label = QLabel("Trigger Price")
        column4_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column5_label = QLabel("Status")
        column5_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column6_label = QLabel("Port Size (USD)")
        column6_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column7_label = QLabel("VAR (%)")
        column7_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column8_label = QLabel("CUT (%)")
        column8_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        column8_label.setToolTip("Percentage change between Entry & Cut in the chart")
        column9_label = QLabel(" Position Size ")
        column9_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # For column & row value alignment purpose only
        column10_label = QLabel("")
        column11_label = QLabel("")

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
        layout.addWidget(column11_label)

        layout.setStretchFactor(column1_label, 1)
        layout.setStretchFactor(column2_label, 1)
        layout.setStretchFactor(column3_label, 1)
        layout.setStretchFactor(column4_label, 1)
        layout.setStretchFactor(column5_label, 1)
        layout.setStretchFactor(column6_label, 1)
        layout.setStretchFactor(column7_label, 1)
        layout.setStretchFactor(column8_label, 1)
        layout.setStretchFactor(column9_label, 1)
        layout.setStretchFactor(column10_label, 1)
        layout.setStretchFactor(column11_label, 1)

        self.show()