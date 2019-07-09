import os

os.chdir(r'C:\Users\student\TIL\00_Startcamp\02_Day\dummy')

for filename in os.listdir('.'):
    os.rename(filename, filename.rename('SAMSUNG_','SSAFY'))