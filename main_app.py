from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextEdit, QWidget, QFileSystemModel, QAbstractItemView, QMenu, QTreeView, QVBoxLayout, QFrame, QLabel, QSizePolicy, QSpacerItem, QHBoxLayout
from PySide6.QtCore import Qt,QFileSystemWatcher, QSize
from PySide6.QtGui import QCursor, QDragEnterEvent, QDropEvent, QKeyEvent, QAction
# 
from src.ui.main_ui import Ui_MainWindow
# 
import shutil
import os
import sys
import send2trash
from concurrent.futures import ThreadPoolExecutor

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
        self.setStyleSheet(u'file_namager')
        # veriable 
        self.path = path
        self.name = name
        self.current_list = []
        self.is_rename = False 
        self.list_item_selected = 0
        
        self.setMinimumSize(QSize(200,300))

        
        # add layout
        self.setupUi()
        # add model
        self.setupModel()
        # add menu
        self.setup_menu()
        
        # add stylesheet
        self.setStyleSheet('''
            * {
                background-color: #000;
            }
            #file_namager {
                background-color: #000;
            }
            QTreeView {
                background-color: #191919; /* Set the background color */
                color: #d7ffff;
                alternate-background-color: #ddd; /* Set the alternate row color */
                margin-right: -1px;
            }
            QTreeView::item {
                padding: 0px; /* Set padding for each item */
            }
            QTreeView::item:hover {
                background-color: #333; /* Set the background color for selected items */
                color: #d7ffff; /* Set the text color for selected items */
            }
            QTreeView::item:selected {
                background-color: #444; /* Set the background color for selected items */
                color: #d7ffff; /* Set the text color for selected items */
            }
            QHeaderView::section {
                background-color: #29292d;
                color: #fff;
                font-size: 12px;
                text-align: center;
                font-weight: bold;
                margin-right: -1px;
            }
            #list_frame {
                background-color: #333333;
                color: #fff;
            }
            QLabel{ 
               color: #fff;
               background-color: #333333; 
            }
            /* custom vertical bar*/
            QScrollBar:vertical {
                background-color: #000; 
                width: 8px; 
                margin: 0px 0px 0px 0px; 
            }
            QScrollBar::handle:vertical {
                border-radius: 4px;
                background: #515050; 
            }
            QScrollBar::handle:vertical:hover {
                border-radius: 4px;
                background: #4d4d4d; 
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background-color: #191919;
            }
            
            /* custom horizontal */
            QScrollBar:horizontal {
                background: #000;
                height: 8px; 
                margin: 0px 0px 0px 0px; 
            }
            QScrollBar::handle:horizontal {
                border-radius: 4px;
                background: #515050; 
            }
            QScrollBar::handle:horizontal:hover {
                border-radius: 4px;
                background: #4d4d4d; 
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                background: #191919; 
            }
        ''')
        
        
    
    #setup UI   
    def setupUi(self):
        # create layout
        self.verticalLayout = QVBoxLayout(self)
        # create tree view
        self.tree_view = QTreeView(self)
        self.tree_view.setAcceptDrops(True)
        self.tree_view.setDragEnabled(True)
        self.tree_view.setDragDropMode(QTreeView.InternalMove)
        
        self.tree_view.dragEnterEvent = self.tree_dragEnterEvent
        self.tree_view.dragMoveEvent = self.tree_dragMoveEvent
        self.tree_view.dropEvent = self.tree_dropEvent
        
        # create frame
        self.frame = QFrame()
        self.frame_layout = QHBoxLayout(self.frame)
        self.frame.setObjectName(u"list_frame")        
        
        # list label
        self.list_label = QLabel(self.name)
        # list count label
        self.list_count_label = QLabel('Count:')
        # list count
        self.list_count = QLabel()
        # 
        self.list_item_select_label = QLabel('')
        self.list_item_select = QLabel()
        
        # add label to widget
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # 
        self.frame_layout.addWidget(self.list_label,0, Qt.AlignVCenter)
        # 
        self.frame_layout.addItem(self.horizontalSpacer)
        # 
        self.frame_layout.addWidget(self.list_item_select,0, Qt.AlignVCenter)
        self.frame_layout.addWidget(self.list_item_select_label,0, Qt.AlignVCenter)
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
        
        # đouble click file
        self.tree_view.doubleClicked.connect(lambda index: os.startfile(self.fileSystemModel.filePath(index)))
        
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
            copy_action = QAction('Copy     Ctrl+C', self)
            paste_action = QAction('Paste   Ctrl+V', self)
            
            
            # 
            menu.addAction(new_action)
            menu.addAction(rename_action)
            menu.addAction(delete_action)
            menu.addAction(copy_action)
            menu.addAction(paste_action)
            
            
            # add delete action
            delete_action.triggered.connect(self.delete_item)
            new_action.triggered.connect(self.new_item)
            rename_action.triggered.connect(lambda: self.rename_item(index))
            copy_action.triggered.connect(self.copy_item)
            paste_action.triggered.connect(self.paste_item)
            
            
            # Show the context menu at the cursor position
            cursor = QCursor()
            menu.exec(cursor.pos())
        else:
            menu = QMenu()
            new_action = QAction('New', self)
            paste_action = QAction('Paste   Ctrl+V', self)
            # 
            menu.addAction(new_action)
            menu.addAction(paste_action)
            
            new_action.triggered.connect(self.new_item)
            paste_action.triggered.connect(self.paste_item)
            
            
            # Show the context menu at the cursor position
            cursor = QCursor()
            menu.exec(cursor.pos())     
    
    # remove elineEdit when click another item
    def handle_currentChange(self, e):
        self.current_select = []
        self.current_list.append(e)
        if len(self.current_list) >=2:
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
        if selected_indexes:
            self.list_item_selected += (int(len(selected_indexes))/4)
        if deselected_indexes:
           self.list_item_selected -= (int(len(deselected_indexes))/4)
        if self.list_item_selected > 0:
            self.list_item_select_label.setText('Selected')
            self.list_item_select.setText(str(int(self.list_item_selected)))
        else:
            self.list_item_select_label.setText('')
            self.list_item_select.setText('')
                    
    # delete item
    def delete_item(self):
        list_process = []
        with ThreadPoolExecutor(3) as executor:
            for item in self.tree_view.selectedIndexes():
                process = executor.submit(self.handle_delete_item, *[item])
                list_process.append(process)
    
    def handle_delete_item(self, item):
        path_item =  os.path.join(self.path, item.data(Qt.DisplayRole))
        print(path_item)
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
        line_edit.setStyleSheet('''background-color: #515050;color: #d7ffff;border: 1px solid #ccc''')
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
    
    # copy item
    def copy_item(self):
        list_text = ['lo:///' + os.path.join(self.path, item.data(Qt.DisplayRole)) for item in self.tree_view.selectedIndexes()]
        QApplication.clipboard().setText('\n'.join(list_text))
    
    # paste item
    def paste_item(self):
        list_process = []
        clipboards = QApplication.clipboard().text().split('\n')
        with ThreadPoolExecutor(3) as executor:
            for clipboard in clipboards:
                process = executor.submit(self.handle_paste_item, *[clipboard])
                list_process.append(process)
            
    def handle_paste_item(self, clipboard):
        old_file_path = ''
        try:
            print(clipboard)
            if clipboard.startswith('file:///'):
                old_file_path = clipboard[8:]
                new_file_path = os.path.join(self.path, old_file_path.split('/')[-1])
            elif clipboard.startswith('lo:///'):
                old_file_path = clipboard[8:]
                new_file_path = os.path.join(self.path, old_file_path.split('\\')[-1])
            if os.path.isfile(old_file_path):
                    shutil.copyfile(old_file_path,new_file_path)
            elif os.path.isdir(old_file_path):
                    shutil.copytree(old_file_path,new_file_path)
        except Exception as message:
            print(message)
            return False
             
    # key event
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == 67:
            self.copy_item()
        if event.key() == 16777223:
            self.delete_item()
                
        if event.key() == 86:
            self.paste_item()
        return super().keyPressEvent(event)
    
    # 
    def tree_dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def tree_dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def tree_dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = [url.toLocalFile() for url in event.mimeData().urls()]

            # Handle the drop action based on your requirements
            if urls:
                for url in urls:
                    print(url.split('/')[-1])
                    if url.split('/')[-1] in os.listdir(self.path):
                        print('exist')
                        shutil.copy(url, self.path)
                    else:
                        shutil.copy(url, self.path)
            print(f"Drop {urls} to {self.path}")
            
