from dataclasses import dataclass
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QFile, QObject, Signal, Slot, SIGNAL, QThread
from PySide2.QtWidgets import QMessageBox
from nbtschematic import SchematicFile
from main_window import Ui_Dialog
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
import math, sys, threading, time
import block_rgb_definitions

'''
i l o v e e m i l i a
rem is cute too :3
'''


@dataclass
class Block:
    id: int
    state: int

    pos_x: int
    pos_y: int
    pos_z: int

# NOTE: THIS IS FOR MINECRAFT JAVA 1.12.2
# NOTE: if list has a value other than tuple, it is a block data
# save it using schematic.data[x,y,z] = <data>
data_cache = {}

data_cache_2 = {}


def get_distance(point1, point2):
    return math.hypot(point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2])


def match_closest_block_flat(rgb_pixel):
    dist_array_iter = []

    for id in block_rgb_definitions.block_id_to_rgb_color_flat:
        dist_array_iter.append((get_distance(rgb_pixel, block_rgb_definitions.block_id_to_rgb_color_flat[id]),
                                block_rgb_definitions.block_id_to_rgb_color_flat[id]))
    dist_array_iter.sort()
    return dist_array_iter[0][1]


def match_closest_block_flat_2(rgb_pixel):
    dist_array_iter = []

    for id in block_rgb_definitions.block_id_to_rgb_color_flat:
        dist_array_iter.append((get_distance(rgb_pixel, block_rgb_definitions.block_id_to_rgb_color_flat[id]),
                                id))

    dist_array_iter.sort()
    return dist_array_iter[0][1]


def match_closest_block_1(rgb_pixel):
    dist_array_iter = []

    for id in block_rgb_definitions.block_id_to_rgb_color_stair:
        dist_array_iter.append((get_distance(rgb_pixel, block_rgb_definitions.block_id_to_rgb_color_stair[id]), block_rgb_definitions.block_id_to_rgb_color_stair[id]))

    dist_array_iter.sort()
    return dist_array_iter[0][1]


def match_closest_block_2(rgb_pixel):
    dist_array_iter = []

    for id in block_rgb_definitions.block_id_to_rgb_color_stair:
        dist_array_iter.append((get_distance(rgb_pixel, block_rgb_definitions.block_id_to_rgb_color_stair[id]), id))

    dist_array_iter.sort()
    return dist_array_iter[0][1]


