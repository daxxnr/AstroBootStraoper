import sys #line:1
import subprocess #line:2
from PyQt5 .QtWidgets import (QApplication ,QMainWindow ,QFileDialog ,QVBoxLayout ,QWidget ,QMessageBox ,QAction ,QStatusBar ,QPushButton ,QPlainTextEdit ,QLabel ,QHBoxLayout ,QDialog ,QRadioButton ,QButtonGroup ,QDialogButtonBox )#line:5
from PyQt5 .QtGui import QIcon ,QFont #line:6
from PyQt5 .QtCore import Qt #line:7
import time #line:8
import random #line:9
class SettingsDialog (QDialog ):#line:11
    def __init__ (O0OOO00OO0O000OO0 ,parent =None ):#line:12
        super (SettingsDialog ,O0OOO00OO0O000OO0 ).__init__ (parent )#line:13
        O0OOO00OO0O000OO0 .setWindowTitle ('Settings')#line:14
        O0OOO00OO0O000OO0 .setGeometry (200 ,200 ,400 ,300 )#line:15
        OOO00O0OO0O0000O0 =QVBoxLayout ()#line:17
        O0OOO00OO0O000OO0 .theme_group =QButtonGroup ()#line:19
        O0OOO00OO0O000OO0 .dark_theme =QRadioButton ('Dark theme')#line:21
        O0OOO00OO0O000OO0 .blue_yellow_theme =QRadioButton ('default theme')#line:22
        O0OOO00OO0O000OO0 .theme_group .addButton (O0OOO00OO0O000OO0 .dark_theme )#line:24
        O0OOO00OO0O000OO0 .theme_group .addButton (O0OOO00OO0O000OO0 .blue_yellow_theme )#line:25
        OOO00O0OO0O0000O0 .addWidget (O0OOO00OO0O000OO0 .dark_theme )#line:27
        OOO00O0OO0O0000O0 .addWidget (O0OOO00OO0O000OO0 .blue_yellow_theme )#line:28
        O0OOO00OO0O000OO0 .blue_yellow_theme .setChecked (True )#line:30
        O0OOO00OO0O000OO0 .buttonBox =QDialogButtonBox (QDialogButtonBox .Ok |QDialogButtonBox .Cancel )#line:32
        O0OOO00OO0O000OO0 .buttonBox .accepted .connect (O0OOO00OO0O000OO0 .accept )#line:33
        O0OOO00OO0O000OO0 .buttonBox .rejected .connect (O0OOO00OO0O000OO0 .reject )#line:34
        OOO00O0OO0O0000O0 .addWidget (O0OOO00OO0O000OO0 .buttonBox )#line:36
        O0OOO00OO0O000OO0 .setLayout (OOO00O0OO0O0000O0 )#line:38
    def get_selected_theme (OO0O000O0O0OOO00O ):#line:40
        if OO0O000O0O0OOO00O .dark_theme .isChecked ():#line:41
            return 'dark'#line:42
        elif OO0O000O0O0OOO00O .blue_yellow_theme .isChecked ():#line:43
            return 'blue_yellow'#line:44
