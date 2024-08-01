import smtplib  
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Configurações do servidor SMTP do Outlook
smtp_server = 'smtp.office365.com'
smtp_port = 587  # Porta TLS padrão

# Suas credenciais de login do Outlook
sender_email = 'digibot2023@outlook.com'
password = 'Tomatefrito1960'

# Criando o objeto MIMEMultipart para o email

def enviar_email(destinatario, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = destinatario
    message['Subject'] = 'Alerta meteorologia'
    # Corpo do email
    body = body
    message.attach(MIMEText(body, 'plain'))

    # Configurando a conexão com o servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    # Enviando o email
    try:
      server.sendmail(sender_email, destinatario, message.as_string())
    # Encerrando a conexão com o servidor
      server.quit()
    except Exception as e:
      print(f"Ocorreu um erro: {e}")  
def check_temperature(temperature, destinatario, nome):
  if temperature < 20:
    body = f"Olá {nome}, a previsão de tempo para hoje é de {temperature:.2f}°C inferior a 20°C, prepare o casaco!"
    enviar_email(destinatario, body)
    print("Alerta enviado!")


  if temperature > 20:
    body = f"Olá {nome}, a previsão de tempo para hoje é de {temperature:.2f}°C superior a 20°C, hidrate-se!"
    enviar_email(destinatario, body)
    print("Alerta enviado!")



 
