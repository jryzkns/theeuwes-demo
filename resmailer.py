from email.utils import formatdate
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def mailout_results(res_paths, dest = "attnlab@sfu.ca", sender = "attention_lab_mailer@sfu.ca"):

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = dest
    msg['Date'] = formatdate(localtime=True)
    fn_names = ", ".join(map(basename,res_paths))
    msg['Subject'] = f"[DATA] {fn_names}"

    msg.attach(MIMEText("See Attached."))

    for res_path in res_paths:
        with open(res_path, "r") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(res_path)
            )

        part['Content-Disposition'] = f'attachment; filename="{basename(res_path)}"'
        msg.attach(part)

    session = smtplib.SMTP("mailgate.sfu.ca", 587)
    session.sendmail(sender, dest, msg.as_string())
    session.close()
