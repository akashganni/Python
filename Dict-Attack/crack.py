import zipfile
import sys
from threading import Thread

def attack(zFile, password):
	try:
		zFile.extractall(pwd=password.encode('utf-8'))
		print('[+] Password:', password)
	except:
		pass

def main():
	zFile = zipfile.ZipFile('fuin.zip')
	passFile = open('words.txt')
	for line in passFile.readlines():
		password = line.strip('\n')
		try:
			t = Thread(target=attack, args=(zFile, password))
			t.start()
		except:
			pass

print('h')