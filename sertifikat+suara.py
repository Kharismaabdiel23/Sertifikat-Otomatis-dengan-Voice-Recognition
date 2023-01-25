import time
import speech_recognition as sr

engine = sr.Recognizer() 
mic = sr.Microphone() 
engine.pause_treshold = 5

hasil = ""

with mic as source:

    print("Silahkan mulai bicara")
    rekaman = engine.listen(source, timeout=3)
try:
    hasil = engine.recognize_google(rekaman, language = "id-ID")
    print(hasil)
    text_file = open("D:\\NOV FILE\\kuliah\\TUGAS\\SEMESTER 5\\python lnjt\\automasi\\Book1.csv", "a")
    text_file.write("\n"+hasil)
    text_file.close()
    time.sleep(1)
except sr.WaitTimeoutError:
    print("Timeout, Recognition stopped")
except sr.UnknownValueError:
    print("Maaf tidak di deteksi, mohon coba lagi")
except Exception as e:
    print(e)



text_file = open("D:\\NOV FILE\\kuliah\\TUGAS\\SEMESTER 5\\python lnjt\\automasi\\Book1.csv", "a")
text_file.write("\n"+hasil)
text_file.close()

import csv
import cv2

with open('D:\\NOV FILE\kuliah\\TUGAS\SEMESTER 5\\python lnjt\\automasi\\book1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    list_names = []
    for index, row in enumerate(csv_reader):
        template = cv2.imread('D:\\NOV FILE\kuliah\\TUGAS\SEMESTER 5\\python lnjt\\automasi\\InkedCertificate Template2.jpg')
        
        # loop for each column
        for i, column in enumerate(row):
            if i == 0 and len(row)>0:
                text_width, text_height = cv2.getTextSize(column, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, 2)[0]
                text_x = (template.shape[1] - text_width) // 2 - 30
                text_y = (template.shape[0] + text_height) // 2 + 50
                cv2.putText(template, column, (text_x, text_y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
            elif i == 1 and len(row)>1:
                text_width, text_height = cv2.getTextSize(column, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, 2)[0]
                text_x = (template.shape[1] - text_width) // 2 - 10
                text_y = (template.shape[0] + text_height) // 2 + 50
                cv2.putText(template, column, (text_x, text_y), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1.3, (0, 0, 255), 1, cv2.LINE_AA)
        # add more elif for each column that you want to add
    if len(row)>0:
        cv2.imwrite(f'D:\\NOV FILE\\kuliah\\TUGAS\\SEMESTER 5\\python lnjt\\automasi\\sertifikat\\{row[0]}.jpg', template)
    else:
        print("row kosong")
    print(f"Proccessing Certificate ke {index + 1}")
            
cv2.imwrite(f'D:\\NOV FILE\\kuliah\\TUGAS\\SEMESTER 5\\python lnjt\\automasi\\sertifikat\\{row[0]}.jpg', template)
print(f"Proccessing Certificate ke {index + 1}")