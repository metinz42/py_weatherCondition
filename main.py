# Made by Metin Öztaş
from PyQt5.QtWidgets import QWidget
import requests
from bs4 import BeautifulSoup
from untitled_ui import Ui_MainWindow
from haftalik_ui import Ui_NewWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap ,QDesktopServices
from PyQt5.QtCore import QUrl
import sys

class NewWindow(QtWidgets.QMainWindow):
    def __init__(self, city):
        super().__init__()
        self.ui = Ui_NewWindow()
        self.ui.newsetupUi(self)
        self.weekly_weather()
        self.ui.refresh_Button.clicked.connect(self.weekly_weather)

    def weekly_weather(self):
        url = f"https://www.mynet.com/hava-durumu/{city}-haftalik-hava-durumu"
        response =requests.get(url)
        soup = BeautifulSoup(response.text,'html.parser')
        day_name = soup.find('h4',class_='heading mb-0 mr-4 d-flex flex-column').find('strong')
        strong_tags = soup.find_all('strong')
        
        degree1 = strong_tags[9].get_text()
        degree2 = strong_tags[23].get_text()
        degree3 = strong_tags[37].get_text()
        degree4 = strong_tags[51].get_text()
        degree5 = strong_tags[65].get_text()
        degree6 = strong_tags[79].get_text()
        degree7 = strong_tags[93].get_text()

        day2 = strong_tags[22].get_text()
        day3 = strong_tags[36].get_text()
        day4 = strong_tags[50].get_text()
        day5 = strong_tags[64].get_text()
        day6 = strong_tags[78].get_text()
        day7 = strong_tags[92].get_text()

        durum1 = strong_tags[16].get_text()
        durum2 = strong_tags[30].get_text()
        durum3 = strong_tags[44].get_text()
        durum4 = strong_tags[58].get_text()
        durum5 = strong_tags[72].get_text()
        durum6 = strong_tags[86].get_text()
        durum7 = strong_tags[100].get_text()

        self.ui.day1_label.setText(day_name.text)
        self.ui.day2_label.setText(day2)
        self.ui.day3_label.setText(day3)
        self.ui.day4_label.setText(day4)
        self.ui.day5_label.setText(day5)
        self.ui.day6_label.setText(day6)
        self.ui.day7_label.setText(day7)

        self.ui.degree1_label.setText(degree1)
        self.ui.degree2_label.setText(degree2)
        self.ui.degree3_label.setText(degree3)
        self.ui.degree4_label.setText(degree4)
        self.ui.degree5_label.setText(degree5)
        self.ui.degree6_label.setText(degree6)
        self.ui.degree7_label.setText(degree7)

        self.ui.durum_label_1.setText(durum1)
        self.ui.durum_label_2.setText(durum2)
        self.ui.durum_label_3.setText(durum3)
        self.ui.durum_label_4.setText(durum4)
        self.ui.durum_label_5.setText(durum5)
        self.ui.durum_label_6.setText(durum6)
        self.ui.durum_label_7.setText(durum7)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.search_button.clicked.connect(self.get_weather)
        self.ui.refresh_button.clicked.connect(self.get_weather)
        self.ui.haftalikDurum_clbtn.clicked.connect(self.open_new_window)

 
    def get_weather(self):
        global city
        city = self.ui.searchBar_lnedit.text()    
        url = f"https://www.mynet.com/hava-durumu/{city.strip()}-hava-durumu-bugun"
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text,'html.parser')
        instant_div = soup.find('h3', class_='heading mb-2')
        degree = soup.find('strong',{'class':'d-flex align-items-start'})
        self.ui.durumyazi_label.setText(instant_div.text)
        self.ui.degre_label.setText(degree.text+"°")
        if instant_div.text == "Sağanak" or "Yağmur" or "Hafif yağmurlu" or "Kapalı" or "Parçalı Az Bulutlu":
            self.ui.resimDurum_label.setPixmap(QtGui.QPixmap("c:\\Users\\Metin\\Desktop\\Py_weatherCondition\\images/rain.png"))
        if degree.text<"10":
            self.ui.resimDurum_label.setPixmap(QtGui.QPixmap("c:\\Users\\Metin\\Desktop\\Py_weatherCondition\\images/snow.png"))
        if instant_div.text == "Açık":
            self.ui.resimDurum_label.setPixmap(QtGui.QPixmap("c:\\Users\\Metin\\Desktop\\Py_weatherCondition\\images/sun.png"))
    
    def open_new_window(self):
        self.new_window = NewWindow(city)
        self.new_window.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())