# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../facex_view_users.ui'
#
# Created: Thu Jun 04 14:31:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui, QtWebKit
import os
import facex


class Ui_facex_view_members(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_facex_view_members, self).__init__()
        self.setupUi(self)

    def setupUi(self, facex_view_members):
        facex_view_members.setObjectName("facex_view_members")
        facex_view_members.resize(1100, 700)
        facex_view_members.setMaximumSize(QtCore.QSize(1100, 700))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        facex_view_members.setFont(font)
        self.centralwidget = QtGui.QWidget(facex_view_members)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 850, 700))
        self.groupBox.setMaximumSize(QtCore.QSize(880, 700))
        self.groupBox.setObjectName("groupBox")
        self.webform = QtWebKit.QWebView(self.groupBox)
        self.webform.setGeometry(QtCore.QRect(22, 33, 800, 680))
        self.webform.setMaximumSize(QtCore.QSize(800, 680))
        self.webform.setObjectName("webform")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(900, 40, 141, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.users_publish_combo = QtGui.QComboBox(self.groupBox_2)
        self.users_publish_combo.setGeometry(QtCore.QRect(10, 20, 121, 22))
        self.users_publish_combo.setObjectName("users_publish_combo")
        self.users_publish_combo.addItem("")
        self.users_publish_combo.addItem("")
        self.publish_users_ok = QtGui.QPushButton(self.groupBox_2)
        self.publish_users_ok.setGeometry(QtCore.QRect(50, 60, 41, 23))
        self.publish_users_ok.setObjectName("publish_users_ok")
        facex_view_members.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(facex_view_members)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 20))
        self.menubar.setObjectName("menubar")
        facex_view_members.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(facex_view_members)
        self.statusbar.setObjectName("statusbar")
        facex_view_members.setStatusBar(self.statusbar)

        self.webform.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)
        self.webform.linkClicked.connect(self.handle_link_click)

        self.webform.load("webform/allusers.html")
        self.webform.loadFinished.connect(self.get_user_list)

        self.retranslateUi(facex_view_members)
        QtCore.QMetaObject.connectSlotsByName(facex_view_members)

        self.publish_users_ok.clicked.connect(lambda: self.publish_list())

    def retranslateUi(self, facex_view_members):
        facex_view_members.setWindowTitle(QtGui.QApplication.translate("facex_view_members", "FaceX - View Users", None,
                                                                       QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(
            QtGui.QApplication.translate("facex_view_members", "Active Database", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(
            QtGui.QApplication.translate("facex_view_members", "Publish List", None, QtGui.QApplication.UnicodeUTF8))
        self.users_publish_combo.setItemText(0, QtGui.QApplication.translate("facex_view_members", "Spreadsheet", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.users_publish_combo.setItemText(1,
                                             QtGui.QApplication.translate("facex_view_members", "Word Document", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.publish_users_ok.setText(
            QtGui.QApplication.translate("facex_view_members", "OK", None, QtGui.QApplication.UnicodeUTF8))

    def get_user_list(self):
        user_list = facex.datacenter.get_allmembers()
        html = ""
        for user in user_list:
            html += "<tr class=\"%s\">" % str(user.id_no)
            html += "<td><center><img src=\"../" + user.pic + "\" "
            html += "width=\"40\" height=auto alt=\"not found\"></center></td>"
            html += "<td><center>%s</center></td><td><center>%s</center></td>" % (user.names, user.id_no)
            html += "<td><center>%s</center></td><td><center>%s</center></td>" % (user.department, user.position)
            html += "<td><a href=\"%s\" class=\"btn btn-danger btn-sm\"><span class=\"glyphicon glyphicon-trash\"></span>" \
                    "</a></td></tr>" % user.id_no

        js = "add_table_contents('%s')" % html
        webframe = self.webform.page().mainFrame()
        webframe.evaluateJavaScript(js)

    def handle_link_click(self, url):
        sep = url.toString()
        parts = sep.split("/")
        uid = parts[len(parts) - 1]
        facex.control.delete_member(id_no=uid)
        webframe = self.webform.page().mainFrame()
        js = "hide_deleted(%s)" % url.toString()
        webframe.evaluateJavaScript(js)

    def publish_list(self):

        doc = None

        if self.users_publish_combo.currentText() == "Spreadsheet":
            doc = facex.util.publish_xlsx_userlist()

        else:
            doc = facex.util.publish_docx_userlist()

        os.system("start " + doc)