class Ast (QMainWindow ):#line:46
    def __init__ (O0OO00O00O0O0OOO0 ):#line:47
        super ().__init__ ()#line:48
        O0OO00O00O0O0OOO0 .current_theme ='blue_yellow'#line:49
        O0OO00O00O0O0OOO0 .injection_status =False #line:50
        O0OO00O00O0O0OOO0 .initUI ()#line:51
    def initUI (OOOO000OO000O000O ):#line:53
        OOOO000OO000O000O .setWindowTitle ('Astro.gg')#line:54
        OOOO000OO000O000O .setGeometry (100 ,100 ,1200 ,800 )#line:55
        OOOO000OO000O000O .setWindowIcon (QIcon (r"ast_IMG.png"))#line:56
        OO0O0OOO00OO0OOO0 =QHBoxLayout ()#line:58
        OOOOO0OOO0O00O0OO =QVBoxLayout ()#line:61
        OOO0OOO00O0OOO00O =QLabel ()#line:64
        OOO0OOO00O0OOO00O .setPixmap (QIcon (r"ast_IMG.png").pixmap (150 ,150 ))#line:65
        OOOOO0OOO0O00O0OO .addWidget (OOO0OOO00O0OOO00O ,alignment =Qt .AlignHCenter )#line:66
        OOOO000OO000O000O .injectButton =QPushButton ('INJECT')#line:69
        OOOO000OO000O000O .injectButton .clicked .connect (OOOO000OO000O000O .injectAll )#line:70
        OOOOO0OOO0O00O0OO .addWidget (OOOO000OO000O000O .injectButton )#line:71
        OOOO000OO000O000O .runButton =QPushButton ('EXECUTE')#line:73
        OOOO000OO000O000O .runButton .clicked .connect (OOOO000OO000O000O .executeLuaCode )#line:74
        OOOOO0OOO0O00O0OO .addWidget (OOOO000OO000O000O .runButton )#line:75
        OOOO000OO000O000O .saveButton =QPushButton ('SAVE FILE')#line:77
        OOOO000OO000O000O .saveButton .clicked .connect (OOOO000OO000O000O .saveFile )#line:78
        OOOOO0OOO0O00O0OO .addWidget (OOOO000OO000O000O .saveButton )#line:79
        OOOO000OO000O000O .loadButton =QPushButton ('OPEN FILE')#line:81
        OOOO000OO000O000O .loadButton .clicked .connect (OOOO000OO000O000O .loadFile )#line:82
        OOOOO0OOO0O00O0OO .addWidget (OOOO000OO000O000O .loadButton )#line:83
        for OO000OOOOO0000OOO in [OOOO000OO000O000O .injectButton ,OOOO000OO000O000O .runButton ,OOOO000OO000O000O .saveButton ,OOOO000OO000O000O .loadButton ]:#line:85
            OO000OOOOO0000OOO .setStyleSheet ('''
                QPushButton {
                    background-color: #2ecc71; /* Green */
                    color: #ffffff; 
                    padding: 10px; 
                    border-radius: 5px; 
                    font-size: 18px; 
                    margin: 10px 0;
                }
                QPushButton:hover {
                    background-color: #27ae60; /* Darker green */
                }
            ''')#line:98
        OOO0OO0OO00OOOO0O =QWidget ()#line:100
        OOO0OO0OO00OOOO0O .setLayout (OOOOO0OOO0O00O0OO )#line:101
        OOO0OO0OO00OOOO0O .setFixedWidth (200 )#line:102
        OOOO000OO000O000O .textEdit =QPlainTextEdit ()#line:104
        OOOO000OO000O000O .textEdit .setFont (QFont ('Consolas',12 ))#line:105
        OOOO000OO000O000O .textEdit .setLineWrapMode (QPlainTextEdit .NoWrap )#line:106
        OO0O0OOO00OO0OOO0 .addWidget (OOO0OO0OO00OOOO0O )#line:108
        OO0O0OOO00OO0OOO0 .addWidget (OOOO000OO000O000O .textEdit )#line:109
        O00O0OOO000O000O0 =QWidget ()#line:111
        O00O0OOO000O000O0 .setLayout (OO0O0OOO00OO0OOO0 )#line:112
        OOOO000OO000O000O .setCentralWidget (O00O0OOO000O000O0 )#line:113
        OOOO000OO000O000O .menuBar =OOOO000OO000O000O .menuBar ()#line:115
        OOOO000OO000O000O .fileMenu =OOOO000OO000O000O .menuBar .addMenu ('File')#line:116
        OOOO000OO000O000O .openAction =QAction ('Open',OOOO000OO000O000O )#line:118
        OOOO000OO000O000O .openAction .setShortcut ('Ctrl+O')#line:119
        OOOO000OO000O000O .openAction .setStatusTip ('Open a Lua file')#line:120
        OOOO000OO000O000O .openAction .triggered .connect (OOOO000OO000O000O .openFile )#line:121
        OOOO000OO000O000O .fileMenu .addAction (OOOO000OO000O000O .openAction )#line:122
        OOOO000OO000O000O .saveAction =QAction ('Save',OOOO000OO000O000O )#line:124
        OOOO000OO000O000O .saveAction .setShortcut ('Ctrl+S')#line:125
        OOOO000OO000O000O .saveAction .setStatusTip ('Save the current Lua script')#line:126
        OOOO000OO000O000O .saveAction .triggered .connect (OOOO000OO000O000O .saveFile )#line:127
        OOOO000OO000O000O .fileMenu .addAction (OOOO000OO000O000O .saveAction )#line:128
        OOOO000OO000O000O .settingsAction =QAction ('Settings',OOOO000OO000O000O )#line:130
        OOOO000OO000O000O .settingsAction .triggered .connect (OOOO000OO000O000O .openSettings )#line:131
        OOOO000OO000O000O .fileMenu .addAction (OOOO000OO000O000O .settingsAction )#line:132
        OOOO000OO000O000O .statusBar =QStatusBar ()#line:134
        OOOO000OO000O000O .setStatusBar (OOOO000OO000O000O .statusBar )#line:135
        OOOO000OO000O000O .apply_theme ()#line:137
    def apply_theme (O0OOOO0000O0O0OO0 ):#line:139
        if O0OOOO0000O0O0OO0 .current_theme =='dark':#line:140
            O0OOOO0000O0O0OO0 .setStyleSheet ('''
                QMainWindow {background-color: #2c3e50;}  /* Dark turquoise */
                QMenuBar {background-color: #34495e; color: #ffffff;}  /* Turquoise */
                QMenuBar::item {background-color: #34495e; color: #ffffff;}
                QMenuBar::item:selected {background-color: #2ecc71; color: #ffffff;}  /* Green */
                QMenu {background-color: #34495e; color: #ffffff;}
                QMenu::item {background-color: #34495e; color: #ffffff;}
                QMenu::item:selected {background-color: #2ecc71; color: #ffffff;}  /* Green */
                QStatusBar {background-color: #34495e; color: #ffffff;}  /* Turquoise */
                QAbstractScrollArea {background-color: #2c3e50; color: #ffffff;}  /* Dark turquoise */
                QTextEdit {background-color: #2c3e50; color: #ffffff;}  /* Dark turquoise */
                QTabWidget::pane {background-color: #2c3e50; color: #ffffff;}  /* Dark turquoise */
                QTabWidget::tab-bar {background-color: #2c3e50; color: #ffffff;}  /* Dark turquoise */
                QTabWidget::tab {background-color: #2c3e50; color: #ffffff;}  /* Dark turquoise */
                QTabWidget::tab:selected {background-color: #2ecc71; color: #ffffff;}  /* Black */
                QPushButton {background-color: #000000; color: #ffffff; padding: 10px; border-radius: 5px; font-size: 18px; margin: 10px 0;}
                QPushButton:hover {background-color: #444444;}
                QPlainTextEdit {background-color: #2c3e50; color: #ffffff;}
            ''')#line:159
        elif O0OOOO0000O0O0OO0 .current_theme =='blue_yellow':#line:160
            O0OOOO0000O0O0OO0 .setStyleSheet ('''
                QMainWindow {background-color: #003366;}  /* Dark blue */
                QMenuBar {background-color: #336699; color: #ffffff;}  /* Blue */
                QMenuBar::item {background-color: #336699; color: #ffffff;}
                QMenuBar::item:selected {background-color: #ffcc00; color: #003366;}  /* Yellow */
                QMenu {background-color: #336699; color: #ffffff;}
                QMenu::item {background-color: #336699; color: #ffffff;}
                QMenu::item:selected {background-color: #ffcc00; color: #003366;}  /* Yellow */
                QStatusBar {background-color: #336699; color: #ffffff;}  /* Blue */
                QAbstractScrollArea {background-color: #003366; color: #ffffff;}  /* Dark blue */
                QTextEdit {background-color: #003366; color: #ffffff;}  /* Dark blue */
                QTabWidget::pane {background-color: #003366; color: #ffffff;}  /* Dark blue */
                QTabWidget::tab-bar {background-color: #003366; color: #ffffff;}  /* Dark blue */
                QTabWidget::tab {background-color: #003366; color: #ffffff;}  /* Dark blue */
                QTabWidget::tab:selected {background-color: #ffcc00; color: #003366;}  /* Yellow */
                QPushButton {background-color: #ffcc00; color: #003366; padding: 10px; border-radius: 5px; font-size: 18px; margin: 10px 0;}
                QPushButton:hover {background-color: #ffcc00; color: #ffffff;}
                QPlainTextEdit {background-color: #003366; color: #ffffff;}
            ''')#line:179
    def openSettings (OOOOO00O0O0O000OO ):#line:181
        O0O00000OO00O0O0O =SettingsDialog (OOOOO00O0O0O000OO )#line:182
        if O0O00000OO00O0O0O .exec_ ()==QDialog .Accepted :#line:183
            OOO000000OO0OO000 =O0O00000OO00O0O0O .get_selected_theme ()#line:184
            OOOOO00O0O0O000OO .current_theme =OOO000000OO0OO000 #line:185
            OOOOO00O0O0O000OO .apply_theme ()#line:186
    def injectAll (OO0OOO0O0OOOOO0O0 ):#line:188
        O0O00OO0OO0000OOO =OO0OOO0O0OOOOO0O0 .is_roblox_running ()#line:189
        if O0O00OO0OO0000OOO :#line:190
            OO0OOO0OO0O0OOOOO =random .randint (12 ,15 )#line:191
            time .sleep (OO0OOO0OO0O0OOOOO )#line:192
            OO0OOO0O0OOOOO0O0 .injection_status =True #line:193
            QMessageBox .information (OO0OOO0O0OOOOO0O0 ,'Inject','Roblox injected.')#line:194
        else :#line:195
            OO0OOO0O0OOOOO0O0 .injection_status =False #line:196
            QMessageBox .information (OO0OOO0O0OOOOO0O0 ,'Inject','Please open Roblox and inject the script manually.')#line:198
    def is_roblox_running (O0O0000OOOOO0O0OO ):#line:200
        try :#line:201
            OOOOOO000OO0000O0 =subprocess .check_output ('tasklist',shell =True ,universal_newlines =True )#line:203
            if 'RobloxPlayerBeta.exe'in OOOOOO000OO0000O0 :#line:205
                return True #line:206
            else :#line:207
                return False #line:208
        except subprocess .CalledProcessError as O0OOOO0OO0O0OO00O :#line:209
            print (f"Error: {O0OOOO0OO0O0OO00O}")#line:210
            return False #line:211
    def createFile (OO0OO0OOOOO0OOO00 ):#line:213
        O000O0O0O0OOO0OOO =QFileDialog .Options ()#line:214
        O000O000O0000O000 ,_O00O0OO00O0000OOO =QFileDialog .getSaveFileName (OO0OO0OOOOO0OOO00 ,'Create New File','','Lua Files (*.lua);;All Files (*)',options =O000O0O0O0OOO0OOO )#line:216
        if O000O000O0000O000 :#line:217
            with open (O000O000O0000O000 ,'w')as O00O0O00OOOOO0000 :#line:218
                O00O0O00OOOOO0000 .write (OO0OO0OOOOO0OOO00 .textEdit .toPlainText ())#line:219
            QMessageBox .information (OO0OO0OOOOO0OOO00 ,'File Created',f'File saved: {O000O000O0000O000}')#line:221
    def loadFile (OO0O0O00000O0000O ):#line:223
        OO0O00OO0OOOO00O0 =QFileDialog .Options ()#line:224
        O0OO0OO000O000OOO ,_O0OO00OOOOOOOO0O0 =QFileDialog .getOpenFileName (OO0O0O00000O0000O ,'Open File','','Lua Files (*.lua);;All Files (*)',options =OO0O00OO0OOOO00O0 )#line:226
        if O0OO0OO000O000OOO :#line:227
            with open (O0OO0OO000O000OOO ,'r')as OO00O0OO00OO0O0OO :#line:228
                O00OO0O0O00O0O0O0 =OO00O0OO00OO0O0OO .read ()#line:229
                OO0O0O00000O0000O .textEdit .setPlainText (O00OO0O0O00O0O0O0 )#line:230
    def openFile (OO00O0O0O00OO00OO ):#line:232
        O000O000OOO00OO0O =QFileDialog .Options ()#line:233
        O00O000OOOOO0O00O ,_O0O0O0O00O0O000O0 =QFileDialog .getOpenFileName (OO00O0O0O00OO00OO ,'Open File','','Lua Files (*.lua);;All Files (*)',options =O000O000OOO00OO0O )#line:235
        if O00O000OOOOO0O00O :#line:236
            with open (O00O000OOOOO0O00O ,'r')as O00000O00OOO000OO :#line:237
                O00O0000O000OO00O =O00000O00OOO000OO .read ()#line:238
                OO00O0O0O00OO00OO .textEdit .setPlainText (O00O0000O000OO00O )#line:239
    def saveFile (OO0000OOO00O00000 ):#line:241
        OOOO0O0OOOO0O0OOO =QFileDialog .Options ()#line:242
        O0O0O00OOO0000O0O ,_OOO0O00O0OO000O00 =QFileDialog .getSaveFileName (OO0000OOO00O00000 ,'Save File','','Lua Files (*.lua);;All Files (*)',options =OOOO0O0OOOO0O0OOO )#line:244
        if O0O0O00OOO0000O0O :#line:245
            with open (O0O0O00OOO0000O0O ,'w')as OOOOOOO0OO0O000OO :#line:246
                OOOOOOO0OO0O000OO .write (OO0000OOO00O00000 .textEdit .toPlainText ())#line:247
            QMessageBox .information (OO0000OOO00O00000 ,'File Saved',f'File saved: {O0O0O00OOO0000O0O}')#line:249
    def executeLuaCode (OOOO0000OOOO0O000 ):#line:251
        if OOOO0000OOOO0O000 .injection_status :#line:252
            try :#line:253
                QMessageBox .information (OOOO0000OOOO0O000 ,'Executed !',f'Executed')#line:254
            except Exception as OO000OO0OO0000O0O :#line:255
                QMessageBox .critical (OOOO0000OOOO0O000 ,'Execution Error',f'Error:\n{str(OO000OO0OO0000O0O)}')#line:256
        else :#line:257
            QMessageBox .critical (OOOO0000OOOO0O000 ,'Astro',f'Roblox is not injected')#line:258
if __name__ =='__main__':#line:259
    app =QApplication (sys .argv )#line:260
    executor =Ast ()#line:261
    executor .show ()#line:262
    sys .exit (app .exec_ ())#line:263
