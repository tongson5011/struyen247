from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMimeData

class CustomTreeView(QTreeView):
    def __init__(self, parent=None):
        super(CustomTreeView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QTreeView.InternalMove)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = [url.toLocalFile() for url in event.mimeData().urls()]
            destination_index = self.indexAt(event.pos())
            destination_path = self.model().filePath(destination_index)

            # Handle the drop action based on your requirements
            print(f"Drop {urls} to {destination_path}")

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        file_system_model = QFileSystemModel()
        file_system_model.setRootPath('/path/to/your/directory')

        tree_view = CustomTreeView()
        tree_view.setModel(file_system_model)
        tree_view.setRootIndex(file_system_model.index('/path/to/your/directory'))

        layout = QVBoxLayout(self)
        layout.addWidget(tree_view)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
