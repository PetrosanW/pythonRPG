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
            QtWidgets.QMessageBox.critical(None, "Финал: Шачир умер", "Шачир не выжил, он пытался найти денег на еду но не судьба. Он умер от голода")
            sys.exit()
        elif self.money <= -1000:
            QtWidgets.QMessageBox.critical(None, "Финал: Шачир уехал", "Шачир не нашёл способ как заработать денег и влез в долги. Он обратно уехал к себе в башкирию")
            sys.exit()
        elif self.money >= 1000000:
            QtWidgets.QMessageBox.information(None, "Финал: Богатый Шачир", "Шачир заработал свой 1 миллион и стал крупным бизнесменом")
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
            self.data += timedelta(days=random.randint(2, 4))
        elif self.health == 100:
            self.ui.label_4.setText(f"У тебя полное здоровье")
        self.static()

    def open_dialog(self):
        self.die_shahir()
        self.dialog = QtWidgets.QDialog()
        self.ui_dialog = Ui_Dialog()
        self.ui_dialog.setupUi(self.dialog)
        self.dialog.show()
        self.ui_dialog.DpushButton.clicked.connect(self.Rob)  # Ограбить пятерочку
        self.ui_dialog.DpushButton_2.clicked.connect(self.temka)  # в Мутить темки
        self.ui_dialog.DpushButton_3.clicked.connect(self.karman)  # в разработке
        self.static()

    def Rob(self):
        self.die_shahir()
        lost_money = random.randint(10, 50)
        lost_health = random.randint(5, 20)
        if random.random() < 0.4:
            if random.random() < 0.2:
                self.ui.label_4.setText(f"Тебя поймал охранник, он сдал тебя ментам. Ты отсидел 15 суток, потерял {lost_health} и отдал {lost_money} монет")
                self.money -= lost_money
                self.health -= lost_health
            else:
                self.ui.label_4.setText(f"Тебя поймал охранник, он тебя отпустил но ты отдал {lost_money} монет")
                self.money -= lost_money
        else:
            add_money = random.randint(5, 140)
            self.money += add_money
            self.ui.label_4.setText(f"Тебя никто не поймал, ты наворовал на {add_money} монет")

        self.data += timedelta(days=1)
        self.static()

    def temka(self):
        add_money = random.randint(-500, 5000)
        price = random.randint(500, 1000)
        if self.money >= price:
            self.money -= price
            self.money += add_money
            self.data += timedelta(days=random.randint(1, 10))
            self.ui.label_4.setText(f"Ты купил темку за {price}, и заработал {add_money} монет")
        else:
            self.ui.label_4.setText(f"Не хватает для темки {price - self.money} монет")
        self.static()

    def karman(self):
        QtWidgets.QMessageBox.information(None, "В разработке...", "Думаю что сюда добавить")



    def skiptime(self):  # Неготова
        self.die_shahir()
        self.data += timedelta(days=1)
        self.static()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
