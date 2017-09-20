# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:46:13 2017

@author: Nathan Leroi
"""

import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QAction
#from PyQt5 import QtWidgets
import os

m = 0.000
pathDir = ''
newFolder = ''
filePlace = ''
newTextFile = ''

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1000, 700)
        self.setWindowTitle('iSWING Software')
        self.setWindowIcon(QIcon('python.gif'))        
        self.home()    
    
    
    def home(self):
        
        btnQ = QPushButton('Quit', self)
        btnQ.resize(300,100)
        btnQ.move(700,600)
        btnQ.clicked.connect(self.closeApp)
        
        btnD = QPushButton('Save', self)
        btnD.resize(50,30)
        btnD.move(330,10)
        btnD.clicked.connect(self.btn_click_directory)
        self.a = QLabel(self)
        self.a.setText('Choose Directory:')
        self.a.move(10,10)
        self.directory = QLineEdit(self)
        self.directory.resize(200, 30)
        self.directory.move(120, 10)
        self.directoryName = QLabel(self)
        self.directoryName.setText(pathDir)
        self.directoryName.move(390,10)
        self.directoryName.resize(300,30)
        
        btnF = QPushButton('Save', self)
        btnF.resize(50,30)
        btnF.move(230,50)
        btnF.clicked.connect(self.btn_click_folder)
        self.b = QLabel(self)
        self.b.setText('Choose Folder:')
        self.b.move(10,50)
        self.folder = QLineEdit(self)
        self.folder.resize(100, 30)
        self.folder.move(120, 50)
        self.folderName = QLabel(self)
        self.folderName.setText(newFolder)
        self.folderName.move(300,50)
        self.folderName.resize(200,30)
        
        btnP = QPushButton('Create Folder', self)
        btnP.resize(100,30)
        btnP.move(700,10)
        btnP.clicked.connect(self.btn_click_createPath)
        self.pathName = QLabel(self)
        self.pathName.setText('Waiting...')
        self.pathName.move(820,10)
        self.pathName.resize(200,30)
        
        btnf = QPushButton('Create File', self)
        btnf.resize(100,30)
        btnf.move(680,50)
        btnf.clicked.connect(self.btn_click_file)
        self.b = QLabel(self)
        self.b.setText('File Name:')
        self.b.move(500,50)
        self.file = QLineEdit(self)
        self.file.resize(100, 30)
        self.file.move(570, 50)
        self.fileName = QLabel(self)
        self.fileName.setText('')
        self.fileName.move(800,50)
        self.fileName.resize(200,30)
  
        
        
        btnM = QPushButton('Save', self)
        btnM.resize(50,30)
        btnM.move(120,100)
        btnM.clicked.connect(self.btn_click_mass)
        self.mass = QLineEdit(self)
        self.mass.resize(100,30)
        self.mass.move(10,100)
        self.massName = QLabel(self)
        self.massName.setText('Mass = ' + str(m) + 'kg')
        self.massName.move(180,100)
        
        
        self.show()
    
# The function down bellow is triggered when the button is pressed.
# It adds the value in the text box to the text printed on the window
# It also changes the desired value 
        
    def btn_click_mass(self):                        
        global m
        new_name = self.mass.text()
        self.massName.setText('Mass = '+ new_name + 'kg')
        m = float(new_name)
        return m
    
    def btn_click_directory(self):                        
        global pathDir
        new_name = self.directory.text()
        self.directoryName.setText(new_name)
        pathDir = '/'.join(new_name.split('\\'))
        return pathDir
    
    def btn_click_folder(self):                        
        global newFolder
        new_name = self.folder.text()
        self.folderName.setText(new_name)
        newFolder = new_name
        return newFolder
    
    def btn_click_createPath(self):                        
        global filePlace
        filePlace = pathDir +'/'+ newFolder +'/'
        if pathDir == '' or newFolder == '':
            self.pathName.setText('Incorrect')
        else:
            os.makedirs(filePlace, exist_ok=False) 
            self.pathName.setText('Path Created'+'('+newFolder+')')
        return filePlace
    
    def btn_click_file(self):                        
        global newTextFile
        if self.pathName.text() == 'Incorrect' or self.pathName.text() == 'Waiting...':
            self.fileName.setText('Path Required...')
        else:
            new_name = self.file.text()
            newTextFile = new_name
            openFile = open(filePlace + newTextFile + '.txt', "w")
            openFile.close()
            self.fileName.setText('File Created'+'('+newTextFile+'.txt)')
        return newTextFile
    
    
    def closeApp (self):
        print(m)
        print(pathDir)
        print(newFolder)
        print(filePlace)  
        print(newTextFile)
        sys.exit()
    
def run():
    
    app = QApplication(sys.argv)
    Gui = Window()
#    Gui.show()
    sys.exit(app.exec_())

run()

