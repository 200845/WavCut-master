import os
import sys
from aip import AipSpeech
from openpyxl.compat import file

""" 你的 APPID AK SK """
APP_ID = '14913816'
API_KEY = 'muqbMozoGOA42hI9EhSbxqWf'
SECRET_KEY = 'vO42mvMOAbGiuVBLNWzsl0rZ08TczF1a'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件

txt_path  = str(sys.argv[1])
temp_path  = str(sys.argv[2])
rootDir = temp_path

for lists in os.listdir(rootDir):
    f2 = open(txt_path, 'a+')
    files_temp=rootDir+'/'+lists
    cy = client.asr(get_file_content(str(files_temp)), 'wav', 16000, {'dev_pid': 1537})
    print(cy)
    if ("result" in cy.keys()):
        f2.write(str(cy['result']))
        f2.write("\n")
        print('success in writing!')
    else:
        f2.write("  ******* skip few words ******   ")
    f2.close()

# cy = client.asr(get_file_content(str('C:/Users\epic_cy\Desktop\WavCut-master\WavCut-master\MusicResult/3.wav')), 'wav', 16000, {'dev_pid': 1537})
# print(cy)