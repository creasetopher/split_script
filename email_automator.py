import smtplib
from os.path import basename
import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

month = str(datetime.datetime.now().month)
today = str(datetime.datetime.now().day)



def email_sender(file, data, recipients, server = "127.0.0.1", **kwargs):
    """
    Sends email to 1 or more recipients

    arg1 : str
        name of local file to attach
    arg2 : str
        unformatted data from arg1
    arg3 : array<str>
        list of recipeint email adresses
    arg4 : str
        server, defaults to localhost
    arg5: dict
        optional args to be included in email body
    """

    me = 'testemail1@fb.com'
    msg = MIMEMultipart()
    msg['Subject'] = month + "/" + today + 'Data'
    msg['From'] = me
    msg['To'] = ", ".join(recipients)

    msg.attach(MIMEText(data))
    if kwargs:
        extra_data = ''
        for k in kwargs.iteritems():
            extra_data += str(k) + '\n'
    msg.attach(MIMEText(extra_data))

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
