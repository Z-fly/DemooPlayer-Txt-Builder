import sys

from PyQt5.QtWidgets import *

from de import Ui_MainWindow


class mywindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def save(self):
        fileName, ok = QFileDialog.getSaveFileName(self, "Save", "./", "(*.txt)")
        if fileName != "":
            txt = open(fileName, "w", encoding='shiftjis')
            txt.write("JSON " + self.line1.text() + "\n")
            txt.write("AUDIO " + self.line2.text() + "\n")
            txt.write("COVER " + self.line3.text() + "\n")
            txt.write("TITLE " + self.line4.text() + "\n")
            txt.write("COMPOSER " + self.line5.text() + "\n")
            txt.write("DIFFICULTY " + self.line6.text() + "\n")
            txt.write("LEVEL " + self.line7.text() + "\n")
            txt.write("AUDIOVOLUME " + self.line8.text() + "\n")
            txt.write("PIANOVOLUME " + self.line9.text() + "\n")
            txt.write("OFFSET " + self.line10.text())
            txt.close()

    def read(self):
        fileName, ok = QFileDialog.getOpenFileName(self, "Open", './', "(*.*)")
        if fileName != "":
            with open(fileName, 'r') as f:
                for i in f.readlines():
                    if i[0:4] == "Name":
                        self.line4.setText(i[5:-1])
                    if i[0:6] == "Artist":
                        self.line5.setText(i[7:-1])
                    if i[0:4] == "Extra":
                        self.line6.setText("3")
                        self.line7.setText(i[5:])
                        if self.line7.text()[-1] == "\n":
                            self.line7.setText(self.line7.text()[:-1])
                    if i[0:4] == "Hard":
                        self.line6.setText("2")
                        self.line7.setText(i[5:])
                        if self.line7.text()[-1] == "\n":
                            self.line7.setText(self.line7.text()[:-1])
                    if i[0:4] == "Normal":
                        self.line6.setText("1")
                        self.line7.setText(i[5:])
                        if self.line7.text()[-1] == "\n":
                            self.line7.setText(self.line7.text()[:-1])
                    if i[0:4] == "Easy":
                        self.line6.setText("0")
                        self.line7.setText(i[5:])
                        if self.line7.text()[-1] == "\n":
                            self.line7.setText(self.line7.text()[:-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
