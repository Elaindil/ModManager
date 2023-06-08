import sys
from PySide6.QtWidgets import (QMainWindow,QApplication,QFileDialog,QListWidgetItem,QAbstractItemView,QMessageBox,QInputDialog,QLineEdit)
from modorder_ui3 import Ui_MainWindow
import os
import json
import re
# print(os.path.isfile('optionsfile.json'))
fileToCheck = ''
x = ['s','d']
# ww = 
replaceSymbol = {'\t':'','{name "':'','"}':'','\n':''}
modlist = {}    
def openOptionFile():
    # global w
    global fileToCheck
    global activatedModList
    modsFound = False
    if os.path.isfile('optionsfile.json'):
        jsonFile = 'optionsfile.json'
        with open (jsonFile, 'r') as f:
            
            data = json.load(f)
            print(data)
            fname = QFileDialog.getOpenFileName(None,'Find options file in Documents\my games\gates of hell\profiles\XXXX or \AppData\Local\digitalmindsoft\gates of hell\profiles\  ',data)
    else:
        fname = QFileDialog.getOpenFileName()
    activatedModList = []
    fileToCheck = fname[0]
    with open (fileToCheck) as f:
            for line in f:
                if 'mod_' in line:
                    activatedModList.append(line)
                if '{mods' in line:
                    modsFound = True
    
    print (fileToCheck)
    if fileToCheck != '':
        with open('optionsfile.json','w')as file:
            json.dump(fileToCheck,file)
    
    if modsFound == False:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("No mods activated")
        msg.setInformativeText('First activate any mod in the game to use the programm.\nRestart the programm when you do it.')
        msg.setWindowTitle("Error")
        msg.exec()
        sys.exit()
    
    # with open (fileToCheck) as f:
    
    w.populateOptionsList()
    
def openModFolder():
    
    global directoryToCheck
    # if os.path.isfile('optionsfile.json'):
        # jsonFile = 'optionsfile.json'
        # with open (jsonFile, 'r') as f:
            
            # data = json.load(f)
            # print(data)
            # fname = QFileDialog.getOpenFileName(None,'Locate options file',data)
    # else:
    if os.path.isfile('modsfile.json'):
        jsonFileMod = 'modsfile.json'
        with open (jsonFileMod, 'r') as fmod:
            
            datamod = json.load(fmod)
            print(datamod)
            fname = QFileDialog.getExistingDirectory(None,'Choose Steam\steamapps\workshop\content\\400750',datamod)
    else:
        fname = QFileDialog.getExistingDirectory(None,'Choose Steam\steamapps\workshop\content\\400750')
    directoryToCheck = fname
    # print (directoryToCheck)
    if directoryToCheck != '':
        with open('modsfile.json','w')as file:
            json.dump(directoryToCheck,file)
    
    directory_list = list()
    global modlist
    modlist = {}
    for item in os.listdir(fname):
        if os.path.isdir(os.path.join(fname, item)):
            modfolder = os.path.join(fname, item)
            if os.path.isfile(f'{fname}/{item}/mod.info'):
                with open(f'{fname}/{item}/mod.info') as modinfo:
                    for line in modinfo:
                        if '{name' in line:
                            print (line)
                            for key,itema in replaceSymbol.items():
                                line = line.replace(key,itema)
                                modfolder = modfolder.replace('\\','/')
                            modlist[f'{item}'] = line + '-' + item
    # print (modlist)
    w.populateModList()
    # w.populateList()


# def checkfilenow(self):
    # if os.path.isfile('optionsfile.json'):
    
        # fileToCheck = 'optionsfile.json'
     
    # w.checkfilenow()  
# def populateList():
    # return


# def checkfilenow():
    # if os.path.isfile('optionsfile.json'):
        # fileToCheck = 'optionsfile.json'
        # populateList()

