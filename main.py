from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui import Ui_MainWindow

import json

class NoteWindow(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {}
        self.read_notes()
        self.connects()

    def connects(self):
        self.ui.notes_list.itemClicked.connect(self.show_note)        
        self.ui.newNote_btn.clicked.connect(self.add_note)
        self.ui.addNote_btn.clicked.connect(self.save_note)
        self.ui.deleteNote_btn.clicked.connect(self.del_note)

    def read_notes(self):
        try:
            with open('notes.json', 'r',encoding='utf-8') as file:
                self.notes = json.load(file)
        except:
            self.notes = {'Welcome to Smart Notes!':{
                'text': 'Add your first note.', 'tags':[]
            }}
        self.ui.notes_list.addItems(self.notes)


    def show_note(self):
        name = self.ui.notes_list.selectedItems()[0].text()

        self.ui.name_le.setText(name)

        self.ui.textEdit.setText(self.notes[name]['text'])
        self.ui.tags_list.clear()
        self.ui.tags_list.addItems(self.notes[name]['tags'])

    def add_note(self):
        self.ui.textEdit.clear()
        self.ui.tags_list.clear()
        self.ui.name_le.setText('New Note')

    def save_file(self):
        try:
            with open('notes.json', 'w', encoding='utf-8') as file:
                json.dump(self.notes, file, ensure_ascii=False)
        except:
            message = QMessageBox()
            message.setText("The file is dumb and don`t want to save him! That`s not our fault.")



    def save_note(self):
        title = self.ui.name_le.text()
        text = self.ui.textEdit.toPlainText()
        
        self.notes[title] = {'text' : text, 'tags' : []}
        self.save_file()
        self.ui.notes_list.clear()
        self.ui.notes_list.addItems(self.notes)

    def del_note(self):
        title = self.ui.name_le.text()
        if title in self.notes:
            del self.notes[title]
            self.ui.notes_list.clear()
            self.ui.notes_list.addItems(self.notes)
            self.save_file()
            self.add_note()



app = QApplication([])
ex = NoteWindow()
ex.show()
app.exec_()
