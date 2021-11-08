from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget
import numpy as np
import matplotlib.pyplot as plt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1061, 744)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.total_label = QtWidgets.QLabel(Form)
        self.total_label.setObjectName("total_label")
        self.horizontalLayout.addWidget(self.total_label)
        self.total = QtWidgets.QLineEdit(Form)
        self.total.setObjectName("total")
        self.horizontalLayout.addWidget(self.total)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.probability_span_label_2 = QtWidgets.QLabel(Form)
        self.probability_span_label_2.setObjectName("probability_span_label_2")
        self.horizontalLayout_3.addWidget(self.probability_span_label_2)
        self.probability_span = QtWidgets.QLineEdit(Form)
        self.probability_span.setObjectName("probability_span")
        self.horizontalLayout_3.addWidget(self.probability_span)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setIcon(icon)
        self.button.setObjectName("button")
        self.horizontalLayout_4.addWidget(self.button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.MplWidget = MplWidget(Form)
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout.addWidget(self.MplWidget, 1, 1, 2, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Trigger Button
        self.button.clicked.connect(self.update_graph)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Coin Flip probability"))
        self.total_label.setText(_translate("Form", "Number of fliping"))
        self.total.setText(_translate("Form", "5000"))
        self.probability_span_label_2.setText(_translate("Form", "probability span"))
        self.probability_span.setText(_translate("Form", "100"))
        self.button.setText(_translate("Form", "Calculate!"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Created by Mohammad Torkaman Dehnavi</p><p>Email: mtorkaman69@gmail.com</p><p>Github: mohammaddehnavi</p></body></html>"))

    def update_graph(self):
        # Simulate Coin flips
        def flip_coin(N, p=0.5):
            prob = [p, (1 - p)]
            return np.random.choice(['H', 'T'], size=N, p=prob)

        # Simulated probability of flipping heads
        ph = 0.5

        # Number of heads to compute
        total = int(self.total.text())
        size = int(self.probability_span.text())

        # Sampling array to plot coin flips
        attempts = np.arange(size, total + size, size)

        # Simulate coin flips
        flips = flip_coin(total, ph)

        # Accumulate head frequencies
        results = [np.sum(flips[:idx] == 'H') / float(idx) for idx in attempts]

        # Compute y limits (how far above or below P(H) to display)
        yp = abs(max(results) - ph)
        yn = abs(min(results) - ph)
        y_delta = max(yp, yn)

        # Create canvas
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(attempts, results, 'o-', alpha=0.75, label='Simulation')
        self.MplWidget.canvas.axes.axhline(ph, 0, 1, color='r', alpha=0.75, label='Theory')
        self.MplWidget.canvas.axes.legend(fontsize=10)
        self.MplWidget.canvas.axes.set_title('Frequency P(Head)', fontsize=20)
        self.MplWidget.canvas.axes.set_xlabel('Number of Flips', fontsize=18)
        self.MplWidget.canvas.axes.set_ylabel('P(Head)', fontsize=18)
        self.MplWidget.canvas.axes.set_ylim(ph - y_delta, ph + y_delta)
        self.MplWidget.canvas.draw()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
