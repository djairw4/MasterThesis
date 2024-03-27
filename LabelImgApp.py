from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import Qt, QPoint, QRect, QDir
import sys, pathlib, os 
from LabelImgUi2 import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.img_w = self.label_image.width()
        self.img_h = self.label_image.height()
        self.rect_start, self.rect_end = QPoint(), QPoint()
        self.offset_x = -9
        self.offset_y = -32
        self.bounding_boxes = []
        self.directory = ".\\dataset\\detection"
        self.image_names = QDir(self.directory).entryList(["*.png", "*.jpg"])
        self.index = 0
        self.show_image()

        self.pushButton_next.clicked.connect(self.next_image)
        self.action_open_directory.triggered.connect(self.open_directory)
        self.action_open_directory.setShortcut("Ctrl+O")


    def open_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.directory = directory
            self.image_names = QDir(self.directory).entryList(["*.png", "*.jpg"])
            self.index = 0
            self.show_image()

    def show_image(self):
        if self.image_names:
            self.filepath = QDir(self.directory).filePath(self.image_names[self.index])
            self.pix = QPixmap(self.filepath)
            
            self.current_image_h = self.pix.height()
            self.current_image_w = self.pix.width()
            
            self.img_offset_x = 0
            self.img_offset_y = 0

            if self.current_image_w > self.current_image_h:
                self.scale = self.img_w / self.current_image_w
                self.img_offset_y = int((self.current_image_h * self.scale - self.img_h)/2)
            else:
                self.scale = self.img_h/self.current_image_h
                self.img_offset_x = int((self.current_image_w * self.scale - self.img_w)/2)

            self.pix = self.pix.scaled(self.img_w,self.img_h,Qt.AspectRatioMode.KeepAspectRatio)
            self.pix_clean = self.pix.copy()
            self.label_image.setPixmap(self.pix)
            self.label_imageName.setText(self.filepath)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.pix = self.pix_clean.copy()
            self.label_image.setPixmap(self.pix)
            self.bounding_boxes.clear()
		
    def paintEvent(self, event):
        self.pix_tmp = self.pix.copy()
        painter = QPainter(self.pix_tmp)
        if not self.rect_start.isNull() and not self.rect_end.isNull():
            rect = QRect(self.rect_start, self.rect_end)
            painter.drawRect(rect.normalized())
            self.label_image.setPixmap(self.pix_tmp)
        

    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.rect_start = event.pos() + QPoint(self.offset_x,self.offset_y) + QPoint(self.img_offset_x,self.img_offset_y)
            self.rect_end = self.rect_start
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:		
            self.rect_end = event.pos() + QPoint(self.offset_x,self.offset_y) + QPoint(self.img_offset_x,self.img_offset_y)
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() & Qt.MouseButton.LeftButton:
            rect = QRect(self.rect_start, self.rect_end)
            painter = QPainter(self.pix)
            self.bounding_boxes.append([self.rect_start.x() / (self.scale * self.current_image_w), 
                                        self.rect_start.y() / (self.scale * self.current_image_h), 
                                        self.rect_end.x() / (self.scale * self.current_image_w), 
                                        self.rect_end.y() / (self.scale * self.current_image_h)])
            print(self.bounding_boxes)
            painter.drawRect(rect.normalized()) 
            self.rect_start, self.rect_end = QPoint(), QPoint()
            self.update()

    def next_image(self):
        if self.bounding_boxes:
            file_path = os.path.join(self.directory,pathlib.Path(self.filepath).stem +".csv")
            print(file_path)
            with open(file_path, 'w') as file:
                for i in self.bounding_boxes:
                    file.write(str(i[0]) + "," + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]))
                    # print(i)
            self.bounding_boxes.clear()
        self.index = (self.index + 1) % len(self.image_names)
        self.show_image()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())