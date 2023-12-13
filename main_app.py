from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QWidget, QFileSystemModel, QAbstractItemView, QMenu, QTreeView, QVBoxLayout, QFrame, QLabel, QSizePolicy, QSpacerItem, QHBoxLayout
from PySide6.QtCore import Qt,QFileSystemWatcher
from PySide6.QtGui import QCursor, QDragEnterEvent, QDropEvent, QKeyEvent, QAction
import shutil
import os
import sys
import send2trash

# path
PATH = os.path.dirname(os.path.abspath('__file__'))
os.chdir(PATH)
inputFolders = os.path.join(PATH, 'inputFolders')
outputAudio = os.path.join(PATH,'outputAudio')
imgFoders = os.path.join(PATH, 'imgFolders')
audioFolders = os.path.join(PATH, 'audioFolders')
outputMP4 = os.path.join(PATH, 'outputMP4')
baseIMG = os.path.join(PATH, r'base\inputIMG\baseIMG.png')
ffmpeg = os.path.join(PATH, 'base/ffmpeg/bin/ffmpeg')

os.makedirs(inputFolders, exist_ok=True)
os.makedirs(outputAudio, exist_ok=True)
os.makedirs(imgFoders, exist_ok=True)
os.makedirs(audioFolders, exist_ok=True)
os.makedirs(outputMP4, exist_ok=True)


