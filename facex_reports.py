# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../facex_reports.ui'
#
# Created: Thu Jun 04 14:31:25 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui, QtWebKit
import facex
import os


class Ui_facex_reports(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_facex_reports, self).__init__()
        self.setupUi(self)

    def setupUi(self, facex_reports):
        facex_reports.setObjectName("facex_reports")
        facex_reports.resize(800, 600)
        facex_reports.setMaximumSize(QtCore.QSize(850, 925))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        facex_reports.setFont(font)
        self.centralwidget = QtGui.QWidget(facex_reports)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 711, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label.setObjectName("label")
        self.dateEdit_from = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_from.setGeometry(QtCore.QRect(60, 30, 110, 22))
        self.dateEdit_from.setCalendarPopup(True)
        self.dateEdit_from.setObjectName("dateEdit_from")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 31, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit_to = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_to.setGeometry(QtCore.QRect(320, 30, 110, 22))
        self.dateEdit_to.setCalendarPopup(True)
        self.dateEdit_to.setObjectName("dateEdit_to")
        self.display_report_btn = QtGui.QPushButton(self.groupBox)
        self.display_report_btn.setGeometry(QtCore.QRect(200, 80, 111, 31))
        self.display_report_btn.setObjectName("display_report_btn")
        self.publish_error_field = QtGui.QLabel(self.groupBox)
        self.publish_error_field.setGeometry(QtCore.QRect(480, 30, 171, 31))
        self.publish_error_field.setText("")
        self.publish_error_field.setObjectName("publish_error_field")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 140, 711, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(560, 30, 81, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_publish = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_publish.setGeometry(QtCore.QRect(580, 60, 111, 22))
        self.comboBox_publish.setObjectName("comboBox_publish")
        self.comboBox_publish.addItem("")
        self.comboBox_publish.addItem("")
        self.publish_btn = QtGui.QPushButton(self.groupBox_2)
        self.publish_btn.setGeometry(QtCore.QRect(590, 100, 75, 31))
        self.publish_btn.setObjectName("publish_btn")
        self.scrollArea = QtGui.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 541, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.webview = QtWebKit.QWebView(self.scrollAreaWidgetContents)
        self.webview.setGeometry(QtCore.QRect(0, 0, 541, 361))
        self.webview.setObjectName("webview")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        facex_reports.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(facex_reports)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        facex_reports.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(facex_reports)
        self.statusbar.setObjectName("statusbar")
        facex_reports.setStatusBar(self.statusbar)

        self.webview.load("webform/reports.html")

        self.retranslateUi(facex_reports)
        QtCore.QMetaObject.connectSlotsByName(facex_reports)

        self.display_report_btn.clicked.connect(lambda: self.display_reports())
        self.publish_btn.clicked.connect(lambda: self.publish_reports())

    def retranslateUi(self, facex_reports):
        facex_reports.setWindowTitle(
            QtGui.QApplication.translate("facex_reports", "facex_reports", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(
            QtGui.QApplication.translate("facex_reports", "Pick Dates", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("facex_reports", "From :", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit_from.setDisplayFormat(
            QtGui.QApplication.translate("facex_reports", "d/M/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("facex_reports", "To :", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit_to.setDisplayFormat(
            QtGui.QApplication.translate("facex_reports", "d/M/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.display_report_btn.setText(
            QtGui.QApplication.translate("facex_reports", "Display Report", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(
            QtGui.QApplication.translate("facex_reports", "Report", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("facex_reports", "Publish Report :", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_publish.setItemText(0, QtGui.QApplication.translate("facex_reports", "Spreadsheet", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.comboBox_publish.setItemText(1, QtGui.QApplication.translate("facex_reports", "Word Document", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.publish_btn.setText(
            QtGui.QApplication.translate("facex_reports", "OK", None, QtGui.QApplication.UnicodeUTF8))

    def display_reports(self):
        d_from_raw = self.dateEdit_from.date()
        d_to_raw = self.dateEdit_to.date()

        d_from = d_from_raw.toString("dd/MM/yyyy")
        d_to = d_to_raw.toString("dd/MM/yyyy")

        s_from = facex.util.date_to_stamp(d_from)
        s_to = facex.util.date_to_stamp(d_to)

        data = facex.datacenter.get_access_reports(s_from, s_to)
        html = ""

        for report in data:
            html += "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (report["Date"], report["id_no"], report["Access"])

        webframe = self.webview.page().mainFrame()

        caption = "set_caption('FaceX System Reports for %s to %s')" % (d_from, d_to)
        cont = "add_table_contents(%s)" % html

        webframe.evaluateJavaScript(caption)
        webframe.evaluateJavaScript(cont)

    def publish_reports(self):
        d_from_raw = self.dateEdit_from.date()
        d_to_raw = self.dateEdit_to.date()

        d_from = d_from_raw.toString("dd/MM/yyyy")
        d_to = d_to_raw.toString("dd/MM/yyyy")

        doc = None

        if self.comboBox_publish.currentText() == "Spreadsheet":
            doc = facex.util.publish_xlsx_report(d_from, d_to)
        else:
            doc = facex.util.publish_docx_report(d_from, d_to)

        os.system("start "+doc)
