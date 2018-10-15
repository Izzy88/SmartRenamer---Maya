# -*- coding: utf-8 -*-

from PySide2 import QtWidgets, QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 613)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(500, 622))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 378, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_main.setContentsMargins(5, 10, 5, 5)
        self.layout_main.setObjectName("layout_main")
        self.layout_mesh_name = QtWidgets.QHBoxLayout()
        self.layout_mesh_name.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_mesh_name.setObjectName("layout_mesh_name")
        self.label_object_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_object_name.sizePolicy().hasHeightForWidth())
        self.label_object_name.setSizePolicy(sizePolicy)
        self.label_object_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_object_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_object_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_object_name.setWordWrap(False)
        self.label_object_name.setObjectName("label_object_name")
        self.layout_mesh_name.addWidget(self.label_object_name)
        self.edit_object_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_object_name.sizePolicy().hasHeightForWidth())
        self.edit_object_name.setSizePolicy(sizePolicy)
        self.edit_object_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_object_name.setObjectName("edit_object_name")
        self.layout_mesh_name.addWidget(self.edit_object_name)
        self.layout_main.addLayout(self.layout_mesh_name)
        self.btn_create_hierarchy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_create_hierarchy.setEnabled(True)
        self.btn_create_hierarchy.setObjectName("btn_create_hierarchy")
        self.layout_main.addWidget(self.btn_create_hierarchy)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layout_main.addWidget(self.line_3)
        self.layout_radio_btn = QtWidgets.QHBoxLayout()
        self.layout_radio_btn.setObjectName("layout_radio_btn")
        self.label_type = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_type.sizePolicy().hasHeightForWidth())
        self.label_type.setSizePolicy(sizePolicy)
        self.label_type.setObjectName("label_type")
        self.layout_radio_btn.addWidget(self.label_type)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.layout_radio_btn.addWidget(self.radioButton_2)
        self.radio_btn_jnt = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_btn_jnt.sizePolicy().hasHeightForWidth())
        self.radio_btn_jnt.setSizePolicy(sizePolicy)
        self.radio_btn_jnt.setObjectName("radio_btn_jnt")
        self.layout_radio_btn.addWidget(self.radio_btn_jnt)
        self.radio_btn_ctrl = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_btn_ctrl.sizePolicy().hasHeightForWidth())
        self.radio_btn_ctrl.setSizePolicy(sizePolicy)
        self.radio_btn_ctrl.setObjectName("radio_btn_ctrl")
        self.layout_radio_btn.addWidget(self.radio_btn_ctrl)
        self.layout_main.addLayout(self.layout_radio_btn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radio_btn_grp = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_btn_grp.setObjectName("radio_btn_grp")
        self.horizontalLayout_2.addWidget(self.radio_btn_grp)
        self.radio_btn_aim = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_btn_aim.setObjectName("radio_btn_aim")
        self.horizontalLayout_2.addWidget(self.radio_btn_aim)
        self.radio_btn_spline = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_btn_spline.setObjectName("radio_btn_spline")
        self.horizontalLayout_2.addWidget(self.radio_btn_spline)
        self.radio_btn_clust = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_btn_clust.setObjectName("radio_btn_clust")
        self.horizontalLayout_2.addWidget(self.radio_btn_clust)
        self.layout_main.addLayout(self.horizontalLayout_2)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.layout_main.addWidget(self.line_4)
        self.layout_combo_box = QtWidgets.QHBoxLayout()
        self.layout_combo_box.setObjectName("layout_combo_box")
        self.label_side = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_side.sizePolicy().hasHeightForWidth())
        self.label_side.setSizePolicy(sizePolicy)
        self.label_side.setObjectName("label_side")
        self.layout_combo_box.addWidget(self.label_side)
        self.com_box_side = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_box_side.sizePolicy().hasHeightForWidth())
        self.com_box_side.setSizePolicy(sizePolicy)
        self.com_box_side.setObjectName("com_box_side")
        self.com_box_side.addItem("")
        self.com_box_side.addItem("")
        self.com_box_side.addItem("")
        self.layout_combo_box.addWidget(self.com_box_side)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.layout_combo_box.addItem(spacerItem)
        self.label_kinematic = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_kinematic.sizePolicy().hasHeightForWidth())
        self.label_kinematic.setSizePolicy(sizePolicy)
        self.label_kinematic.setObjectName("label_kinematic")
        self.layout_combo_box.addWidget(self.label_kinematic)
        self.com_box_kinematic = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_box_kinematic.sizePolicy().hasHeightForWidth())
        self.com_box_kinematic.setSizePolicy(sizePolicy)
        self.com_box_kinematic.setObjectName("com_box_kinematic")
        self.com_box_kinematic.addItem("")
        self.com_box_kinematic.addItem("")
        self.com_box_kinematic.addItem("")
        self.layout_combo_box.addWidget(self.com_box_kinematic)
        self.layout_main.addLayout(self.layout_combo_box)
        self.layout_line_1 = QtWidgets.QHBoxLayout()
        self.layout_line_1.setObjectName("layout_line_1")
        self.layout_main.addLayout(self.layout_line_1)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layout_main.addWidget(self.line)
        self.layout_custom_name = QtWidgets.QHBoxLayout()
        self.layout_custom_name.setObjectName("layout_custom_name")
        self.label_custom_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_custom_name.sizePolicy().hasHeightForWidth())
        self.label_custom_name.setSizePolicy(sizePolicy)
        self.label_custom_name.setObjectName("label_custom_name")
        self.layout_custom_name.addWidget(self.label_custom_name)
        self.edit_pers_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_pers_name.sizePolicy().hasHeightForWidth())
        self.edit_pers_name.setSizePolicy(sizePolicy)
        self.edit_pers_name.setObjectName("edit_pers_name")
        self.layout_custom_name.addWidget(self.edit_pers_name)
        self.btn_apply = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_apply.sizePolicy().hasHeightForWidth())
        self.btn_apply.setSizePolicy(sizePolicy)
        self.btn_apply.setObjectName("btn_apply")
        self.layout_custom_name.addWidget(self.btn_apply)
        self.layout_main.addLayout(self.layout_custom_name)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layout_main.addWidget(self.line_2)
        self.tab_body_parts = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tab_body_parts.setObjectName("tab_body_parts")
        self.Spine = QtWidgets.QWidget()
        self.Spine.setObjectName("Spine")
        self.label_spine = QtWidgets.QLabel(self.Spine)
        self.label_spine.setGeometry(QtCore.QRect(0, 10, 341, 291))
        self.label_spine.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spine.setObjectName("label_spine")
        self.btn_root = QtWidgets.QPushButton(self.Spine)
        self.btn_root.setGeometry(QtCore.QRect(150, 260, 93, 28))
        self.btn_root.setObjectName("btn_root")
        self.btn_spine = QtWidgets.QPushButton(self.Spine)
        self.btn_spine.setGeometry(QtCore.QRect(210, 200, 93, 28))
        self.btn_spine.setObjectName("btn_spine")
        self.btn_neck = QtWidgets.QPushButton(self.Spine)
        self.btn_neck.setGeometry(QtCore.QRect(210, 110, 93, 28))
        self.btn_neck.setObjectName("btn_neck")
        self.btn_jaw = QtWidgets.QPushButton(self.Spine)
        self.btn_jaw.setGeometry(QtCore.QRect(80, 80, 93, 28))
        self.btn_jaw.setObjectName("btn_jaw")
        self.btn_head = QtWidgets.QPushButton(self.Spine)
        self.btn_head.setGeometry(QtCore.QRect(150, 30, 93, 28))
        self.btn_head.setObjectName("btn_head")
        self.tab_body_parts.addTab(self.Spine, "")
        self.Arms = QtWidgets.QWidget()
        self.Arms.setObjectName("Arms")
        self.label_arm = QtWidgets.QLabel(self.Arms)
        self.label_arm.setGeometry(QtCore.QRect(50, 30, 311, 241))
        self.label_arm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_arm.setObjectName("label_arm")
        self.btn_clavicole = QtWidgets.QPushButton(self.Arms)
        self.btn_clavicole.setGeometry(QtCore.QRect(10, 100, 93, 28))
        self.btn_clavicole.setObjectName("btn_clavicole")
        self.btn_shoulder = QtWidgets.QPushButton(self.Arms)
        self.btn_shoulder.setGeometry(QtCore.QRect(170, 80, 93, 28))
        self.btn_shoulder.setObjectName("btn_shoulder")
        self.btn_elbow = QtWidgets.QPushButton(self.Arms)
        self.btn_elbow.setGeometry(QtCore.QRect(220, 130, 93, 28))
        self.btn_elbow.setObjectName("btn_elbow")
        self.btn_forearm = QtWidgets.QPushButton(self.Arms)
        self.btn_forearm.setGeometry(QtCore.QRect(120, 190, 93, 28))
        self.btn_forearm.setObjectName("btn_forearm")
        self.btn_wrist = QtWidgets.QPushButton(self.Arms)
        self.btn_wrist.setGeometry(QtCore.QRect(260, 180, 93, 28))
        self.btn_wrist.setObjectName("btn_wrist")
        self.tab_body_parts.addTab(self.Arms, "")
        self.Legs = QtWidgets.QWidget()
        self.Legs.setObjectName("Legs")
        self.label_legs = QtWidgets.QLabel(self.Legs)
        self.label_legs.setGeometry(QtCore.QRect(20, 0, 331, 361))
        self.label_legs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_legs.setObjectName("label_legs")
        self.btn_hip = QtWidgets.QPushButton(self.Legs)
        self.btn_hip.setGeometry(QtCore.QRect(200, 30, 93, 28))
        self.btn_hip.setObjectName("btn_hip")
        self.btn_knee = QtWidgets.QPushButton(self.Legs)
        self.btn_knee.setGeometry(QtCore.QRect(200, 160, 93, 28))
        self.btn_knee.setObjectName("btn_knee")
        self.btn_ankle = QtWidgets.QPushButton(self.Legs)
        self.btn_ankle.setGeometry(QtCore.QRect(200, 260, 93, 28))
        self.btn_ankle.setObjectName("btn_ankle")
        self.tab_body_parts.addTab(self.Legs, "")
        self.Foot = QtWidgets.QWidget()
        self.Foot.setObjectName("Foot")
        self.label_2 = QtWidgets.QLabel(self.Foot)
        self.label_2.setGeometry(QtCore.QRect(90, 20, 221, 291))
        self.label_2.setObjectName("label_2")
        self.btn_heel = QtWidgets.QPushButton(self.Foot)
        self.btn_heel.setGeometry(QtCore.QRect(30, 280, 93, 28))
        self.btn_heel.setObjectName("btn_heel")
        self.btn_ball = QtWidgets.QPushButton(self.Foot)
        self.btn_ball.setGeometry(QtCore.QRect(150, 160, 93, 28))
        self.btn_ball.setObjectName("btn_ball")
        self.btn_inner_foot = QtWidgets.QPushButton(self.Foot)
        self.btn_inner_foot.setGeometry(QtCore.QRect(30, 200, 93, 28))
        self.btn_inner_foot.setObjectName("btn_inner_foot")
        self.btn_outer_foot = QtWidgets.QPushButton(self.Foot)
        self.btn_outer_foot.setGeometry(QtCore.QRect(250, 200, 93, 28))
        self.btn_outer_foot.setObjectName("btn_outer_foot")
        self.btn_toes = QtWidgets.QPushButton(self.Foot)
        self.btn_toes.setGeometry(QtCore.QRect(220, 20, 93, 28))
        self.btn_toes.setObjectName("btn_toes")
        self.tab_body_parts.addTab(self.Foot, "")
        self.Hand = QtWidgets.QWidget()
        self.Hand.setObjectName("Hand")
        self.label_hand = QtWidgets.QLabel(self.Hand)
        self.label_hand.setGeometry(QtCore.QRect(80, 40, 231, 301))
        self.label_hand.setObjectName("label_hand")
        self.btn_hand = QtWidgets.QPushButton(self.Hand)
        self.btn_hand.setGeometry(QtCore.QRect(250, 260, 93, 28))
        self.btn_hand.setObjectName("btn_hand")
        self.btn_thumb = QtWidgets.QPushButton(self.Hand)
        self.btn_thumb.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.btn_thumb.setObjectName("btn_thumb")
        self.btn_index = QtWidgets.QPushButton(self.Hand)
        self.btn_index.setGeometry(QtCore.QRect(20, 60, 93, 28))
        self.btn_index.setObjectName("btn_index")
        self.btn_middle = QtWidgets.QPushButton(self.Hand)
        self.btn_middle.setGeometry(QtCore.QRect(80, 10, 93, 28))
        self.btn_middle.setObjectName("btn_middle")
        self.btn_ring = QtWidgets.QPushButton(self.Hand)
        self.btn_ring.setGeometry(QtCore.QRect(220, 30, 93, 28))
        self.btn_ring.setObjectName("btn_ring")
        self.btn_pinkie = QtWidgets.QPushButton(self.Hand)
        self.btn_pinkie.setGeometry(QtCore.QRect(260, 110, 93, 28))
        self.btn_pinkie.setObjectName("btn_pinkie")
        self.tab_body_parts.addTab(self.Hand, "")
        self.layout_main.addWidget(self.tab_body_parts)
        self.btn_mirror = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_mirror.setObjectName("btn_mirror")
        self.layout_main.addWidget(self.btn_mirror)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_body_parts.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart Renamer"))
        self.label_object_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">Mesh Name    </span></p></body></html>"))
        self.btn_create_hierarchy.setText(_translate("MainWindow", "Create Hierarchy"))
        self.label_type.setText(_translate("MainWindow", "Label Type"))
        self.radioButton_2.setText(_translate("MainWindow", "None"))
        self.radio_btn_jnt.setText(_translate("MainWindow", "Joint"))
        self.radio_btn_ctrl.setText(_translate("MainWindow", "Controller"))
        self.radio_btn_grp.setText(_translate("MainWindow", "Group"))
        self.radio_btn_aim.setText(_translate("MainWindow", "Aim"))
        self.radio_btn_spline.setText(_translate("MainWindow", "Spline"))
        self.radio_btn_clust.setText(_translate("MainWindow", "Cluster"))
        self.label_side.setText(_translate("MainWindow", "Side "))
        self.com_box_side.setItemText(0, _translate("MainWindow", "None"))
        self.com_box_side.setItemText(1, _translate("MainWindow", "Left"))
        self.com_box_side.setItemText(2, _translate("MainWindow", "Right"))
        self.label_kinematic.setText(_translate("MainWindow", " Kinematic"))
        self.com_box_kinematic.setItemText(0, _translate("MainWindow", "None"))
        self.com_box_kinematic.setItemText(1, _translate("MainWindow", "Inverse"))
        self.com_box_kinematic.setItemText(2, _translate("MainWindow", "Forward"))
        self.label_custom_name.setText(_translate("MainWindow", "Custom Name"))
        self.btn_apply.setText(_translate("MainWindow", "Apply"))
        self.label_spine.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/pic/torso.png\"/></p></body></html>"))
        self.btn_root.setText(_translate("MainWindow", "Root"))
        self.btn_spine.setText(_translate("MainWindow", "Spine"))
        self.btn_neck.setText(_translate("MainWindow", "Neck"))
        self.btn_jaw.setText(_translate("MainWindow", "Jaw"))
        self.btn_head.setText(_translate("MainWindow", "Head"))
        self.tab_body_parts.setTabText(self.tab_body_parts.indexOf(self.Spine), _translate("MainWindow", "Spine"))
        self.label_arm.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/pic/arm.png\"/></p></body></html>"))
        self.btn_clavicole.setText(_translate("MainWindow", "Clavicle"))
        self.btn_shoulder.setText(_translate("MainWindow", "Shoulder"))
        self.btn_elbow.setText(_translate("MainWindow", "Elbow"))
        self.btn_forearm.setText(_translate("MainWindow", "Forearm"))
        self.btn_wrist.setText(_translate("MainWindow", "Wrist"))
        self.tab_body_parts.setTabText(self.tab_body_parts.indexOf(self.Arms), _translate("MainWindow", "Arms"))
        self.label_legs.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/pic/leg.png\"/></p></body></html>"))
        self.btn_hip.setText(_translate("MainWindow", "Hip"))
        self.btn_knee.setText(_translate("MainWindow", "Knee"))
        self.btn_ankle.setText(_translate("MainWindow", "Ankle"))
        self.tab_body_parts.setTabText(self.tab_body_parts.indexOf(self.Legs), _translate("MainWindow", "Legs"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/pic/foot.png\"/></p></body></html>"))
        self.btn_heel.setText(_translate("MainWindow", "Heel"))
        self.btn_ball.setText(_translate("MainWindow", "Ball"))
        self.btn_inner_foot.setText(_translate("MainWindow", "Inner"))
        self.btn_outer_foot.setText(_translate("MainWindow", "Outer"))
        self.btn_toes.setText(_translate("MainWindow", "Toes"))
        self.tab_body_parts.setTabText(self.tab_body_parts.indexOf(self.Foot), _translate("MainWindow", "Foot"))
        self.label_hand.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/pic/hand.png\"/></p></body></html>"))
        self.btn_hand.setText(_translate("MainWindow", "Hand"))
        self.btn_thumb.setText(_translate("MainWindow", "Thumb"))
        self.btn_index.setText(_translate("MainWindow", "Index"))
        self.btn_middle.setText(_translate("MainWindow", "Middle"))
        self.btn_ring.setText(_translate("MainWindow", "Ring"))
        self.btn_pinkie.setText(_translate("MainWindow", "Pinkie"))
        self.tab_body_parts.setTabText(self.tab_body_parts.indexOf(self.Hand), _translate("MainWindow", "Hand"))
        self.btn_mirror.setText(_translate("MainWindow", "Mirror YZ and Rename"))