# sorry for the case confusion
class ImageToMinecraft(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(ImageToMinecraft, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.imageInputButton.clicked.connect(self.openFileExplorer_input)
        self.ui.outputButton.clicked.connect(self.openFileExplorer_output)

        self.ui.checkUseFlatBox.stateChanged.connect(self.setFlatFlag)

        self.ioFileSelected = 0
        self.inputSelect = 0
        self.outputSelect = 0

        self.useFlat = False

        self.currentImageFilename = ""
        self.currentOutputDir = ""

        self.ui.scale_LineEdit.textChanged.connect(self.setScale)

        self.ui.generateButton.clicked.connect(self.preGen)

        self.ui.generateButton.setDisabled(True)
        self.ui.imageInputButton.setDisabled(False)
        self.ui.outputButton.setDisabled(True)
        self.ui.checkUseFlatBox.setDisabled(True)
        self.ui.scale_LineEdit.setDisabled(True)
        self.ui.lineTextOutput.setDisabled(True)


        self.scale = 1.0

        self.ui.imageLabel.setScaledContents(True)

        # LMAO why fix things when you can just remove them XD
        # self.ui.progressBar.setValue(100)
        self.ui.barLabel.setText(f"")

        self.currentPreviewImageMCList = {}



        # Image

        self.show()

    def preGen(self):
        thread = threading.Thread(target=self.generateSchematic, args=(self.currentImageFilename, self.currentOutputDir, self.useFlat,))
        if thread.is_alive():
            print("yes")
        thread.start()
        # self.generateSchematic(self.currentImageFilename, self.currentOutputDir, self.useFlat)

    def setScale(self):
        try:
            self.scale = float(self.ui.scale_LineEdit.text())
            thread = threading.Thread(target=self.generatePreviewList, args=(self.currentImageFilename, True,))
            if thread.is_alive():
                thread.join()
            thread.start()
        except ValueError:
            self.scale = 1.0
            thread = threading.Thread(target=self.generatePreviewList, args=(self.currentImageFilename, True,))
            if thread.is_alive():
                thread.join()
            thread.start()

    def setFlatFlag(self):
        if self.ui.checkUseFlatBox.isChecked():
            self.useFlat = True
            thread = threading.Thread(target=self.generatePreviewList, args=(self.currentImageFilename, True,))
            if thread.is_alive():
                thread.join()
            thread.start()
        else:
            self.useFlat = False
            thread = threading.Thread(target=self.generatePreviewList, args=(self.currentImageFilename, False,))
            if thread.is_alive():
                thread.join()
            thread.start()

    def openFileExplorer_input(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.', filter='*.jpg')
        if str(filename) != '':
            self.ui.lineTextImageInput.setText(str(filename))
            self.currentImageFilename = str(filename)
            self.inputSelect = 1
            self.disableEnableAll(False)
            thread = threading.Thread(target=self.generatePreviewList, args=(filename,))
            if thread.is_alive():
                print("yes")
            thread.start()

    def openFileExplorer_output(self):
        fileDialog = QtWidgets.QFileDialog(self)
        filename, filer = fileDialog.getSaveFileName(parent=self, caption='Save As...', filter='*.schematic')
        self.ui.lineTextOutput.setText(str(filename))
        self.currentOutputDir = filename
        self.outputSelect = 1

    def generatePreviewList(self, imagePath, useFlat = False):
        imagePath = str(imagePath)

        with Image.open(imagePath) as preview_img:
            try:
                image_x, image_y = preview_img.size
                image_x = int(round(image_x * self.scale, 0))
                image_y = int(round(image_y * self.scale, 0))

                preview_img.thumbnail((image_x,image_y), Image.ANTIALIAS)
                image_x, image_y = preview_img.size
            except ZeroDivisionError:
                preview_img.close()
                sys.exit()
            self.currentPreviewImageMCList = list(preview_img.getdata())
            image_x, image_y = preview_img.size
            self.ui.barLabel.setText(f"Generating Preview...")
            if not useFlat:
                for i in range(len(self.currentPreviewImageMCList)):
                    self.ui.barLabel.setText(f"Generating Preview...{int(round((i/len(self.currentPreviewImageMCList))*100, 0))}%")
                    #self.ui.progressBar.setValue(int(round((i/len(self.currentPreviewImageMCList))*100, 0)))
                    self.currentPreviewImageMCList[i] = tuple(match_closest_block_1(self.currentPreviewImageMCList[i]))
            elif useFlat:
                for i in range(len(self.currentPreviewImageMCList)):
                    self.ui.barLabel.setText(f"Generating Preview...{int(round((i/len(self.currentPreviewImageMCList))*100, 0))}%")
                    #self.ui.progressBar.setValue(int(round((i/len(self.currentPreviewImageMCList))*100, 0)))
                    self.currentPreviewImageMCList[i] = tuple(match_closest_block_flat(self.currentPreviewImageMCList[i]))

            im2 = Image.new(preview_img.mode, preview_img.size)
            im2.putdata(self.currentPreviewImageMCList)
            self.ui.imageLabel.setScaledContents(True)
            self.ui.imageLabel_2.setPixmap(QtGui.QPixmap.fromImage(ImageQt(im2)))
            self.ui.imgOutSizeX.setText(f"X: {image_x}")
            self.ui.imgOutSizeY.setText(f"Y: {image_y}")
            self.ui.barLabel.setText(f"Done!")

        preview_img.close()

        sys.exit()

    def generateSchematic(self, imagePath, outputPath, useFlat=False):
        #self.ui.generateButton.setDisabled(True)
        imagePath = str(imagePath)
        outputPath = str(outputPath)

        # Turn all the Class Vars into Local Vars
        # To Ensure nothing changes during generation
        scale = self.scale
        # Generate a preview with
        # "Block ID"(Z,X,Y)
        # Then Fix Preview (normalize negative Y values)
        block_data = []

        with Image.open(imagePath) as process_img:
            self.ui.barLabel.setText("Processing...")
            try:
                image_x, image_y = process_img.size
                image_x = int(round(image_x * scale, 0))
                image_y = int(round(image_y * scale, 0))

                process_img.thumbnail((image_x,image_y), Image.ANTIALIAS)
            except:
                process_img.close()
                self.ui.barLabel.setText("ERROR")
                sys.exit()
            image_x, image_y = process_img.size
            sf_output = SchematicFile(shape=(image_y + 3, image_y + 3, image_x + 3))
            b_dat = []
            self.disableEnableAll(True)


            if useFlat:
                sf_output = SchematicFile(shape=(1, image_y +3, image_x+3))
                self.ui.barLabel.setText("Processing...")
                for x in range(image_x):
                    block_Obj = []
                    for y in range(image_y):
                        block_data.append(match_closest_block_flat_2(process_img.getpixel((x, y))))

                    y_val = 0
                    pc = 0
                    for i in block_data:
                        #print(i)
                        data = i.split(':')
                        if ":" in i:
                            block = Block(int(data[0]), int(data[1]), x, 0, y_val)
                            block_Obj.append(block)
                            y_val = y_val + 1
                            pc = pc + 1
                        else:
                            block = Block(int(data[0]), 0, x, 0, y_val)
                            block_Obj.append(block)
                            # print(f"Block y: {y_val}, data: {data[1]}\n")
                            y_val = y_val + 1
                            pc = pc + 1
                    a = 0
                    for blocks in block_Obj:
                        sf_output.blocks[0, blocks.pos_z, blocks.pos_x] = blocks.id
                        sf_output.data[0, blocks.pos_z, blocks.pos_x] = blocks.state
                        a = a + 1
                    block_data = []
                sf_output.save(outputPath)

            elif not useFlat:
                sf_output = SchematicFile(shape=(image_y +3, image_y+3, image_x+3))
                for x in range(image_x):
                    self.ui.barLabel.setText("Processing...")
                    block_Obj = []
                    y_counter = 1
                    for y in range(image_y):
                        block_data.append(match_closest_block_2(process_img.getpixel((x, y))))

                    y_val = 0
                    pc = 0
                    for i in block_data:
                        data = i.split(':')
                        if data[1] == "0":
                            y_counter = y_counter + int(data[2])
                            block = Block(int(data[0]), 0, x, y_counter, y_val)
                            block_Obj.append(block)
                            y_val = y_val + 1
                            pc = pc + 1
                        else:
                            y_counter = y_counter + int(data[2])
                            block = Block(int(data[0]), 0, x, y_counter, y_val)
                            block_Obj.append(block)
                            y_val = y_val + 1
                            pc = pc + 1
                    current_low = 0
                    a = 0
                    for blocks in block_Obj:
                        if blocks.pos_y < current_low:
                            current_low = blocks.pos_y
                        a = a+1
                    a = 0
                    for i in range(len(block_Obj)):
                        block_Obj[i].pos_y = block_Obj[i].pos_y + (current_low*-1) +1
                        a = a + 1
                    a = 0
                    for blocks in block_Obj:
                        assert sf_output.shape == (image_y +3, image_y+3, image_x+3)
                        sf_output.blocks[blocks.pos_y, blocks.pos_z, blocks.pos_x] = blocks.id
                        sf_output.data[blocks.pos_y, blocks.pos_z, blocks.pos_x] = blocks.state
                        a = a + 1
                    block_data = []
                # i want to fucking die
                # turns out the "bug" was me writing an empty file
                # because indentation
                sf_output.save(outputPath)
        #print(outputPath)
        process_img.close()
        self.ui.barLabel.setText("Done!")
        self.disableEnableAll(False)
        self.showInfoBox("Complete!","Processing Complete!")
        sys.exit()

    def updateBarLabel(self,text):
        self.ui.barLabel.setText(f"{text}")

    def updatePreview(self, imageObject):
        self.imageLabel_2.setPixmap(QtGui.QPixmap.fromImage(ImageQt(imageObject)))
        self.ui.imgOutSizeX.setText(f"X: {imageObject.size[0]}")
        self.ui.imgOutSizeY.setText(f"Y: {imageObject.size[1]}")

    def disableEnableAll(self,boolean=True):
        self.ui.generateButton.setDisabled(boolean)
        self.ui.imageInputButton.setDisabled(boolean)
        self.ui.outputButton.setDisabled(boolean)
        self.ui.checkUseFlatBox.setDisabled(boolean)
        self.ui.scale_LineEdit.setDisabled(boolean)
        self.ui.lineTextOutput.setDisabled(boolean)
        self.ui.lineTextImageInput.setDisabled(boolean)

    def showInfoBox(self,title,text):
        QtWidgets.QMessageBox.information(self, title, text)


# For some reason NBTSchematic does coords Y,Z,X
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = ImageToMinecraft()
    ex.show()
    sys.exit(app.exec_())


'''
block_data_and_pos = {}

with Image.open('test_data/images/SJtyuBUSG.jpg') as process_image:
    image_x, image_y = process_image.size
    b_dat = []
    print(f"image size x:{image_x}, y:{image_y}")
    sf_output = SchematicFile(shape=(image_y+3, image_y+3, image_x+3))
    file2 = open("log.txt", "w+")
    for x in range(image_x):
        y_counter = 1
        for y in range(image_y):
            assert sf_output.shape == (image_y+3, image_y+3, image_x+3)
            #print(f"Processing ({x}, {y})")
            file2.write(f"Processing ({x}, {y})\n")
            b_dat.append(match_closest_block(process_image.getpixel((x,y))))

            print(b_dat)
        print(len(b_dat))

        y_val = 0
        for i in b_dat:
            print(i)
            data = i.split(':')
            if data[1] == "0":
                y_counter = y_counter + int(data[2])
                sf_output.blocks[y_counter, y_val, x] = int(data[0])
                print(f"Block y: {y_val}\n")
                y_val = y_val + 1
                file2.write(f"Block y: {y_val}\nBlock ID: {data[0]}, Block State: {data[1]}, Block Elevation{data[2]}")
            else:
                y_counter = y_counter + int(data[2])
                sf_output.blocks[y_counter, y_val, x] = int(data[0])
                sf_output.data[y_counter, y_val, x] = int(data[1])
                print(f"Block y: {y_val}, data: {data[1]}\n")
                y_val = y_val + 1
                file2.write(f"Block y: {y_val}\nBlock ID: {data[0]}, Block State: {data[1]}, Block Elevation{data[2]}")

        b_dat = []
process_image.close()
sf_output.save('test_data/schematic/fuckyourichard.schematic')
file2.close()
'''


if __name__ == '__main__':
    main()