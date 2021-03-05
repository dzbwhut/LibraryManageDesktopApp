''' 用户注册
    setUpUI用来初始化UI界面
    signUp实现在注册过程中的逻辑以及对数据库的操作，按理说应该把数据库操作单独写一个模块的，不过我很懒…
    注册成功暂时只是把数据插入了数据库，本来应该加上跳转页面之类的操作
    如果觉得黑色的效果很好看的话，大家也可以调用经典的QSSstyle表qdarkstyle
    '''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
from PyQt5.QtSql import *
import hashlib


class SignUpWidget(QWidget):
    user_signup_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__() 
        self.resize(400, 420)
        self.setWindowTitle("欢迎登陆管理系统-YZY")
        self.setUpUI()

    def setUpUI(self):   
        font = QFont()
        font.setPixelSize(36)
        lineEditFont = QFont()
        lineEditFont.setPixelSize(16)
            
        self.signUpLabel = QLabel("注   册")
        self.signUpLabel.setAlignment(Qt.AlignCenter)
        # self.signUpLabel.setFixedWidth(300)
        self.signUpLabel.setFixedHeight(100)       
        self.signUpLabel.setFont(font)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.signUpLabel, Qt.AlignHCenter)
        self.setLayout(self.layout)
        
        # 表单，包括学号，姓名，密码，确认密码
        self.formlayout = QFormLayout()
        font.setPixelSize(18)
        
        
        ''' # Row1 userIdLabel
            self.userIdLabel = QLabel("用户编号: ")
            self.userIdLabel.setFixedWidth(100)
            self.userIdLabel.setFont(font)
            self.userIdLineEdit = QLineEdit()
            self.userIdLineEdit.setFixedWidth(180)
            self.userIdLineEdit.setFixedHeight(32)
            self.userIdLineEdit.setFont(lineEditFont)
            self.userIdLineEdit.setMaxLength(10)
            self.userIdLineEdit.setText('A6-3-302-001')
            self.formlayout.addRow(self.userIdLabel, self.userIdLineEdit)
            '''
        # Row2
        self.userNameLabel = QLabel("姓    名: ")
        self.userNameLabel.setFixedWidth(100)
        self.userNameLabel.setFont(font)
        self.userNameLineEdit = QLineEdit()
        self.userNameLineEdit.setFixedHeight(32)
        self.userNameLineEdit.setFixedWidth(180)
        self.userNameLineEdit.setFont(lineEditFont)
        self.userNameLineEdit.setMaxLength(10)
        self.formlayout.addRow(self.userNameLabel, self.userNameLineEdit)
        
        # Row3
        self.passwordLabel = QLabel("密    码: ")
        self.passwordLabel.setFont(font)        
        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setFixedWidth(180)
        self.passwordLineEdit.setFixedHeight(32)
        self.passwordLineEdit.setFont(lineEditFont)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setMaxLength(32)
        self.formlayout.addRow(self.passwordLabel, self.passwordLineEdit)
        
        # Row4  password
        self.passwordConfirmLabel = QLabel("确认密码: ")
        self.passwordConfirmLabel.setFont(font)
        self.passwordConfirmLineEdit = QLineEdit()
        self.passwordConfirmLineEdit.setFixedWidth(180)
        self.passwordConfirmLineEdit.setFixedHeight(32)
        self.passwordConfirmLineEdit.setFont(lineEditFont)
        self.passwordConfirmLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordConfirmLineEdit.setMaxLength(32)
        self.formlayout.addRow(self.passwordConfirmLabel, self.passwordConfirmLineEdit)

        #lineEditFont.setPixelSize(10)
        # Row5
        self.userAddrLabel = QLabel("地    址: ")
        self.userAddrLabel.setFont(font)
        self.userAddrLineEdit = QLineEdit()
        self.userAddrLineEdit.setFixedHeight(32)
        self.userAddrLineEdit.setFixedWidth(180)
        self.userAddrLineEdit.setFont(lineEditFont)
        self.userAddrLineEdit.setMaxLength(32)
        self.userAddrLineEdit.setText('YZY-A6-3-302')
        self.formlayout.addRow(self.userAddrLabel, self.userAddrLineEdit)
        
        # Row6
        self.userPhoneLabel = QLabel("电    话: ")
        self.userPhoneLabel.setFont(font)
        self.userPhoneLineEdit = QLineEdit()
        self.userPhoneLineEdit.setFixedHeight(32)
        self.userPhoneLineEdit.setFixedWidth(180)
        self.userPhoneLineEdit.setFont(lineEditFont)
        self.userPhoneLineEdit.setMaxLength(11)
        self.formlayout.addRow(self.userPhoneLabel, self.userPhoneLineEdit)
        
        # Row6
        self.NullLabel = QLabel("")
        self.NullLabel.setFont(font)       
        self.NullLabel.setFixedHeight(32)        
        self.formlayout.addRow(self.NullLabel)
        
        # Row7
        self.signUpbutton = QPushButton("注 册")
        self.signUpbutton.setFixedWidth(120)
        self.signUpbutton.setFixedHeight(30)
        self.signUpbutton.setFont(font)
        self.formlayout.addRow("", self.signUpbutton)
        
        
        # formlayout --> widget --> Hlayout
        widget = QWidget()  
        widget.setFixedHeight(250)
        widget.setFixedWidth(300)
        widget.setLayout(self.formlayout)
        # 水平居中
        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(widget, Qt.AlignCenter)
        widget = QWidget()
        widget.setLayout(self.Hlayout)
        self.layout.addWidget(widget, Qt.AlignHCenter)

        # 地址验证:地址
        addrRegExp = QRegExp("YZY-[A-Z][0-9]-[0-9]-[0-9]{3}")
        addrValidator = QRegExpValidator(addrRegExp)        
        self.userAddrLineEdit.setValidator(addrValidator)
        
        # 电话验证:电话
        addrRegExp = QRegExp("[0-9]{11}")
        addrValidator = QRegExpValidator(addrRegExp)        
        self.userAddrLineEdit.setValidator(addrValidator)
        # 密码验证
        pwdRegExp = QRegExp("[a-zA-Z0-9]+$")
        pwdValidator = QRegExpValidator(pwdRegExp)
        self.passwordLineEdit.setValidator(pwdValidator)        
        self.passwordConfirmLineEdit.setValidator(pwdValidator)
        
        self.signUpbutton.clicked.connect(self.SignUp)
        #self.userIdLineEdit.returnPressed.connect(self.SignUp)
        self.userNameLineEdit.returnPressed.connect(self.SignUp)
        self.passwordLineEdit.returnPressed.connect(self.SignUp)
        self.passwordConfirmLineEdit.returnPressed.connect(self.SignUp)
        self.userAddrLineEdit.returnPressed.connect(self.SignUp)
        self.userPhoneLineEdit.returnPressed.connect(self.SignUp)

    def SignUp(self):
        #userId = self.userIdLineEdit.text()
        #userNum=3
        #userId = str(userNum+1)
        userName = self.userNameLineEdit.text()
        userAddr = self.userAddrLineEdit.text()
        userPhone = self.userPhoneLineEdit.text()
        password = self.passwordLineEdit.text()
        confirmPassword = self.passwordConfirmLineEdit.text()
        if (userName == "" or password == "" or confirmPassword == "" or userAddr == "" or userPhone == ""):
            print(QMessageBox.warning(self, "警告", "表单不可为空，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:  # 需要处理逻辑，1.账号已存在;2.密码不匹配;3.插入user表
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('./db/LibraryManagement.db')
            db.open()
            query = QSqlQuery()
            if (confirmPassword != password):
                print(QMessageBox.warning(self, "警告", "两次输入密码不一致，请重新输入", QMessageBox.Yes, QMessageBox.Yes))
                return
            elif (confirmPassword == password):                             
                # md5编码
                hl = hashlib.md5()
                hl.update(password.encode(encoding='utf-8'))
                md5password = hl.hexdigest()
                        
                sql = "SELECT * FROM User WHERE Name='%s'" % (userName)
                query.exec_(sql)
                if (query.next()):
                    print(QMessageBox.warning(self, "警告", "该账号已存在,请重新输入", QMessageBox.Yes, QMessageBox.Yes))
                    return
                else:
                    sql = "SELECT COUNT(StudentId) FROM User"
                    query.exec_(sql)
                    if query.next():
                        userId =  str(query.value(0)+1) 
                    
                    sql = "INSERT INTO user VALUES ('%s','%s','%s',0,'%s','%s',0,0,CURRENT_TIMESTAMP,1)" % (
                        userId, userName, md5password, userAddr,userPhone)
                    db.exec_(sql)
                    db.commit()
                    print(QMessageBox.information(self, "提醒", "您已成功注册账号!", QMessageBox.Yes, QMessageBox.Yes))
                    self.user_signup_signal.emit(userId)
                db.close()
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = SignUpWidget()
    mainMindow.show()
    sys.exit(app.exec_())
