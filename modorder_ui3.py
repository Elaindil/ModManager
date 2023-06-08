# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modorder_ui3.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QLabel,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 100, 291, 311))
        self.chooseModFolderbutton = QPushButton(self.centralwidget)
        self.chooseModFolderbutton.setObjectName(u"chooseModFolderbutton")
        self.chooseModFolderbutton.setGeometry(QRect(50, 30, 141, 21))
        self.chooseOptionFileButton = QPushButton(self.centralwidget)
        self.chooseOptionFileButton.setObjectName(u"chooseOptionFileButton")
        self.chooseOptionFileButton.setGeometry(QRect(590, 30, 121, 31))
        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(470, 100, 291, 311))
        self.listWidget_2.setDragEnabled(True)
        self.listWidget_2.setDragDropOverwriteMode(False)
        self.listWidget_2.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget_2.setDefaultDropAction(Qt.CopyAction)
        self.listWidget_2.setMovement(QListView.Static)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(330, 450, 91, 21))
        self.presetsComboBox = QComboBox(self.centralwidget)
        self.presetsComboBox.setObjectName(u"presetsComboBox")
        self.presetsComboBox.setGeometry(QRect(340, 60, 69, 22))
        self.savePresetButton = QPushButton(self.centralwidget)
        self.savePresetButton.setObjectName(u"savePresetButton")
        self.savePresetButton.setGeometry(QRect(300, 10, 141, 41))
        self.modLabel = QLabel(self.centralwidget)
        self.modLabel.setObjectName(u"modLabel")
        self.modLabel.setGeometry(QRect(80, 70, 111, 16))
        self.activatedModsLabel = QLabel(self.centralwidget)
        self.activatedModsLabel.setObjectName(u"activatedModsLabel")
        self.activatedModsLabel.setGeometry(QRect(580, 70, 131, 16))
        self.presetsLabel = QLabel(self.centralwidget)
        self.presetsLabel.setObjectName(u"presetsLabel")
        self.presetsLabel.setGeometry(QRect(430, 60, 101, 21))
        self.removeModButton = QPushButton(self.centralwidget)
        self.removeModButton.setObjectName(u"removeModButton")
        self.removeModButton.setGeometry(QRect(514, 423, 241, 31))
        self.helpButton = QPushButton(self.centralwidget)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setGeometry(QRect(20, 510, 75, 24))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 180, 81, 21))
        self.removeButton = QPushButton(self.centralwidget)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(340, 240, 75, 24))
        self.deletePresetButton = QPushButton(self.centralwidget)
        self.deletePresetButton.setObjectName(u"deletePresetButton")
        self.deletePresetButton.setGeometry(QRect(220, 60, 81, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mod Manager", None))
        self.chooseModFolderbutton.setText(QCoreApplication.translate("MainWindow", u"Select mod folder", None))
        self.chooseOptionFileButton.setText(QCoreApplication.translate("MainWindow", u"Select option file", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Save changes", None))
        self.savePresetButton.setText(QCoreApplication.translate("MainWindow", u"Save Preset Mod Order", None))
        self.modLabel.setText(QCoreApplication.translate("MainWindow", u"Available mods", None))
        self.activatedModsLabel.setText(QCoreApplication.translate("MainWindow", u"Activated mods order", None))
        self.presetsLabel.setText(QCoreApplication.translate("MainWindow", u"Mod order presets", None))
        self.removeModButton.setText(QCoreApplication.translate("MainWindow", u"Deactivate selected mod", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Activate Mod", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Disable Mod", None))
        self.deletePresetButton.setText(QCoreApplication.translate("MainWindow", u"Delete Preset", None))
    # retranslateUi