class MyApp(QMainWindow):
    def initiatesModStuff(self):                
        if os.path.isfile('modsfile.json'):
            jsonFileMod = 'modsfile.json'
            with open (jsonFileMod, 'r') as f:
                data = json.load(f)
                directory_list = list()
                modlistinitial = {}
                for item in os.listdir(data):
                    if os.path.isdir(os.path.join(data, item)):
                        modfolder = os.path.join(data, item)
                        if os.path.isfile(f'{data}/{item}/mod.info'):
                            with open(f'{data}/{item}/mod.info') as modinfo:
                                for line in modinfo:
                                    if '{name' in line:
                                        # print (line)
                                        for key,itema in replaceSymbol.items():
                                            line = line.replace(key,itema)
                                            modfolder = modfolder.replace('\\','/')
                                        modlistinitial[f'{item}'] = line + '-' + item 
                newItem = QListWidgetItem()
                newItem.setText('sadsa')
                for key in modlistinitial.values():
                    self.ui.listWidget.addItem(key)
                # self.ui.listWidget.addItem(newItem)
                # self.ui.listWidget.addItem('x')
                quantity = self.ui.listWidget.count()
                # print(quantity)
        
            return modlistinitial
    
    def initiatesOptionStuff(self):
        if os.path.isfile('optionsfile.json'):
            jsonFile = 'optionsfile.json'
            modsFound = False
            with open (jsonFile, 'r') as filejson:
                data = json.load(filejson)
                activatedModList = []
            
                with open (data,'r') as f:
                    for line in f:
                        if 'mod_' in line:
                            print(line)
                            activatedModList.append(line)
                        if '{mods' in line:
                            modsFound = True

            for activeMod in activatedModList:
                if not self.ui.modlistinitial:
                    self.ui.listWidget_2.addItem(activeMod)
                else:
                    print('else')
                    for key,value in self.ui.modlistinitial.items():
                        # print(key)
                        # self.ui.listWidget_2.addItem(value)
                        if key in activeMod:
                            # print('sssss')
                            # print(key)
                            self.ui.listWidget_2.addItem(value)
            if modsFound == False:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("No mods activated")
                msg.setInformativeText('First activate any mod in the game to use the programm.\nRestart the programm when you do it.')
                msg.setWindowTitle("Error")
                msg.exec()
                
                        
    
    def deactivateMod(self):
        modDeactivate = self.ui.listWidget_2.selectedItems()
        if not modDeactivate:
            return        
        for itemtake in modDeactivate:
            self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(itemtake))
    
    def activateMod(self):
        modActivate = self.ui.listWidget.selectedItems()
        if not modActivate:
            
            return        
        for itemadd in modActivate:
            print('yes')
            self.ui.listWidget_2.addItem(itemadd.text())
    
    def deactivateAllMods(self):
        self.ui.listWidget_2.takeItem(self.ui.listWidget_2.clear())
        # self.ui.listWidget_2.takeItem(1)
    
    def helpButton(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("How to use the program")
        msg.setInformativeText("To use this programm you need to have at least one mod activated in game first! This programm will not work if there are no mods activated! First locate your mod folder. It should be in Steam\steamapps\workshop\content\400750. Then select your options file, it should be in Documents\my games\gates of hell\profiles\XXXX or \AppData\Local\digitalmindsoft\gates of hell\profiles\\. Their locations will be saved next time you load the programm and you won't have to do it again. Left window has all workshop mods that were found in your mod folder. Right window show all mods that are activated and in what order they are in. You can double click mods to activate\deactivate them or use corresponding button. Drag mods in the right window to set the mod order you need. You can save and delete mod order presets to easily switch between them. After you make your changes make sure to save them to take effect. If you have any more questions then ask on mod page or in discord. If you encounter strange behaviour, restart the programm.\n\nMod made by MrCookie")
        msg.setWindowTitle("Read me")
        msg.exec()
    
    def savePreset(self):
        textget = QInputDialog.getText(self, "Enter name for preset",
                                "Preset name:")
        presetJson = 'presetfile.json'
        oldPresets = json.load(open(presetJson))
        if type(oldPresets) is dict:
            oldPresets = [oldPresets]
        with open(presetJson,'w')as file:
            
            
            # print(jsondata)
            
            modOrderList=[]
            modListName = {}
            # print(text)
            for i in range(self.ui.listWidget_2.count()):
                # text[f'{text}'] = self.ui.listWidget_2.item(i).text()
                modOrderList.append(self.ui.listWidget_2.item(i).text())
                   # <--- should reset file position to the beginning.
            
            modListName [textget[0]] = modOrderList
            oldPresets.append(modListName)
            # print(datanew)
            json.dump(oldPresets,file)
            # print(text)
        self.ui.presetsComboBox.addItem(textget[0])    
    
    def deletePreset(self):
        deleteMePreset = self.ui.presetsComboBox.currentText()
        presetJson = 'presetfile.json'
        oldPresets = json.load(open(presetJson))
        if type(oldPresets) is dict:
            oldPresets = [oldPresets]
        with open(presetJson,'w')as file:
            # print(oldPresets)
            for presetList in oldPresets:
                for presetMods,presetValues in presetList.items():
                    if presetMods == self.ui.presetsComboBox.currentText():
                        print(presetList)
                        print(type(presetList))
                        print(presetMods)
                        
                        presetList.clear()
                        break
                
                        # file[presetMods] = presetList
                        # print(presetMods)
                        # self.ui.listWidget_2.addItem(values)
        
        
            json.dump(oldPresets,file)
            # print(text)
  

    def createPresetFile(self):
        if not os.path.isfile('presetfile.json'):
            empty = {'no preset':'x'}
            with open('presetfile.json','w')as file:
                json.dump(empty,file)
        else:
            if os.path.getsize('presetfile.json') == 0:
                dummyfile = {'no preset':'x'}
                with open('presetfile.json','w')as file:
                    json.dump(dummyfile,file)
    
    def comboBoxOptions(self):
        try:
            presetsValue = json.load(open('presetfile.json'))
        except:
            pass
        try:
            for presetsName in presetsValue:
                for keyPreset in presetsName.keys():
                    print(keyPreset)
                    self.ui.presetsComboBox.addItem(keyPreset)
        except:
            pass
                
    def changeActivatedModList(self):
        self.ui.listWidget_2.clear()
        presetsValue = json.load(open('presetfile.json'))
        
        for presetsName in presetsValue:
            # print(type(presetsName))
            # print(presetsName)
            # self.ui.listWidget_2.clear()
            for presetMods,presetValues in presetsName.items():
                if presetMods == self.ui.presetsComboBox.currentText():
                    for values in presetValues:
                        print(values)
                        self.ui.listWidget_2.addItem(values)
                    
                # print(presetMods)
                # print(type(presetMods))
                    # print('break')
                # print(presetName)
        # for values in presetMods:
            # print(values)
                    # self.ui.listWidget_2.clear()
            
                    # break
        
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # if os.path.isfile('optionsfile.json'):
        # print(modlist)   
        self.ui.modlistinitial = self.initiatesModStuff()
        # self.ui = checkfilenow()
        self.ui.chooseOptionFileButton.clicked.connect(lambda:openOptionFile())
        self.ui.chooseModFolderbutton.clicked.connect(lambda:openModFolder())
        self.ui.removeButton.clicked.connect(lambda:self.deactivateMod())
        self.ui.pushButton.clicked.connect(lambda:self.activateMod())
        self.ui.listWidget.itemDoubleClicked.connect(lambda:self.activateMod())
        self.ui.listWidget_2.itemDoubleClicked.connect(lambda:self.deactivateMod())
        self.ui.removeModButton.clicked.connect(lambda:self.deactivateAllMods())
        self.ui.savePresetButton.clicked.connect(lambda:self.savePreset())
        self.ui.deletePresetButton.clicked.connect(lambda:self.deletePreset())
        self.ui.helpButton.clicked.connect(lambda:self.helpButton())
        self.ui.chooseOptionFileButton.setEnabled(False)
        self.ui.listWidget_2.setDragDropMode(QAbstractItemView.InternalMove)
        self.ui.presetsComboBox.textActivated.connect(lambda:self.changeActivatedModList())  
        
        # self.ui.listWidget.addItem('x')
        # self.ui.listWidget.addItem('x')
        # self.ui.listWidget.addItem('a')
        # self.ui.listWidget.setSortingEnabled(True)
        # self.ui.listWidget.itemPressed.()
        # self.ui.listWidget.supportedDropActions()
        # checkfilenow(self)
        # global ww
        # ww = MyApp()
        # checkfilenow(self)
        # self.initiatesModStuff()
        # self.ui.modlistinitial = modlistinitial
        self.initiatesOptionStuff()
        self.createPresetFile()
        self.comboBoxOptions()
        
        # print(self.ui.modlistinitial)
        
        def saveChanges():
            items = []
            for x in range(self.ui.listWidget_2.count()):
                items.append(self.ui.listWidget_2.item(x).text())
                
               
            newlines = ''
            jsonFile = 'optionsfile.json'
            for i in items:
                newlines = newlines + '\t'+'\t'+'"mod_'+re.sub('.*-','',i) + ':0"'+'\n'
                
            
            with open (jsonFile, 'r') as f:
                data = json.load(f)
                with open (data,'r+') as newfile:
                    newfile2 = newfile.read()
                    
                    newfile3 = re.sub('(?<=\t{mods\n)[^`]*(?=\t})','',newfile2)
                    newfile3 = re.sub('(?<={mods\n)[^`]*(?=\t})',newlines,newfile2)
                    # print(newfile3)
                    newfile.truncate(0)
                    newfile.seek(0)
                    newfile.write(newfile3)
                    newfile.close()
            
            # data = json.load(f)
            
            print(items)
            
        
        self.ui.pushButton_3.clicked.connect(lambda:saveChanges())
    
    def populateOptionsList(self):
        # newItem = QListWidgetItem()
        # newItem.setText('sadsa')
        # with open (fileToCheck) as f:
            # for line in f:
                # if 'mod_' in line:
                    # self.ui.listWidget_2.addItem(line)
        self.ui.listWidget_2.clear()
        for activeMod in activatedModList:
            # self.ui.listWidget_2.clear()
            if not modlist:
                self.ui.listWidget_2.addItem(activeMod)
            else:
                print('else')
                for key,value in modlist.items():
                    print(key)
                    if key in activeMod:
                        self.ui.listWidget_2.addItem(value)
        
        # self.ui.listWidget.addItem(newItem)
        # self.ui.listWidget.addItem('x')
        quantity = self.ui.listWidget_2.count()
        print(quantity)
        # self.ui.listWidget.update()
        print('x')
    
    
    def populateModList(self):
        self.ui.listWidget.clear()
        for key in modlist.values():
            self.ui.listWidget.addItem(key)
        # self.ui.listWidget.addItem(newItem)
        # self.ui.listWidget.addItem('x')
        quantity = self.ui.listWidget.count()
        print(quantity)
        # self.ui.listWidget.update()
        print('x')
        self.ui.chooseOptionFileButton.setEnabled(True)
    
        
     
    # w.checkfilenow() 
    
        # self.ui.pushButton.clicked.connect(self.populateList())
# x.puplateList('s')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = MyApp()
    # ex.setupUi(w)
    w.show()
    sys.exit(app.exec())


 
ww = MyApp()
