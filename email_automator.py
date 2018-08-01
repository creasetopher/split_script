import smtplib
from os.path import basename
import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

month = str(datetime.datetime.now().month)
today = str(datetime.datetime.now().day)



def email_sender(file, data, recipients, server = "127.0.0.1", **kwargs):
    me = 'GriffinSafety@fb.com'
    msg = MIMEMultipart()
    msg['Subject'] = month + "/" + today + 'Data'
    msg['From'] = me
    msg['To'] = ", ".join(recipients)

    with open(file) as csv_file:
        attachment = MIMEApplication(
                    csv_file.read(),
                    Name = basename(file)
                    )

    attachment['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
    msg.attach(attachment)

    s = smtplib.SMTP(server)
    s.sendmail(me, recipients, msg.as_string())
    s.close()
