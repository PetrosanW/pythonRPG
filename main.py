import sys
import random
from datetime import datetime, timedelta

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from mainwindow import Ui_MainWindow
from dialogzar import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        die = False
        self.health = 100
        self.money = 0
        self.data = datetime.strptime("01.01.2024", "%d.%m.%Y")
        self.ui.label.setText(f"Здоровье: {self.health}")
        self.ui.label_2.setText(f"Монет: {self.money}")
        self.ui.label_3.setText(f"Дата: {self.data.strftime('%d.%m.%Y')}")

        self.ui.pushButton.clicked.connect(self.healthadd)  # Восстановить здоровье
        self.ui.pushButton_2.clicked.connect(self.open_dialog)  # Подзаработать
        self.ui.pushButton_3.clicked.connect(self.skiptime)  # Пропустить время

    def die_shahir(self):
        if self.health <= 0:
            QtWidgets.QMessageBox.critical(None, "Произошла трагедия", "Шачир не выжил в этом жёстоком мире")
            sys.exit()

    def static(self):
        self.ui.label.setText(f"Здоровье: {self.health}")
        self.ui.label_2.setText(f"Монет: {self.money}")
        self.ui.label_3.setText(f"Дата: {self.data.strftime('%d.%m.%Y')}")
    def healthadd(self):
        self.die_shahir()
        if self.health < 100:
            self.health += 10
            if self.health > 100:
                self.health = 100
            self.data += timedelta(days=1)
        elif self.health == 100:
            self.ui.label_4.setText(f"У тебя полное здоровье")
        self.static()

    def open_dialog(self):
        self.die_shahir()
        self.dialog = QtWidgets.QDialog()
        self.ui_dialog = Ui_Dialog()
        self.ui_dialog.setupUi(self.dialog)
        self.dialog.show()
        self.ui_dialog.DpushButton.clicked.connect(self.Rob_5)  # Ограбить пятерочку
        # self.ui_dialog.DpushButton_2.clicked.connect()  # в разработке
        # self.ui_dialog.DpushButton_3.clicked.connect()  # в разработке
        self.static()

    def Rob_5(self):
        self.die_shahir()
        lost_money = random.randint(10, 100)
        lost_health = random.randint(5, 20)
        if random.random() < 0.5:
            if random.random() < 0.5:
                self.ui.label_4.setText(f"Тебя поймал охранник, он сдал тебя ментам. Ты отсидел 15 суток, потерял {lost_health} и отдал {lost_money} монет")
                self.money -= lost_money
                self.health -= lost_health
            else:
                self.ui.label_4.setText(f"Тебя поймал охранник, он тебя отпустил но ты отдал {lost_money} монет")
                self.money -= lost_money
        else:
            add_money = random.randint(10, 1000)
            self.money += add_money
            self.ui.label_4.setText(f"Тебя никто не поймал, ты наворовал на {add_money} монет")

        self.data += timedelta(days=1)
        self.static()

    def skiptime(self):  # Неготова
        self.die_shahir()
        self.data += timedelta(days=1)
        self.static()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
