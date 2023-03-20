import smtplib

# Chiedi i dati per l'email mittente
email_mittente = input("Inserisci l'indirizzo email mittente: ")
# password_mittente = input("Inserisci la password dell'email mittente: ")

# Chiedi i dati per l'email destinatario
email_destinatario = input("Inserisci l'indirizzo email destinatario: ")

# Chiedi i dettagli del server SMTP
smtp_server = input("Inserisci il nome del server SMTP: ")
smtp_port = input("Inserisci il numero di porta del server SMTP (di solito è 587 o 465): ")

# Crea il messaggio email

messaggio = """From: From Person <from@fromdomain.com>
To: “test Email” testemail@tedomain.it
Subject: Test Message 

Hello World,
This is a test message sent from Python.

Yours truly,
SMTP administrator

.

QUIT
"""

# Invia l'email
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Email inviata con successo!")
except Exception as e:
    print("Errore durante l'invio dell'email:", e)
finally:
    server.quit()
