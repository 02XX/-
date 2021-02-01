# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Search(object):
    def setupUi(self, Search):
        if not Search.objectName():
            Search.setObjectName(u"Search")
        Search.resize(500, 500)
        Search.setMinimumSize(QSize(500, 500))
        Search.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(Search)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.q = QLineEdit(self.centralwidget)
        self.q.setObjectName(u"q")
        self.q.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.q.sizePolicy().hasHeightForWidth())
        self.q.setSizePolicy(sizePolicy)
        self.q.setMouseTracking(True)
        self.q.setFocusPolicy(Qt.StrongFocus)
        self.q.setContextMenuPolicy(Qt.NoContextMenu)
        self.q.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.q.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.q)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.search = QPushButton(self.centralwidget)
        self.search.setObjectName(u"search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        self.search.setFont(font1)
        self.search.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.search)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.question = QTextBrowser(self.centralwidget)
        self.question.setObjectName(u"question")
        self.question.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(18)
        font2.setBold(True)
        self.question.setFont(font2)
        self.question.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.question.setTabStopDistance(83.000000000000000)

        self.verticalLayout_3.addWidget(self.question)

        self.answer = QTextBrowser(self.centralwidget)
        self.answer.setObjectName(u"answer")
        font3 = QFont()
        font3.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font3.setPointSize(22)
        self.answer.setFont(font3)

        self.verticalLayout_3.addWidget(self.answer)

        Search.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Search)
        self.statusbar.setObjectName(u"statusbar")
        Search.setStatusBar(self.statusbar)

        self.retranslateUi(Search)

        QMetaObject.connectSlotsByName(Search)
    # setupUi

    def retranslateUi(self, Search):
        Search.setWindowTitle(QCoreApplication.translate("Search", u"\u641c\u9898\u795e\u5668", None))
        self.label.setText(QCoreApplication.translate("Search", u"\u95ee\u9898", None))
#if QT_CONFIG(statustip)
        self.q.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.q.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.q.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.q.setInputMask("")
        self.q.setText("")
        self.q.setPlaceholderText(QCoreApplication.translate("Search", u"\u8f93\u5165\u95ee\u9898", None))
        self.search.setText(QCoreApplication.translate("Search", u"\u67e5\u8be2", None))
        self.question.setHtml(QCoreApplication.translate("Search", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:18pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt; font-weight:400;\"><br /></p></body></html>", None))
    # retranslateUi

