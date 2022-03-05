import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QApplication,QLabel,QHBoxLayout,QVBoxLayout,QTextEdit,QWidget,QLineEdit,QPushButton,QMessageBox

class Mail(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.SenderMailAddressLabel = QLabel("Gönderen Mail Adresi")
        self.SenderMailPassLabel = QLabel("Gönderen Mail Parolası")
        self.RecipientMailAddressLabel = QLabel("Alıcı Mail Adresi")
        self.MailLabel = QLabel("Mailiniz")
        self.MailSubjectLabel = QLabel("Mail Konusu")

        self.SenderMailAddress = QLineEdit()
        self.SenderMailPass = QLineEdit()
        self.RecipientMailAddress = QLineEdit()

        self.mailSubject = QLineEdit()
        self.mail = QTextEdit()
        self.btnSend = QPushButton("Gönder")

        SenderV_box = QVBoxLayout()
        SenderV_box.addWidget(self.SenderMailAddressLabel)
        SenderV_box.addWidget(self.SenderMailAddress)
        SenderV_box.addWidget(self.SenderMailPassLabel)
        SenderV_box.addWidget(self.SenderMailPass)

        RecipientV_box = QVBoxLayout()
        RecipientV_box.addWidget(self.RecipientMailAddressLabel)
        RecipientV_box.addWidget(self.RecipientMailAddress)
        RecipientV_box.addWidget(self.MailSubjectLabel)
        RecipientV_box.addWidget(self.mailSubject)
        RecipientV_box.addWidget(self.MailLabel)
        RecipientV_box.addWidget(self.mail)
        RecipientV_box.addWidget(self.btnSend)

        h_box = QHBoxLayout()
        h_box.addLayout(SenderV_box)
        h_box.addLayout(RecipientV_box)

        self.btnSend.clicked.connect(self.SendMail)

        self.setLayout(h_box)
        self.setWindowTitle("Mail")
        self.show()

    def SendMail(self):
        message = MIMEMultipart()
        message["From"] = self.SenderMailAddress.text()
        message["To"] = self.RecipientMailAddress.text()
        message["Subject"] = self.mailSubject.text()

        message_body = MIMEText(self.mail.toPlainText(),"plain")
        message.attach(message_body)

        try:
            mail = smtplib.SMTP("smtp.gmail.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.SenderMailAddress.text(),self.SenderMailPass.text())
            mail.sendmail(message["From"],message["To"],message.as_string())
            mail.close()
            QMessageBox.about(self,"Başarılı","Mail gönderildi...")
        except:
            print("bir hata var")


app = QApplication(sys.argv)
mail1 = Mail()
sys.exit(app.exec_())


