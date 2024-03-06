from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet(u"background-color: #323232;\n"
"font-family: Tacticalbit;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 160, 60))
        font = QFont()
        font.setFamilies([u"Tacticalbit"])
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: white;\n"
"background-color: None;\n"
"border: None;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 40, 160, 60))
        font1 = QFont()
        font1.setFamilies([u"Tacticalbit"])
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"color: white;\n"
"background-color: None;\n"
"border: None;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(529, 40, 211, 60))
        self.label_3.setFont(font1)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"color: white;\n"
"background-color: None;\n"
"border: None;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 490, 221, 61))
        self.pushButton.setStyleSheet(u"color: white;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 170, 761, 221))
        self.label_4.setStyleSheet(u"color: white;\n"
"border:3px solid white;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 490, 251, 61))
        self.pushButton_2.setStyleSheet(u"color: white;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 490, 211, 61))
        self.pushButton_3.setStyleSheet(u"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pythonRPG", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u043e\u0440\u043e\u0432\u044c\u0435: 100", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" \u041c\u043e\u043d\u0435\u0442: 0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" \u0414\u0430\u0442\u0430: 06.03.2024", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0443\u043b\u044f\u0442\u043e\u0440 \u0428\u0410\u0427\u0418\u0420\u0410", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0437\u0430\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0434\u0435\u043d\u0435\u0433", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0434\u0435\u043d\u044c", None))
    # retranslateUi