class File_manager(QWidget):
    def __init__(self,name, path):
        super().__init__()
        # veriable 
        self.path = path
        self.name = name
        self.current_list = []

        self.is_rename = False 
        # add layout
        self.setupUi()
        # add model
        self.setupModel()
        # add menu
        self.setup_menu()
    
    #setup UI   
    def setupUi(self):
        # create layout
        self.verticalLayout = QVBoxLayout(self)
        # create tree view
        self.tree_view = QTreeView()
        
        
        self.frame = QFrame()
        self.frame_layout = QHBoxLayout(self.frame)
        # list label
        self.list_label = QLabel(self.name)
        # list count label
        self.list_count_label = QLabel('Count:')
        # list count
        self.list_count = QLabel()
        # 
        self.list_item_select_label = QLabel('select item')
        self.list_item_select = QLabel()
        
        # add label to widget
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # 
        self.frame_layout.addWidget(self.list_label)
        # 
        self.frame_layout.addItem(self.horizontalSpacer)
        # 
        self.frame_layout.addWidget(self.list_item_select)
        self.frame_layout.addWidget(self.list_item_select_label)
        # 
        self.frame_layout.addItem(self.horizontalSpacer)
        # 
        self.frame_layout.addWidget(self.list_count_label)
        self.frame_layout.addWidget(self.list_count)
        
        # add tree view and custom layout
        self.verticalLayout.addWidget(self.tree_view)
        self.verticalLayout.addWidget(self.frame,0, Qt.AlignVCenter)
        # style of label
        self.frame_layout.setContentsMargins(10,0,20,0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(0,0,0,0)
        self.verticalLayout.setSpacing(0)
    
    #setup model    
    def setupModel(self):
        # create model
        self.fileSystemModel = QFileSystemModel()
        self.fileSystemModel.setRootPath(self.path)
        self.tree_view.setModel(self.fileSystemModel)
        self.tree_view.setRootIndex(self.fileSystemModel.index(self.path))
        
        # sorted item
        self.tree_view.setSortingEnabled(True)
        self.fileSystemModel.sort(0, Qt.AscendingOrder)
        
        # hidden another column 
        self.tree_view.setColumnHidden(1,True)
        self.tree_view.setColumnHidden(2,True)
        self.tree_view.setColumnHidden(3,True)
        
        # select all, select custom
        self.tree_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tree_view.pressed.connect(self.handle_currentChange)
        # self.tree_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # show current item in folder
        self.fileSystemModel.rowsInserted.connect(lambda: self.list_count.setText(str(len(os.listdir(self.path)))))
        self.fileSystemModel.rowsRemoved.connect(lambda: self.list_count.setText(str(len(os.listdir(self.path)))))
        self.tree_view.selectionModel().selectionChanged.connect(self.handle_selection_changed)
     
    # setup menu
    def setup_menu(self):
        self.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.show_context_menu)
        
    # show context menu 
    def show_context_menu(self, pos):
        # Get the index under the cursor position
        index = self.tree_view.indexAt(pos)
        self.old_index = 0
        # If the index is valid, show a context menu
        # 
        if index.isValid():
            menu = QMenu()
            # Add a rename action to the context menu
            rename_action = QAction("Rename", self)
            delete_action = QAction('Delete', self)
            new_action = QAction('New', self)
            
            # 
            menu.addAction(new_action)
            menu.addAction(rename_action)
            menu.addAction(delete_action)
            
            # add delete action
            delete_action.triggered.connect(self.delete_item)
            new_action.triggered.connect(self.new_item)
            rename_action.triggered.connect(lambda: self.rename_item(index))
            
            # Show the context menu at the cursor position
            cursor = QCursor()
            menu.exec(cursor.pos())
        else:
            menu = QMenu()
            new_action = QAction('New', self)
            # 
            menu.addAction(new_action)
            new_action.triggered.connect(self.new_item)
            
            # Show the context menu at the cursor position
            cursor = QCursor()
            menu.exec(cursor.pos())     
    
    # remove elineEdit when click another item
    def handle_currentChange(self, e):
        self.current_select = []
        self.current_list.append(e)
        if self.is_rename and len(self.current_list) >=2:
            prev_index = self.current_list.pop(0)
            self.tree_view.setIndexWidget(prev_index, None)
        for item in self.tree_view.selectedIndexes():
            self.current_select.append(item.data(Qt.DisplayRole))
        self.list_item_select.setText(str(len(self.current_select)))
    
    # handle selection change
    def handle_selection_changed(self, selected, deselected):
        selected_indexes = selected.indexes()
        deselected_indexes = deselected.indexes()
        if self.is_rename and not selected_indexes:
            prev_index = self.current_list.pop(0)
            self.tree_view.setIndexWidget(prev_index, None)
            
    # delete item
    def delete_item(self):
        for item in self.tree_view.selectedIndexes():
            path_item =  os.path.join(self.path, item.data(Qt.DisplayRole))
            if os.path.isfile(path_item):
                send2trash.send2trash(path_item)
            else:
                send2trash.send2trash(path_item)
                
    # new item
    def new_item(self):
        rename_file = 'New Document.txt'
        count = 1
        while rename_file in os.listdir(self.path):
            rename_file = f'New Document({count}).txt'
            count +=1
        new_document = os.path.join(self.path, rename_file)
        with open(new_document, 'w', encoding='utf-8') as f:
            pass
        
    # rename item
    def rename_item(self, index):
        line_edit = QLineEdit()
        line_edit.setText(self.fileSystemModel.fileName(index))
        line_edit.selectAll()
        line_edit.returnPressed.connect(lambda: self.handle_rename(index, line_edit.text()))
        self.tree_view.setIndexWidget(index, line_edit)
        self.is_rename = True 

    def handle_rename(self,index, new_name):
        dir_path = self.fileSystemModel.filePath(index.parent())
        if new_name in os.listdir(dir_path):
            self.tree_view.setIndexWidget(index, None)
            return False
        old_name = self.fileSystemModel.fileName(index)
        old_path = os.path.join(dir_path, old_name)
        new_path = os.path.join(dir_path, new_name)
        os.rename(old_path, new_path)
        self.is_rename = False 
                    
    # key event
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == 67:
            list_text = ['la:///' + os.path.join(self.path, item.data(Qt.DisplayRole)) for item in self.list_item.selectedIndexes()]
            QApplication.clipboard().setText('\n'.join(list_text))
        if event.key() == 16777223:
            self.delete_item()
                
        if event.key() == 86:
            clipboards = QApplication.clipboard().text().split('\n')
                
            for clipboard in clipboards:
                if clipboard.startswith('file:///'):
                    old_file_path = clipboard[8:]
                    new_file_path = os.path.join(self.path, old_file_path.split('/')[-1])
                elif clipboard.startswith('la:///'):
                    old_file_path = clipboard[8:]
                    new_file_path = os.path.join(self.path, old_file_path.split('\\')[-1])
                if os.path.isfile(old_file_path):
                        shutil.copyfile(old_file_path,new_file_path)
                elif os.path.isdir(old_file_path):
                        shutil.copytree(old_file_path,new_file_path)
        return super().keyPressEvent(event)

            
class Main_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.path = inputFolders
        file_manager = File_manager(name='Input', path=self.path)
        self.resize(350,400)
        self.setCentralWidget(file_manager)


if __name__ == '__main__':
    app = QApplication([])
    window = Main_ui()
    window.show()
    app.exec()