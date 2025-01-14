# ("__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\____/\\\________/\\\_")
#   ("_\///////\\\/////____/\\\/////////\\\_\/\\\_____/\\\//_")
#    ("_______\/\\\________\//\\\______\///__\/\\\__/\\\//____")
#    ("_______\/\\\_________\////\\\_________\/\\\\\\//\\\_____")
#     ("_______\/\\\____________\////\\\______\/\\\//_\//\\\____")
#      ("_______\/\\\_______________\////\\\___\/\\\____\//\\\___")
#      (" _______\/\\\________/\\\______\//\\\__\/\\\_____\//\\\__")
#        ("_______\/\\\_______\///\\\\\\\\\\\/___\/\\\______\//\\\_")
#         ("_______\///__________\///////////_____\///________\///__")

import math
from PySide6 import QtGui
from PySide6 import QtWidgets

class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(340, 200)
        self.setWindowTitle("BTS Snir-2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()

    def create_layouts(self):

        self.layoutVall = QtWidgets.QVBoxLayout()

        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutV1 = QtWidgets.QVBoxLayout()
        self.layoutV2 = QtWidgets.QVBoxLayout()
        self.layoutV3 = QtWidgets.QVBoxLayout()
        self.layoutV4 = QtWidgets.QVBoxLayout()
        # self.layoutV5 = QtWidgets.QVBoxLayout()

        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()
        self.layoutH6 = QtWidgets.QHBoxLayout()



    def create_widgets(self):

        self.lbl_espace = QtWidgets.QLabel("")

        self.radioBt_duree= QtWidgets.QRadioButton("Durée")
        self.radioBt_hdd= QtWidgets.QRadioButton("HDD")

        self.lbl_Nom = QtWidgets.QLabel("Taille  :")
        self.LEdit_Nom = QtWidgets.QLineEdit()

        self.lbl_Ips = QtWidgets.QLabel("Ips       :")
        self.LEdit_Ips = QtWidgets.QLineEdit()

        self.lbl_Hdd = QtWidgets.QLabel("Hdd    :")
        self.LEdit_Hdd = QtWidgets.QLineEdit()

        self.lbl_Duree = QtWidgets.QLabel("Durée :")

        self.lbl_Jour = QtWidgets.QLabel("Jour")
        self.LEdit_Jour = QtWidgets.QLineEdit()

        self.lbl_Heures = QtWidgets.QLabel("Heures")
        self.LEdit_Heures = QtWidgets.QLineEdit()

        self.lbl_Minutes = QtWidgets.QLabel("Minutes")
        self.LEdit_Minutes = QtWidgets.QLineEdit()
        
        self.lbl_Secondes = QtWidgets.QLabel("Secondes")
        self.LEdit_Secondes = QtWidgets.QLineEdit()


        self.btn_Effacer = QtWidgets.QPushButton("Calculer")
        self.btn_Quitter = QtWidgets.QPushButton("Exit")

        self.radioBt_hdd.setChecked(True)
        self.LEdit_Hdd.setDisabled(True)

        self.lblImage = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("Icons-Land-Vista-Hardware-Devices-Security-Camera.72.png")
        self.lblImage.setPixmap(pixmap)

        self.LEdit_Nom.setFixedWidth(250)
        self.LEdit_Ips.setFixedWidth(250)
        self.LEdit_Hdd.setFixedWidth(250)


    def addWigets_to_layouts(self):
        #############################################################################################

        self.layoutH0.addWidget(self.radioBt_duree)
        self.layoutH0.addWidget(self.radioBt_hdd)

        self.layoutH1.addWidget(self.lbl_Nom)
        self.layoutH1.addWidget(self.LEdit_Nom)

        self.layoutH2.addWidget(self.lbl_Ips)
        self.layoutH2.addWidget(self.LEdit_Ips)

        self.layoutH3.addWidget(self.lbl_Hdd)
        self.layoutH3.addWidget(self.LEdit_Hdd)

        self.layoutH4.addWidget(self.lbl_Duree)
        self.layoutH4.addLayout(self.layoutV1)
        self.layoutH4.addLayout(self.layoutV2)
        self.layoutH4.addLayout(self.layoutV3)
        self.layoutH4.addLayout(self.layoutV4)


        self.layoutH5.addWidget(self.btn_Effacer)
        self.layoutH5.addWidget(self.btn_Quitter)

        #############################################################################################

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)

        self.layoutV1.addWidget(self.lbl_Jour)
        self.layoutV1.addWidget(self.LEdit_Jour)

        self.layoutV2.addWidget(self.lbl_Heures)
        self.layoutV2.addWidget(self.LEdit_Heures)

        self.layoutV3.addWidget(self.lbl_Minutes)
        self.layoutV3.addWidget(self.LEdit_Minutes)

        self.layoutV4.addWidget(self.lbl_Secondes)
        self.layoutV4.addWidget(self.LEdit_Secondes)

        self.layoutH6.addLayout((self.layoutV))
        self.layoutH6.addWidget((self.lblImage))


        self.layoutVall.addLayout((self.layoutH6))
        self.layoutVall.addWidget(self.lbl_espace)
        self.layoutVall.addWidget(self.lbl_espace)
        self.layoutVall.addWidget(self.lbl_espace)

        self.layoutVall.addLayout((self.layoutH4))
        self.layoutVall.addWidget(self.lbl_espace)
        self.layoutVall.addWidget(self.lbl_espace)
        self.layoutVall.addWidget(self.lbl_espace)

        self.layoutVall.addLayout((self.layoutH5))

        self.setLayout(self.layoutVall)


    #############################################################################################

    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Effacer.clicked.connect(self.calculer)
        self.radioBt_hdd.clicked.connect(self.activer)
        self.radioBt_duree.clicked.connect(self.desactiver)

    def activer(self):
        if self.radioBt_hdd.isChecked():
            print("HDD activé")
            self.enable_duration_fields(True)

    def desactiver(self):
        if self.radioBt_duree.isChecked():
            print("Durée activée")
            self.disabled_duration_fields(False)

    def calculer(self):
        print("Je calcule")

        try:
            taille = int(self.LEdit_Nom.text()) if self.LEdit_Nom.text().isdigit() else 0
            ips = int(self.LEdit_Ips.text()) if self.LEdit_Ips.text().isdigit() else 0
            hdd = int(self.LEdit_Hdd.text()) if self.LEdit_Hdd.text().isdigit() else 0

            if taille == 0 or ips == 0 or hdd == 0:
                QtWidgets.QMessageBox.warning(self, "Erreur","Tous les champs doivent contenir une valeur valide différente de 0.")
                return

            total_secondes = taille * (1024 * 1024) / (hdd * ips)

            jours = math.floor(total_secondes / (24 * 3600))  # 1 jour = 86400 s
            heures_restantes = total_secondes % (24 * 3600)
            heures = math.floor(heures_restantes / 3600)  # 1 heure = 3600 s
            minutes_restantes = heures_restantes % 3600
            minutes = math.floor(minutes_restantes / 60)  # 1 minute = 60 s
            secondes = math.floor(minutes_restantes % 60)

            self.LEdit_Jour.setText(str(jours))
            self.LEdit_Heures.setText(str(heures))
            self.LEdit_Minutes.setText(str(minutes))
            self.LEdit_Secondes.setText(str(secondes))

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Erreur", f"Une erreur est survenue : {e}")

    def enable_duration_fields(self, state):
        self.LEdit_Hdd.setDisabled(True)
        self.LEdit_Ips.setEnabled(True)
        self.LEdit_Nom.setEnabled(True)
        self.LEdit_Jour.setEnabled(True)
        self.LEdit_Heures.setEnabled(True)
        self.LEdit_Minutes.setEnabled(True)
        self.LEdit_Secondes.setEnabled(True)

    def disabled_duration_fields(self, state):
        self.LEdit_Hdd.setEnabled(True)
        self.LEdit_Ips.setEnabled(True)
        self.LEdit_Nom.setEnabled(True)
        self.LEdit_Jour.setDisabled(True)
        self.LEdit_Heures.setDisabled(True)
        self.LEdit_Minutes.setDisabled(True)
        self.LEdit_Secondes.setDisabled(True)

app = QtWidgets.QApplication([])
form = MaFenetre()
form.show()
app.exec()

