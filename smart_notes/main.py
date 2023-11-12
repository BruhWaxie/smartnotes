from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
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

app = QApplication([])
ex = NoteWindow()
ex.show()
app.exec_()
