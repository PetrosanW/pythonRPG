from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: #323232;\n"
"font-family: Tacticalbit;")
        self.DpushButton = QPushButton(Dialog)
        self.DpushButton.setObjectName(u"DpushButton")
        self.DpushButton.setGeometry(QRect(30, 40, 341, 71))
        self.DpushButton.setStyleSheet(u"color: white;")
        self.DpushButton_2 = QPushButton(Dialog)
        self.DpushButton_2.setObjectName(u"DpushButton_2")
        self.DpushButton_2.setGeometry(QRect(30, 120, 341, 71))
        self.DpushButton_2.setStyleSheet(u"color: white;")
        self.DpushButton_3 = QPushButton(Dialog)
        self.DpushButton_3.setObjectName(u"DpushButton_3")
        self.DpushButton_3.setGeometry(QRect(30, 210, 341, 71))
        self.DpushButton_3.setStyleSheet(u"color: white;")
        self.Dlabel = QLabel(Dialog)
        self.Dlabel.setObjectName(u"Dlabel")
        self.Dlabel.setGeometry(QRect(30, 15, 341, 21))
        self.Dlabel.setStyleSheet(u"color: white;\n"
"background-color: None;\n"
"border: None;")
        self.Dlabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u0437\u0430\u0440\u0430\u0431\u043e\u043a\u0442\u0430", None))
        self.DpushButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0433\u0440\u0430\u0431\u0438\u0442\u044c \u043f\u044f\u0442\u0435\u0440\u043e\u0447\u043a\u0443", None))
        self.DpushButton_2.setText(QCoreApplication.translate("Dialog", u"\u041c\u0443\u0442\u0438\u0442\u044c \u0442\u0435\u043c\u043a\u0438", None))
        self.DpushButton_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043a\u0430 \u043d\u0435 \u043f\u0440\u0438\u0434\u0443\u043c\u0430\u043b", None))
        self.Dlabel.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0421\u043f\u043e\u0441\u043e\u0431 \u0437\u0430\u0440\u0430\u0431\u043e\u043a\u0442\u0430", None))
    # retranslateUi

