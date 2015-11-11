# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facex_new_member.ui'
#
# Created: Wed Jun 24 05:24:01 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui, QtWebKit
import facex


class Ui_change_member_win(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_change_member_win, self).__init__()
        self.setupUi(self)
        self.captured_imgs = []

    def setupUi(self, change_member_win):
        change_member_win.setObjectName("change_member_win")
        change_member_win.resize(794, 600)
        change_member_win.setMinimumSize(QtCore.QSize(400, 499))
        change_member_win.setMaximumSize(QtCore.QSize(800, 900))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        change_member_win.setFont(font)
        self.centralwidget = QtGui.QWidget(change_member_win)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 751, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.browse_btn = QtGui.QPushButton(self.tab)
        self.browse_btn.setGeometry(QtCore.QRect(170, 20, 91, 21))
        self.browse_btn.setObjectName("browse_btn")
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.capture_btn = QtGui.QPushButton(self.tab)
        self.capture_btn.setObjectName("capture_btn")
        self.capture_btn.setGeometry(QtCore.QRect(300, 20, 118, 21))

        self.webview = QtWebKit.QWebView(self.tab)
        self.webview.setMaximumSize(700, 500)
        self.webview.setMinimumSize(700, 500)
        self.webview.setGeometry(QtCore.QRect(20, 65, 700, 500))

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 50, 51, 31))
        self.label.setObjectName("label")
        self.names_box = QtGui.QLineEdit(self.tab_2)
        self.names_box.setGeometry(QtCore.QRect(90, 50, 221, 31))
        self.names_box.setInputMask("")
        self.names_box.setMaxLength(50)
        self.names_box.setObjectName("names_box")
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 61, 31))
        self.label_2.setObjectName("label_2")
        self.id_number_box = QtGui.QLineEdit(self.tab_2)
        self.id_number_box.setGeometry(QtCore.QRect(90, 130, 221, 31))
        self.id_number_box.setInputMask("")
        self.id_number_box.setMaxLength(8)
        self.id_number_box.setObjectName("id_number_box")
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 71, 31))
        self.label_3.setObjectName("label_3")
        self.dept_box = QtGui.QLineEdit(self.tab_2)
        self.dept_box.setGeometry(QtCore.QRect(90, 210, 221, 31))
        self.dept_box.setInputMask("")
        self.dept_box.setMaxLength(30)
        self.dept_box.setObjectName("dept_box")
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 71, 31))
        self.label_4.setObjectName("label_4")
        self.position_box = QtGui.QLineEdit(self.tab_2)
        self.position_box.setGeometry(QtCore.QRect(90, 280, 221, 31))
        self.position_box.setInputMask("")
        self.position_box.setMaxLength(30)
        self.position_box.setObjectName("position_box")
        self.personal_info_error_field = QtGui.QLabel(self.tab_2)
        self.personal_info_error_field.setGeometry(QtCore.QRect(410, 50, 321, 71))
        self.personal_info_error_field.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.personal_info_error_field.setObjectName("personal_info_error_field")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.confirm_btn = QtGui.QPushButton(self.tab_3)
        self.confirm_btn.setGeometry(QtCore.QRect(260, 180, 151, 61))
        self.confirm_btn.setObjectName("confirm_btn")
        self.tabWidget.addTab(self.tab_3, "")
        change_member_win.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(change_member_win)
        self.statusbar.setObjectName("statusbar")
        change_member_win.setStatusBar(self.statusbar)

        self.retranslateUi(change_member_win)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(change_member_win)
        self.browse_btn.clicked.connect(lambda: self.open_file_dialog())
        self.confirm_btn.clicked.connect(lambda: self.confirm_changes())
        self.capture_btn.clicked.connect(lambda: self.capture_img())

    def retranslateUi(self, change_member_win):
        change_member_win.setWindowTitle(
            QtGui.QApplication.translate("change_member_win", "FaceX - Change Member", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.browse_btn.setText(
            QtGui.QApplication.translate("change_member_win", "Browse...", None, QtGui.QApplication.UnicodeUTF8))

        self.capture_btn.setText(
            QtGui.QApplication.translate("change_member_win", "Capture", None, QtGui.QApplication.UnicodeUTF8))

        self.comboBox.setItemText(0, QtGui.QApplication.translate("change_member_win", "New Member", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("change_member_win", "Modify Existing", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QtGui.QApplication.translate("change_member_win", "Images", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("change_member_win", "Names :", None, QtGui.QApplication.UnicodeUTF8))
        self.names_box.setPlaceholderText(
            QtGui.QApplication.translate("change_member_win", "Name at most 50 characters", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("change_member_win", "ID Number :", None, QtGui.QApplication.UnicodeUTF8))
        self.id_number_box.setPlaceholderText(
            QtGui.QApplication.translate("change_member_win", "ID Number at most 8 digits", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("change_member_win", "Department :", None, QtGui.QApplication.UnicodeUTF8))
        self.dept_box.setPlaceholderText(
            QtGui.QApplication.translate("change_member_win", "Department at most 30 characters", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("change_member_win", "Postion Title :", None, QtGui.QApplication.UnicodeUTF8))
        self.position_box.setPlaceholderText(
            QtGui.QApplication.translate("change_member_win", "Postion at most 30 characters", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.personal_info_error_field.setText(
            QtGui.QApplication.translate("change_member_win", "Fill Info as accurately as possible please..", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QtGui.QApplication.translate("change_member_win", "Personal Info", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.confirm_btn.setText(
            QtGui.QApplication.translate("change_member_win", "Confirm Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QtGui.QApplication.translate("change_member_win", "Confirm", None,
                                                               QtGui.QApplication.UnicodeUTF8))
        self.webview.load("webform/index.html")

    def open_file_dialog(self):
        chosen = QtGui.QFileDialog.getOpenFileNames(self, "Choose User Images", facex.util.system_user_dir,
                                                    u"Images(*.png;*.jpg;*.gif)")
        if len(chosen[0]) == 0:
            return

        self.add_imgs_to_js(chosen[0], face_factor=5)

    def capture_img(self):
        pic = facex.camera.capture_image()
        self.captured_imgs.append(pic)
        self.add_imgs_to_js(self.captured_imgs)

    def add_imgs_to_js(self, imgs, face_factor=1):
        back_slash = "%c" % 0x5c

        chosen_paths = []

        for elem in imgs:
            elem = elem.replace(back_slash, "/")
            faces = facex.neurals.get_faces(elem, face_factor)
            for face in faces:
                face = "'../" + face + "'"
                chosen_paths.append(face)

        js_str = ","
        js_paths_str = js_str.join(chosen_paths)

        if len(chosen_paths) > 0:
            js_paths = "addPaths([" + js_paths_str + "])"

        else:
            js_paths = "addPaths(0, 1)"

        webframe = self.webview.page().mainFrame()
        webframe.evaluateJavaScript(js_paths)

    def confirm_changes(self):
        webframe = self.webview.page().mainFrame()
        chosen = webframe.evaluateJavaScript('getPaths()')

        temp = []

        for x in chosen:
            # get rid of prefix ../temp.data/
            x = str(x)
            temp.append(str(x[13: len(x)]))

        final = facex.util.temp_to_permanent_face(temp)

        mod_type = self.comboBox.currentText()

        names = self.names_box.text()
        id_no = self.id_number_box.text()
        jdept = self.dept_box.text()
        jpos = self.position_box.text()

        id_no = str(id_no)
        id_no.strip()
        names = str(names)
        names.strip()
        jdept = str(jdept)
        jdept.strip()
        jpos = str(jpos)
        jpos.strip()

        if len(id_no) == 0:
            msg = QtGui.QMessageBox()
            msg.setWindowTitle("Error: ID Number needed")
            msg.setText("Please enter the ID Number of the target person")
            return

        if mod_type == "New Member":
            facex.control.add_member(names, id_no, jdept, jpos, final)
        else:
            if len(final) == 0:
                final = None

            facex.control.modify_member(names, id_no, jdept, jpos, final)

        self.close()