
# ("__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\____/\\\________/\\\_")
#   ("_\///////\\\/////____/\\\/////////\\\_\/\\\_____/\\\//_")
#    ("_______\/\\\________\//\\\______\///__\/\\\__/\\\//____")
#    ("_______\/\\\_________\////\\\_________\/\\\\\\//\\\_____")
#     ("_______\/\\\____________\////\\\______\/\\\//_\//\\\____")
#      ("_______\/\\\_______________\////\\\___\/\\\____\//\\\___")
#      (" _______\/\\\________/\\\______\//\\\__\/\\\_____\//\\\__")
#        ("_______\/\\\_______\///\\\\\\\\\\\/___\/\\\______\//\\\_")
#         ("_______\///__________\///////////_____\///________\///__")

from PySide6 import QtWidgets
import sys
import os
import platform
from requests import get
import netifaces

ip = get('https://api.ipify.org').content.decode('utf8')

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computer Informations")
        self.resize(400, 200)
        self.create_layouts()
        self.create_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()
        self.populate_fields()

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.button_layout = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.lbl_Hostname = QtWidgets.QLabel("Hostname")
        self.LEdit_Hostname = QtWidgets.QLineEdit()
        self.LEdit_Hostname.setReadOnly(True)

        self.lbl_Lan = QtWidgets.QLabel("LAN IP Address")
        self.LEdit_Lan = QtWidgets.QLineEdit()
        self.LEdit_Lan.setReadOnly(True)

        self.lbl_Mac = QtWidgets.QLabel("MAC Address")
        self.LEdit_Mac = QtWidgets.QLineEdit(netifaces.ifaddresses('eno1')[netifaces.AF_LINK][0]["addr"])# ['lo', 'eth0', 'tun2']

        self.LEdit_Mac.setReadOnly(True)

        self.lbl_Wan = QtWidgets.QLabel("WAN IP Address")
        self.LEdit_Wan = QtWidgets.QLineEdit(ip)
        self.LEdit_Wan.setReadOnly(True)

        self.lbl_System = QtWidgets.QLabel("System")
        self.LEdit_System = QtWidgets.QLineEdit()
        self.LEdit_System.setReadOnly(True)

        self.btn_Quitter = QtWidgets.QPushButton("Exit")

    def add_widgets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_Hostname)
        self.layoutH1.addWidget(self.LEdit_Hostname)

        self.layoutH2.addWidget(self.lbl_Lan)
        self.layoutH2.addWidget(self.LEdit_Lan)

        self.layoutH3.addWidget(self.lbl_Mac)
        self.layoutH3.addWidget(self.LEdit_Mac)

        self.layoutH4.addWidget(self.lbl_Wan)
        self.layoutH4.addWidget(self.LEdit_Wan)

        self.layoutH5.addWidget(self.lbl_System)
        self.layoutH5.addWidget(self.LEdit_System)

        self.button_layout.addWidget(self.btn_Quitter)

        self.main_layout.addLayout(self.layoutH1)
        self.main_layout.addLayout(self.layoutH2)
        self.main_layout.addLayout(self.layoutH3)
        self.main_layout.addLayout(self.layoutH4)
        self.main_layout.addLayout(self.layoutH5)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(self.close)

    def populate_fields(self):
        self.LEdit_Hostname.setText(platform.node())
        self.LEdit_Lan.setText(self.get_local_ip())
        self.LEdit_System.setText(platform.system())

    def get_local_ip(self):
        try:
            hostname = os.popen("hostname -I").read().strip()
            return hostname.split()[0] if hostname else "Unavailable"
        except Exception:
            return "Unavailable"

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    form = MaFenetre()
    form.show()
    sys.exit(app.exec())