class Main_ui(QMainWindow,Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet('''
            #MainWindow {
                background-color: #000;
                color: #adaaaa;
            }
            QMenuBar { 
                background-color: #191919;
                color: #aaa;
            }
            QMenuBar::item:selected { 
                background-color: #101010;
                color: #1b75d0;
            }
            QMenu { 
                background-color: #191919;
                color: #aaa;
            }
            QMenu::item:selected { 
                background-color: 101010; 
                color: #ccc; 
                border: 1px solid #1b75d0;
            }
            QLabel { 
                color: #adaaaa; 
            }
            QLineEdit {
                background-color: #101010;
                color: #aaa;
                border: 1px solid gray;
            }
            QLineEdit:hover, QLineEdit:focus {
                border: 1px solid #1b75d0;
            }
            QPushButton {
                background-color: #101010;
                color: #aaa;
                border-radius: 4px;
            }
            QPushButton:hover, QPushButton:focus {
               background-color: #303030;
               border: 1px solid #1b75d0;
               outline: blue;
            }
            QCheckBox {
                background-color: #303030;
            }
            #header_frame_c {
                border: 1px solid #ccc;
            }
        ''') 
        self.input_path = inputFolders
        self.output_path = outputAudio
        self.img_path = imgFoders
        self.audio_path = audioFolders
        self.vid_path = outputMP4
        # 
        self.input_folder = File_manager(name='Input', path=self.input_path)
        self.output_folder = File_manager(name='Output', path=self.output_path)
        self.img_folder = File_manager(name='Img', path=self.img_path)
        self.audio_folder = File_manager(name='Aduio', path=self.audio_path)
        self.vid_folder = File_manager(name='Vid', path=self.vid_path)
        
        self.content_layout.setSpacing(6)
        self.content_layout.addWidget(self.input_folder)
        self.content_layout.addWidget(self.output_folder)
        self.content_layout.addWidget(self.img_folder)
        self.content_layout.addWidget(self.audio_folder)
        self.content_layout.addWidget(self.vid_folder)
    
        

if __name__ == '__main__':
    app = QApplication([])
    window = Main_ui()
    window.show()
    app.exec()