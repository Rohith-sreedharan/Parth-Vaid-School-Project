'''
Dont Remove this line...
Coded by Rohith SV aka ROHITHADITYA
'''

# Importing Modules...
import pyttsx3
import PyPDF2
import random
import time
import sys
import webbrowser as wb
import pyfiglet

# Class For The Whole Code..
class reader():
    def menu():
        print('''
1. Read pdf
2. Contact Dev
3. List Of Books to read
4. Exit
''')

    def read():
        book = open('s.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages

        speaker = pyttsx3.init()
        for num in range(7, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    def lis():
        lisy = ['Shakspere histor', 'Novel Future', 'Baby ON Board']
        a = random.choice(lisy)
        print(a)

    def exit():
        print('Program By @Rohithaditya\nThaning You\nSee Google by - www.googl.com/rohithaditya')
        time.sleep(2)
        print('Exiting...')
        sys.exit()

    def contact():
        print('So You GOt probs? Right... Wait Contacting Dev....')
        time.sleep(1)
        print('''
[+] GITHUB - www.github.com/rohith-sreedharan
[+] TELEGRAM - www.telegram.me/rohithaditya
[+] TWITTER - www.twitter.com/rohithaditya

[+] Opening Telegram Chat...
''')
        time.sleep(2)
        wb.open('telegram.me/rohithaditya')
        time.sleep(1)
        return
    
    def setup():
        print('Starting To install pyfiglet..')
        os.system('pip install pyfiglet')
        time.sleep(2)
        print('pyttsx3 module Installing...')
        os.system('pip install pyttsx3')
        time.sleep(1)
        print('pypdf2 module Installing...')
        os.system('pip install pypdf2')
        time.sleep(1)
        print('setup.py finshed...')


"""
Main COde for the whole program...
Author ; @Rohithaditya

"""
# Main code...
result = pyfiglet.figlet_format(
    "Zira Scrapper\n(C) @ROHITHADITYA", font="slant")
print(result)
time.sleep(1)
x = input('Enter Your Name: ')
print(f'''
Hello {x} Greetings from @Rohithaditya !
Welcome To ZIRA PDF READER
''')

reader.menu()
ci = int(input('Enter your choice: '))
try:
    if ci == 1:
        print('Starting to read')
        reader.read()
    if ci == 2:
        reader.contact()
    if ci == 3:
        reader.lis()
    if ci == 4:
        reader.exit()
    else:
        print('Error wrong Choice...')
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt :: Exitting')

except OSError:
    print('Caught OSError :: Invaild File or File having Problem')

except NameError:
    print('Caught NameError :: Exitting Due to Internet connection problem')

except Exception as e:
    print(
        f'Caught Exception :: {e} Error Conatct Dev By Using Following Link...')
    time.sleep(2)
    wb.open('telegram.me/rohithaditya')
    time.sleep(2)
    sys.exit()


"""
AUTHOR: @Rohithaditya
CODE DETAILS : LICENSE TO RESPECTIVE MODULES

"""