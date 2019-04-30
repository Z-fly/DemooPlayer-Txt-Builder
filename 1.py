import sys

from PyQt5.QtWidgets import *

from de import Ui_MainWindow


class mywindow(QWidget, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    def msg(self):
        fileName, ok = QFileDialog.getSaveFileName(self, "Save", "./", "Text Files (*.txt)")
        if fileName != "":
            txt = open(fileName, "w", encoding='shiftjis')
            txt.write("JSON " + self.line1.text() + "\n")
            txt.write("AUDIO " + self.line2.text() + "\n")
            txt.write("COVER " + self.line3.text() + "\n")
            txt.write("TITLE " + self.line4.text() + "\n")
            txt.write("COMPOSER " + self.line5.text() + "\n")
            txt.write("LEVEL " + self.line6.text() + "\n")
            txt.write("AUDIOVOLUME " + self.line7.text() + "\n")
            txt.write("PIANOVOLUME " + self.line8.text() + "\n")
            txt.write("OFFSET " + self.line9.text())
            txt.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
