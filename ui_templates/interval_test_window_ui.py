# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interval_test_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IntervalTestWindow(object):
    def setupUi(self, IntervalTestWindow):
        IntervalTestWindow.setObjectName("IntervalTestWindow")
        IntervalTestWindow.setEnabled(True)
        IntervalTestWindow.resize(1324, 493)
        self.centralwidget = QtWidgets.QWidget(IntervalTestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, -30, 821, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(30, 90, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output_label.setFont(font)
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 140, 721, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.replay_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.replay_button.setFont(font)
        self.replay_button.setObjectName("replay_button")
        self.horizontalLayout_2.addWidget(self.replay_button)
        self.skip_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.skip_button.setFont(font)
        self.skip_button.setObjectName("skip_button")
        self.horizontalLayout_2.addWidget(self.skip_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.P8_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.P8_button.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.P8_button.setFont(font)
        self.P8_button.setObjectName("P8_button")
        self.interval_buttonGroup = QtWidgets.QButtonGroup(IntervalTestWindow)
        self.interval_buttonGroup.setObjectName("interval_buttonGroup")
        self.interval_buttonGroup.addButton(self.P8_button)
        self.gridLayout.addWidget(self.P8_button, 3, 5, 1, 1)
        self.m6_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.m6_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.m6_button.setFont(font)
        self.m6_button.setObjectName("m6_button")
        self.interval_buttonGroup.addButton(self.m6_button)
        self.gridLayout.addWidget(self.m6_button, 2, 5, 1, 1)
        self.M3_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.M3_button.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.M3_button.setFont(font)
        self.M3_button.setObjectName("M3_button")
        self.interval_buttonGroup.addButton(self.M3_button)
        self.gridLayout.addWidget(self.M3_button, 1, 5, 1, 1)
        self.M6_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.M6_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.M6_button.setFont(font)
        self.M6_button.setObjectName("M6_button")
        self.interval_buttonGroup.addButton(self.M6_button)
        self.gridLayout.addWidget(self.M6_button, 3, 2, 1, 1)
        self.TT_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.TT_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TT_button.setFont(font)
        self.TT_button.setObjectName("TT_button")
        self.interval_buttonGroup.addButton(self.TT_button)
        self.gridLayout.addWidget(self.TT_button, 2, 3, 1, 1)
        self.P5_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.P5_button.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.P5_button.setFont(font)
        self.P5_button.setObjectName("P5_button")
        self.interval_buttonGroup.addButton(self.P5_button)
        self.gridLayout.addWidget(self.P5_button, 2, 4, 1, 1)
        self.P4_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.P4_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.P4_button.setFont(font)
        self.P4_button.setObjectName("P4_button")
        self.interval_buttonGroup.addButton(self.P4_button)
        self.gridLayout.addWidget(self.P4_button, 2, 2, 1, 1)
        self.m2_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.m2_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.m2_button.setFont(font)
        self.m2_button.setObjectName("m2_button")
        self.interval_buttonGroup.addButton(self.m2_button)
        self.gridLayout.addWidget(self.m2_button, 1, 2, 1, 1)
        self.m7_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.m7_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.m7_button.setFont(font)
        self.m7_button.setObjectName("m7_button")
        self.interval_buttonGroup.addButton(self.m7_button)
        self.gridLayout.addWidget(self.m7_button, 3, 3, 1, 1)
        self.m3_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.m3_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.m3_button.setFont(font)
        self.m3_button.setObjectName("m3_button")
        self.interval_buttonGroup.addButton(self.m3_button)
        self.gridLayout.addWidget(self.m3_button, 1, 4, 1, 1)
        self.M2_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.M2_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.M2_button.setFont(font)
        self.M2_button.setObjectName("M2_button")
        self.interval_buttonGroup.addButton(self.M2_button)
        self.gridLayout.addWidget(self.M2_button, 1, 3, 1, 1)
        self.M7_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.M7_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.M7_button.setFont(font)
        self.M7_button.setObjectName("M7_button")
        self.interval_buttonGroup.addButton(self.M7_button)
        self.gridLayout.addWidget(self.M7_button, 3, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.score_label = QtWidgets.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(620, 80, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.score_label.setFont(font)
        self.score_label.setText("")
        self.score_label.setObjectName("score_label")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(920, 440, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close_button.setFont(font)
        self.close_button.setObjectName("close_button")
        self.select_all = QtWidgets.QCheckBox(self.centralwidget)
        self.select_all.setGeometry(QtCore.QRect(820, 70, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_all.setFont(font)
        self.select_all.setObjectName("select_all")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 0, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(820, 110, 431, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.select_all1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_all1.setFont(font)
        self.select_all1.setObjectName("select_all1")
        self.verticalLayout_2.addWidget(self.select_all1)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.buttonGroup1 = QtWidgets.QButtonGroup(IntervalTestWindow)
        self.buttonGroup1.setObjectName("buttonGroup1")
        self.buttonGroup1.setExclusive(False)
        self.buttonGroup1.addButton(self.checkBox)
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup1.addButton(self.checkBox_2)
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.buttonGroup1.addButton(self.checkBox_3)
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.buttonGroup1.addButton(self.checkBox_4)
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.buttonGroup1.addButton(self.checkBox_5)
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.buttonGroup1.addButton(self.checkBox_6)
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.select_all2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_all2.setFont(font)
        self.select_all2.setObjectName("select_all2")
        self.verticalLayout_3.addWidget(self.select_all2)
        self.checkBox_7 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.buttonGroup2 = QtWidgets.QButtonGroup(IntervalTestWindow)
        self.buttonGroup2.setObjectName("buttonGroup2")
        self.buttonGroup2.setExclusive(False)
        self.buttonGroup2.addButton(self.checkBox_7)
        self.verticalLayout_3.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.buttonGroup2.addButton(self.checkBox_8)
        self.verticalLayout_3.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.buttonGroup2.addButton(self.checkBox_9)
        self.verticalLayout_3.addWidget(self.checkBox_9)
        self.checkBox_10 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.buttonGroup2.addButton(self.checkBox_10)
        self.verticalLayout_3.addWidget(self.checkBox_10)
        self.checkBox_11 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.buttonGroup2.addButton(self.checkBox_11)
        self.verticalLayout_3.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.buttonGroup2.addButton(self.checkBox_12)
        self.verticalLayout_3.addWidget(self.checkBox_12)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        IntervalTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IntervalTestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1324, 18))
        self.menubar.setObjectName("menubar")
        IntervalTestWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IntervalTestWindow)
        self.statusbar.setObjectName("statusbar")
        IntervalTestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IntervalTestWindow)
        QtCore.QMetaObject.connectSlotsByName(IntervalTestWindow)

    def retranslateUi(self, IntervalTestWindow):
        _translate = QtCore.QCoreApplication.translate
        IntervalTestWindow.setWindowTitle(_translate("IntervalTestWindow", "Interval Test"))
        self.label.setText(_translate("IntervalTestWindow", "Select the interval you just heard"))
        self.replay_button.setText(_translate("IntervalTestWindow", "Replay Interval"))
        self.skip_button.setText(_translate("IntervalTestWindow", "Skip this Interval"))
        self.P8_button.setAccessibleName(_translate("IntervalTestWindow", "OCTAVE"))
        self.P8_button.setText(_translate("IntervalTestWindow", "Octave"))
        self.m6_button.setAccessibleName(_translate("IntervalTestWindow", "MINOR_6TH"))
        self.m6_button.setText(_translate("IntervalTestWindow", "Minor 6th"))
        self.M3_button.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_3RD"))
        self.M3_button.setText(_translate("IntervalTestWindow", "Major 3rd"))
        self.M6_button.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_6TH"))
        self.M6_button.setText(_translate("IntervalTestWindow", "Major 6th"))
        self.TT_button.setAccessibleName(_translate("IntervalTestWindow", "TRITONE"))
        self.TT_button.setText(_translate("IntervalTestWindow", "Tritone"))
        self.P5_button.setAccessibleName(_translate("IntervalTestWindow", "PERFECT_5TH"))
        self.P5_button.setText(_translate("IntervalTestWindow", "Perfect 5th"))
        self.P4_button.setAccessibleName(_translate("IntervalTestWindow", "PERFECT_4TH"))
        self.P4_button.setText(_translate("IntervalTestWindow", "Perfect 4th"))
        self.m2_button.setAccessibleName(_translate("IntervalTestWindow", "MINOR_2ND"))
        self.m2_button.setText(_translate("IntervalTestWindow", "Minor 2nd"))
        self.m7_button.setAccessibleName(_translate("IntervalTestWindow", "MINOR_7TH"))
        self.m7_button.setText(_translate("IntervalTestWindow", "Minor 7th"))
        self.m3_button.setAccessibleName(_translate("IntervalTestWindow", "MINOR_3RD"))
        self.m3_button.setText(_translate("IntervalTestWindow", "Minor 3rd"))
        self.M2_button.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_2ND"))
        self.M2_button.setText(_translate("IntervalTestWindow", "Major 2nd"))
        self.M7_button.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_7TH"))
        self.M7_button.setText(_translate("IntervalTestWindow", "Major 7th"))
        self.close_button.setText(_translate("IntervalTestWindow", "Close"))
        self.select_all.setText(_translate("IntervalTestWindow", "Select all intervals"))
        self.label_2.setText(_translate("IntervalTestWindow", "Select the intervals you would like to test"))
        self.select_all1.setText(_translate("IntervalTestWindow", "Select all below:"))
        self.checkBox.setAccessibleName(_translate("IntervalTestWindow", "MINOR_2ND"))
        self.checkBox.setText(_translate("IntervalTestWindow", "Minor 2nd"))
        self.checkBox_2.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_2ND"))
        self.checkBox_2.setText(_translate("IntervalTestWindow", "Major 2nd"))
        self.checkBox_3.setAccessibleName(_translate("IntervalTestWindow", "MINOR_3RD"))
        self.checkBox_3.setText(_translate("IntervalTestWindow", "Minor 3rd"))
        self.checkBox_4.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_3RD"))
        self.checkBox_4.setText(_translate("IntervalTestWindow", "Major 3rd"))
        self.checkBox_5.setAccessibleName(_translate("IntervalTestWindow", "PERFECT_4TH"))
        self.checkBox_5.setText(_translate("IntervalTestWindow", "Perfect 4th"))
        self.checkBox_6.setAccessibleName(_translate("IntervalTestWindow", "TRITONE"))
        self.checkBox_6.setText(_translate("IntervalTestWindow", "Tritone"))
        self.select_all2.setText(_translate("IntervalTestWindow", "Select all below:"))
        self.checkBox_7.setAccessibleName(_translate("IntervalTestWindow", "PERFECT_5TH"))
        self.checkBox_7.setText(_translate("IntervalTestWindow", "Perfect 5th"))
        self.checkBox_8.setAccessibleName(_translate("IntervalTestWindow", "MINOR_6TH"))
        self.checkBox_8.setText(_translate("IntervalTestWindow", "Minor 6th"))
        self.checkBox_9.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_6TH"))
        self.checkBox_9.setText(_translate("IntervalTestWindow", "Major 6th"))
        self.checkBox_10.setAccessibleName(_translate("IntervalTestWindow", "MINOR_7TH"))
        self.checkBox_10.setText(_translate("IntervalTestWindow", "Minor 7th"))
        self.checkBox_11.setAccessibleName(_translate("IntervalTestWindow", "MAJOR_7TH"))
        self.checkBox_11.setText(_translate("IntervalTestWindow", "Major 7th"))
        self.checkBox_12.setAccessibleName(_translate("IntervalTestWindow", "OCTAVE"))
        self.checkBox_12.setText(_translate("IntervalTestWindow", "Octave"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IntervalTestWindow = QtWidgets.QMainWindow()
    ui = Ui_IntervalTestWindow()
    ui.setupUi(IntervalTestWindow)
    IntervalTestWindow.show()
    sys.exit(app.exec_())
