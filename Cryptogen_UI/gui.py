import sys 
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from cryptogen import encrypt, decrypt
import qrainbowstyle
import qrainbowstyle.windows



class WarwickHack21(QDialog):
    def __init__(self):
        super(WarwickHack21,self).__init__()
        loadUi('gui.ui',self)
        self.image=None
        self.loadButton.clicked.connect(self.loadClicked)
        self.saveButton.clicked.connect(self.saveClicked)
        self.enc1.clicked.connect(self.enc1Clicked)
        self.enc2.clicked.connect(self.enc2Clicked)
        self.enc3.clicked.connect(self.enc3Clicked)
        self.enc4.clicked.connect(self.enc4Clicked)
        self.enc5.clicked.connect(self.enc5Clicked)
        self.dec1.clicked.connect(self.dec1Clicked)
        self.dec2.clicked.connect(self.dec2Clicked)
        self.dec3.clicked.connect(self.dec3Clicked)
        self.dec4.clicked.connect(self.dec4Clicked)
        self.dec5.clicked.connect(self.dec5Clicked)

    @pyqtSlot()
    def enc1Clicked(self):
        frame=self.image
        self.image=encrypt.gotham(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def enc2Clicked(self):
        frame=self.image
        self.image=encrypt.krypton(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def enc3Clicked(self):
        frame=self.image
        self.image=encrypt.atlantis(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def enc4Clicked(self):
        frame=self.image
        self.image=encrypt.oa(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def enc5Clicked(self):
        frame=self.image
        self.image=encrypt.starling(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def dec1Clicked(self):
        frame=self.image
        self.image=decrypt.batman(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def dec2Clicked(self):
        frame=self.image
        self.image=decrypt.superman(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def dec3Clicked(self):
        frame=self.image
        self.image=decrypt.aquaman(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def dec4Clicked(self):
        frame=self.image
        self.image=decrypt.green_lantern(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def dec5Clicked(self):
        frame=self.image
        self.image=decrypt.green_arrow(frame, 'F')
        self.displayImage(2)

    @pyqtSlot()
    def loadClicked(self):
        fname,filter =QFileDialog.getOpenFileName(self,'Open File','/',"Image Files (*.png)")
        if fname:
            self.loadImage(fname)
        else:
            print('Invalid Image')

    @pyqtSlot()
    def saveClicked(self):
        fname, filter = QFileDialog.getSaveFileName(self, 'Save File', '/', "Image Files (*.png)")
        if fname:
            cv2.imwrite(fname,self.image)
        else:
            print('Error')


    def loadImage(self,fname):
        self.image=cv2.imread(fname,cv2.IMREAD_COLOR)
        self.displayImage(1)

    def displayImage(self,window=1):
        qformat=QImage.Format_Indexed8

        if len(self.image.shape)==3: #rows[0],cols[1],channels[2]
            if(self.image.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(self.image,self.image.shape[1],self.image.shape[0],self.image.strides[0],qformat)
        #BGR > RGB
        img= img.rgbSwapped()
        if window==1:
            self.imgLabel.setPixmap(QPixmap.fromImage(img))
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        if window==2:
            self.processedLabel.setPixmap(QPixmap.fromImage(img))
            self.processedLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

if __name__=='__main__':
    app=QApplication(sys.argv)
    stylesheet = qrainbowstyle.load_stylesheet_pyqt5(style='oceanic')
    app.setStyleSheet(stylesheet)
    window=WarwickHack21()
    window.setWindowTitle('Cryptogen GUI')
    window.show()
    sys.exit(app.exec_())