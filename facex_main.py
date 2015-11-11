# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../facex_main.ui'
#
# Created: Thu Jun 04 14:29:45 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import sys

from PySide import QtCore, QtGui, QtWebKit

import facex_new_member
import facex_reports
import facex_view_users
import atexit

import facex


class Ui_FaceX(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_FaceX, self).__init__()
        self.setupUi(self)
        atexit.register(facex.util.atexit)
        atexit.register(facex.datacenter.shutdown)
        atexit.register(facex.neurals.neural_save)
        facex.datacenter.bootup()
        facex.neurals.neural_start()
        self.captured_faces = list()

    def setupUi(self, FaceX):
        FaceX.setObjectName("FaceX")
        FaceX.resize(806, 587)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FaceX.sizePolicy().hasHeightForWidth())
        FaceX.setSizePolicy(sizePolicy)
        FaceX.setMinimumSize(QtCore.QSize(1, 1))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        FaceX.setFont(font)
        self.centralwidget = QtGui.QWidget(FaceX)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.captured_image_box = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captured_image_box.sizePolicy().hasHeightForWidth())
        self.captured_image_box.setSizePolicy(sizePolicy)
        self.captured_image_box.setMinimumSize(QtCore.QSize(280, 0))
        self.captured_image_box.setObjectName("captured_image_box")

        self.captured_img = QtWebKit.QWebView(self.captured_image_box)
        self.captured_img.setGeometry(QtCore.QRect(10, 16, 260, 280))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captured_img.sizePolicy().hasHeightForWidth())
        self.captured_img.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.captured_image_box, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.detected_faces_pane = QtWebKit.QWebView(self.groupBox_4)

        self.detected_faces_pane.setObjectName("detected_faces_pane")

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())

        self.detected_faces_pane.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.detected_faces_pane, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 2, 1)
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setMinimumSize(QtCore.QSize(0, 260))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setObjectName("groupBox_2")
        self.check_access_btn = QtGui.QPushButton(self.groupBox_2)
        self.check_access_btn.setGeometry(QtCore.QRect(20, 110, 91, 31))
        self.check_access_btn.setObjectName("check_access_btn")
        self.capture_btn = QtGui.QPushButton(self.groupBox_2)
        self.capture_btn.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.capture_btn.setObjectName("capture_btn")
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        FaceX.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FaceX)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        FaceX.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FaceX)
        self.statusbar.setObjectName("statusbar")
        FaceX.setStatusBar(self.statusbar)
        self.actionAdd_User = QtGui.QAction(FaceX)
        self.actionAdd_User.setObjectName("actionAdd_User")
        self.actionView_Users = QtGui.QAction(FaceX)
        self.actionView_Users.setObjectName("actionView_Users")
        self.actionExit = QtGui.QAction(FaceX)
        self.actionExit.setObjectName("actionExit")
        self.actionCapture = QtGui.QAction(FaceX)
        self.actionCapture.setObjectName("actionCapture")
        self.actionAccess_Reports = QtGui.QAction(FaceX)
        self.actionAccess_Reports.setObjectName("actionAccess_Reports")
        self.menuFile.addAction(self.actionAdd_User)
        self.menuFile.addAction(self.actionView_Users)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAccess_Reports)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(FaceX)
        QtCore.QMetaObject.connectSlotsByName(FaceX)

        self.captured_img.load("webform/capturedimage.html")
        self.detected_faces_pane.load("webform/detectedimages.html")

    def retranslateUi(self, FaceX):
        FaceX.setWindowTitle(QtGui.QApplication.translate("FaceX", "FaceX", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FaceX", "Image Box", None, QtGui.QApplication.UnicodeUTF8))
        self.captured_image_box.setTitle(QtGui.QApplication.translate("FaceX", "Captured Image", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("FaceX", "Detected Faces", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FaceX", "Button Box", None, QtGui.QApplication.UnicodeUTF8))
        self.check_access_btn.setText(QtGui.QApplication.translate("FaceX", "Check Access", None, QtGui.QApplication.UnicodeUTF8))
        self.capture_btn.setText(QtGui.QApplication.translate("FaceX", "Capture Image", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("FaceX", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_User.setText(QtGui.QApplication.translate("FaceX", "Edit Users", None, QtGui.QApplication.UnicodeUTF8))
        self.actionView_Users.setText(QtGui.QApplication.translate("FaceX", "View Users", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("FaceX", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCapture.setText(QtGui.QApplication.translate("FaceX", "Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAccess_Reports.setText(QtGui.QApplication.translate("FaceX", "Access Reports", None, QtGui.QApplication.UnicodeUTF8))

        # now link the signals
        self.actionAdd_User.triggered.connect(self.launch_change_member)
        self.actionAccess_Reports.triggered.connect(self.launch_reports)
        self.actionView_Users.triggered.connect(self.launch_view_users)
        self.actionExit.triggered.connect(self.close_app)
        self.capture_btn.clicked.connect(self.capture_img)
        self.check_access_btn.clicked.connect(self.check_access)

    def capture_img(self):
        img = facex.camera.capture_image()
        self.captured_faces = list()
        _img = "../%s" % img
        c_webframe = self.captured_img.page().mainFrame()
        x_webframe = self.detected_faces_pane.page().mainFrame()
        x_webframe.evaluateJavaScript("remove_faces()")
        c_js = "set_imgpath('%s')" % _img
        c_webframe.evaluateJavaScript(c_js)

        faces_paths = []
        faces = facex.neurals.get_faces(img)
        self.captured_faces.extend(faces)
        for face in faces:
            _face = "'../%s'" % face
            faces_paths.append(_face)

        comma = ","
        x_js_cmd = "add_faces([%s])" % comma.join(faces_paths)
        x_webframe.evaluateJavaScript(x_js_cmd)

    def check_access(self):
        access = False
        msgbox = QtGui.QMessageBox()
        msgbox.setWindowTitle("FaceX Access permission")

        for face in self.captured_faces:
            gate, uinfo = facex.control.anonymous_checkaccess(face)
            if gate is True:
                access = True
                break

        if access is False:
            msgbox.setText("ACCESS DENIED")
        else:
            text = "ACCESS GRANTED!<br><br>Welcome <strong>%s</strong><br>%s at %s" % \
                   (uinfo.names, uinfo.position, uinfo.department)

            msgbox.setText(text)

        msgbox.exec_()

    def launch_change_member(self):
        self.change_mem = facex_new_member.Ui_change_member_win()
        self.change_mem.show()

    def launch_view_users(self):
        self.view_mem = facex_view_users.Ui_facex_view_members()
        self.view_mem.show()

    def launch_reports(self):
        self.reps = facex_reports.Ui_facex_reports()
        self.reps.show()

    def close_app(self):
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    obj = Ui_FaceX()
    obj.show()
    sys.exit(app.exec_())

