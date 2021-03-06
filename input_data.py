# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PIL import Image
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QMessageBox

from conf import ResolutionConf, WindowConf, GraphConf
from graph import Graph


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Generator Tool")
        MainWindow.resize(363, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 361, 357))
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.window_space_x_edit = QtWidgets.QLineEdit(self.frame)
        self.window_space_x_edit.setObjectName("window_space_x_edit")
        self.gridLayout_4.addWidget(self.window_space_x_edit, 5, 0, 1, 1)
        self.resolution_y_edit = QtWidgets.QLineEdit(self.frame)
        self.resolution_y_edit.setObjectName("resolution_y_edit")
        self.gridLayout_4.addWidget(self.resolution_y_edit, 2, 0, 1, 1)
        self.padding_y_label = QtWidgets.QLabel(self.frame)
        self.padding_y_label.setObjectName("padding_y_label")
        self.gridLayout_4.addWidget(self.padding_y_label, 12, 1, 1, 1)
        self.window_space_y_edit = QtWidgets.QLineEdit(self.frame)
        self.window_space_y_edit.setObjectName("window_space_y_edit")
        self.gridLayout_4.addWidget(self.window_space_y_edit, 6, 0, 1, 1)
        self.generator_button = QtWidgets.QPushButton(self.frame)
        self.generator_button.setObjectName("generator_button")
        self.generator_button.clicked.connect(self.clicked)
        self.gridLayout_4.addWidget(self.generator_button, 13, 0, 1, 2)
        self.unit_y_edit = QtWidgets.QLineEdit(self.frame)
        self.unit_y_edit.setObjectName("unit_y_edit")
        self.gridLayout_4.addWidget(self.unit_y_edit, 4, 0, 1, 1)
        self.unit_x_edit = QtWidgets.QLineEdit(self.frame)
        self.unit_x_edit.setObjectName("unit_x_edit")
        self.gridLayout_4.addWidget(self.unit_x_edit, 3, 0, 1, 1)
        self.resolution_y_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resolution_y_label.sizePolicy().hasHeightForWidth())
        self.resolution_y_label.setSizePolicy(sizePolicy)
        self.resolution_y_label.setMaximumSize(QtCore.QSize(111, 111))
        self.resolution_y_label.setObjectName("resolution_y_label")
        self.gridLayout_4.addWidget(self.resolution_y_label, 2, 1, 1, 1)
        self.padding_x_label = QtWidgets.QLabel(self.frame)
        self.padding_x_label.setObjectName("padding_x_label")
        self.gridLayout_4.addWidget(self.padding_x_label, 11, 1, 1, 1)
        self.padding_y_edit = QtWidgets.QLineEdit(self.frame)
        self.padding_y_edit.setObjectName("padding_y_edit")
        self.gridLayout_4.addWidget(self.padding_y_edit, 12, 0, 1, 1)
        self.unit_x_label = QtWidgets.QLabel(self.frame)
        self.unit_x_label.setObjectName("unit_x_label")
        self.gridLayout_4.addWidget(self.unit_x_label, 3, 1, 1, 1)
        self.window_x_num_edit = QtWidgets.QLineEdit(self.frame)
        self.window_x_num_edit.setObjectName("window_x_num_edit")
        self.gridLayout_4.addWidget(self.window_x_num_edit, 7, 0, 1, 1)
        self.window_x_num_label = QtWidgets.QLabel(self.frame)
        self.window_x_num_label.setObjectName("window_x_num_label")
        self.gridLayout_4.addWidget(self.window_x_num_label, 7, 1, 1, 1)
        self.window_x_size_edit = QtWidgets.QLineEdit(self.frame)
        self.window_x_size_edit.setObjectName("window_x_size_edit")
        self.gridLayout_4.addWidget(self.window_x_size_edit, 9, 0, 1, 1)
        self.padding_x_edit = QtWidgets.QLineEdit(self.frame)
        self.padding_x_edit.setObjectName("padding_x_edit")
        self.gridLayout_4.addWidget(self.padding_x_edit, 11, 0, 1, 1)
        self.window_y_size_edit = QtWidgets.QLineEdit(self.frame)
        self.window_y_size_edit.setObjectName("window_y_size_edit")
        self.gridLayout_4.addWidget(self.window_y_size_edit, 10, 0, 1, 1)
        self.window_y_num_label = QtWidgets.QLabel(self.frame)
        self.window_y_num_label.setObjectName("window_y_num_label")
        self.gridLayout_4.addWidget(self.window_y_num_label, 8, 1, 1, 1)
        self.unit_y_label = QtWidgets.QLabel(self.frame)
        self.unit_y_label.setObjectName("unit_y_label")
        self.gridLayout_4.addWidget(self.unit_y_label, 4, 1, 1, 1)
        self.window_space_y_label = QtWidgets.QLabel(self.frame)
        self.window_space_y_label.setObjectName("window_space_y_label")
        self.gridLayout_4.addWidget(self.window_space_y_label, 6, 1, 1, 1)
        self.window_y_size_label = QtWidgets.QLabel(self.frame)
        self.window_y_size_label.setObjectName("window_y_size_label")
        self.gridLayout_4.addWidget(self.window_y_size_label, 10, 1, 1, 1)
        self.window_x_size_label = QtWidgets.QLabel(self.frame)
        self.window_x_size_label.setObjectName("window_x_size_label")
        self.gridLayout_4.addWidget(self.window_x_size_label, 9, 1, 1, 1)
        self.window_y_num_edit = QtWidgets.QLineEdit(self.frame)
        self.window_y_num_edit.setObjectName("window_y_num_edit")
        self.gridLayout_4.addWidget(self.window_y_num_edit, 8, 0, 1, 1)
        self.window_space_x_label = QtWidgets.QLabel(self.frame)
        self.window_space_x_label.setObjectName("window_space_x_label")
        self.gridLayout_4.addWidget(self.window_space_x_label, 5, 1, 1, 1)
        self.resolution_x_edit = QtWidgets.QLineEdit(self.frame)
        self.resolution_x_edit.setObjectName("resolution_x_edit")
        self.gridLayout_4.addWidget(self.resolution_x_edit, 1, 0, 1, 1)
        self.resolution_x_label = QtWidgets.QLabel(self.frame)
        self.resolution_x_label.setObjectName("resolution_x_label")
        self.gridLayout_4.addWidget(self.resolution_x_label, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.set_validator()
        self.set_default_value()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.resolution_x_edit, self.resolution_y_edit)
        MainWindow.setTabOrder(self.resolution_y_edit, self.unit_x_edit)
        MainWindow.setTabOrder(self.unit_x_edit, self.unit_y_edit)
        MainWindow.setTabOrder(self.unit_y_edit, self.window_space_x_edit)
        MainWindow.setTabOrder(self.window_space_x_edit, self.window_space_y_edit)
        MainWindow.setTabOrder(self.window_space_y_edit, self.window_x_num_edit)
        MainWindow.setTabOrder(self.window_x_num_edit, self.window_y_num_edit)
        MainWindow.setTabOrder(self.window_y_num_edit, self.window_x_size_edit)
        MainWindow.setTabOrder(self.window_x_size_edit, self.window_y_size_edit)
        MainWindow.setTabOrder(self.window_y_size_edit, self.padding_x_edit)
        MainWindow.setTabOrder(self.padding_x_edit, self.padding_y_edit)
        MainWindow.setTabOrder(self.padding_y_edit, self.generator_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.padding_y_label.setText(_translate("MainWindow", "?????????????????????:mm"))
        self.generator_button.setText(_translate("MainWindow", "??????????????????"))
        self.resolution_y_label.setText(_translate("MainWindow", "????????????????????????DPI"))
        self.padding_x_label.setText(_translate("MainWindow", "????????????????????????mm"))
        self.unit_x_label.setText(_translate("MainWindow", "?????????um"))
        self.window_x_num_label.setText(_translate("MainWindow", "??????x??????"))
        self.window_y_num_label.setText(_translate("MainWindow", "??????y??????"))
        self.unit_y_label.setText(_translate("MainWindow", "?????????um"))
        self.window_space_y_label.setText(_translate("MainWindow", "Pitch????????????um"))
        self.window_y_size_label.setText(_translate("MainWindow", "????????????????????????um"))
        self.window_x_size_label.setText(_translate("MainWindow", "????????????????????????um"))
        self.window_space_x_label.setText(_translate("MainWindow", "Pitch????????????um"))
        self.resolution_x_label.setText(_translate("MainWindow", "????????????????????????DPI"))

    def set_default_value(self):
        self.resolution_x_edit.setText(str(1080.86))
        self.resolution_y_edit.setText(str(1441.13))
        self.unit_x_edit.setText(str(1))
        self.unit_y_edit.setText(str(1))
        self.window_space_x_edit.setText(str(1.5625))
        self.window_space_y_edit.setText(str(1.5625))
        self.window_x_num_edit.setText(str(108))
        self.window_y_num_edit.setText(str(96))
        self.window_x_size_edit.setText(str(0.72))
        self.window_y_size_edit.setText(str(0.41))
        self.padding_x_edit.setText(str(1))
        self.padding_y_edit.setText(str(1))

    def set_validator(self):
        double_validator = QDoubleValidator()
        double_validator.setBottom(0.01)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        double_validator.setDecimals(2)

        int_validator = QIntValidator()
        int_validator.setBottom(1)

        self.resolution_x_edit.setValidator(double_validator)
        self.resolution_y_edit.setValidator(double_validator)
        self.unit_x_edit.setValidator(int_validator)
        self.unit_y_edit.setValidator(int_validator)
        self.window_space_x_edit.setValidator(double_validator)
        self.window_space_y_edit.setValidator(double_validator)
        self.window_x_num_edit.setValidator(int_validator)
        self.window_y_num_edit.setValidator(int_validator)
        self.window_x_size_edit.setValidator(double_validator)
        self.window_y_size_edit.setValidator(double_validator)
        self.padding_x_edit.setValidator(double_validator)
        self.padding_y_edit.setValidator(double_validator)

    def clicked(self):
        # ???????????????????????????????????????
        self.generator_button.setEnabled(False)

        resolution_conf = ResolutionConf()
        resolution_conf.resolution_x = float(self.resolution_x_edit.text())
        resolution_conf.resolution_y = float(self.resolution_y_edit.text())

        window_conf = WindowConf()
        window_conf.window_size_x = float(self.window_x_size_edit.text())
        window_conf.window_size_y = float(self.window_y_size_edit.text())

        graph_conf = GraphConf()
        graph_conf.window_space_x = float(self.window_space_x_edit.text())
        graph_conf.window_space_y = float(self.window_space_y_edit.text())
        graph_conf.window_num_x = int(self.window_x_num_edit.text())
        graph_conf.window_num_y = int(self.window_y_num_edit.text())
        graph_conf.padding_x = int(self.padding_x_edit.text())
        graph_conf.padding_y = int(self.padding_y_edit.text())

        graph = Graph()
        graph.__str__()
        graph.write_base_graph()

        image_file = Image.open("base_pic.bmp")  # open colour image
        image_file = image_file.convert('1')  # convert image to black and white
        image_file.save('base_pic.bmp')

        msg_box = QMessageBox(QMessageBox.Information, "??????", "???????????????")
        msg_box.exec_()
        # ????????????????????????????????????
        self.generator_button.setEnabled(True)
