# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(775, 487)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HomeWindow.sizePolicy().hasHeightForWidth())
        HomeWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 50, 651, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(601, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.chord_relation_test_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chord_relation_test_button.setMinimumSize(QtCore.QSize(321, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chord_relation_test_button.setFont(font)
        self.chord_relation_test_button.setObjectName("chord_relation_test_button")
        self.gridLayout.addWidget(self.chord_relation_test_button, 1, 1, 1, 1)
        self.chord_id_test_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chord_id_test_button.setMinimumSize(QtCore.QSize(321, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chord_id_test_button.setFont(font)
        self.chord_id_test_button.setObjectName("chord_id_test_button")
        self.gridLayout.addWidget(self.chord_id_test_button, 0, 1, 1, 1)
        self.interval_test_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.interval_test_button.setMinimumSize(QtCore.QSize(322, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.interval_test_button.setFont(font)
        self.interval_test_button.setObjectName("interval_test_button")
        self.gridLayout.addWidget(self.interval_test_button, 0, 0, 1, 1)
        self.chord_degree_test_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chord_degree_test_button.setMinimumSize(QtCore.QSize(322, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chord_degree_test_button.setFont(font)
        self.chord_degree_test_button.setObjectName("chord_degree_test_button")
        self.gridLayout.addWidget(self.chord_degree_test_button, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.close_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")
        self.verticalLayout.addWidget(self.close_button, 0, QtCore.Qt.AlignHCenter)
        HomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 18))
        self.menubar.setObjectName("menubar")
        HomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "Home"))
        self.label.setText(_translate("HomeWindow", "Hello, select which test you want to do below"))
        self.chord_relation_test_button.setText(_translate("HomeWindow", "Chord Relation Test"))
        self.chord_id_test_button.setText(_translate("HomeWindow", "Chord Identification Test"))
        self.interval_test_button.setText(_translate("HomeWindow", "Interval Test"))
        self.chord_degree_test_button.setText(_translate("HomeWindow", "Chord Degree Test"))
        self.close_button.setText(_translate("HomeWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())
