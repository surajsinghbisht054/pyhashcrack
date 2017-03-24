#!/usr/bin/python
#
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# =================Other Configuration================ 
# Usages :
usage = "usage: %prog [options] "
# Version
Version="%prog 0.0.1"
# ====================================================
print __author__
 
# Import Modules
import hashlib
import optparse
import sys
import time


class hash_crack_engine:
	def __init__(self):
		self.starttime = time.time()
		self.extract_input_data()
		self.open_and_get_file_data()
		self.start_cracking_engine()
		self.closetime = time.time()
		self.close_all_process()
		

	def encrypt_salt(self, string):
		if self.salt=="md5":
			return hashlib.md5(string).hexdigest()

	def start_cracking_engine(self):
		self.got_hash = []
		for i in self.words:
			if self.encrypt_salt(i.strip("\n")) in self.hashlist:
				print "[+] Hash Cracked! {} = {}".format(i.strip('\n'), self.encrypt_salt(i.strip("\n")))
				self.result.write(" {} : {}\n".format(i.strip('\n'), self.encrypt_salt(i.strip("\n"))))
				self.got_hash.append(i.strip("\n"))
				if len(self.got_hash)==len(self.hashlist):
					break
			self.pwdtries = self.pwdtries + 1
		return

	def extract_input_data(self):
		self.starttime=time.time()
		self.pwdtries=0
		# Extracting Function
		parser = optparse.OptionParser(usage, version=Version)
		parser.add_option("-f", "--file", action="store", type="string", dest="filename",help="Please Specify Path of Hash File", default=None)
		parser.add_option("-d", "--dict", action="store", type="string", dest="dictionery", help="Please Specify Path of Password Dictionery.", default=None)
		parser.add_option("-o", "--output", action="store", type="string", dest="output", help="Please Specify Path for Saving Cracked hash", default='cracked_hash.txt')
		parser.add_option("-s", "--salt", action="store", type="string", dest="salt", help="Please Provide Hash Salt. ex: md5, sha1, sha256, sha512", default=None)
		(option, args)=parser.parse_args()
		# Record Inputs Data
		print "[+] Extracting Input Data..."
		self.filename=option.filename
		self.dictionery=option.dictionery
		self.output = option.output
		self.salt = option.salt
		
		if not self.salt:
			print "[+] Please Provide Hash Salts."
			sys.exit(0)
		if self.salt not in hashlib.algorithms:
			print "[+] Please Provide Valid Salt. \n\t\tEx : {}".format(hashlib.algorithms)
			sys.exit(0)

		if not self.filename:
			print "[+] Please Provide Hash File."
			sys.exit(0)
		
		if not self.dictionery:
			print "[+] Please Provide Password Source."
			sys.exit(0)
		if not self.output:
			print "[+] Please Provide Output Path."
			sys.exit(0)
		return

	def open_and_get_file_data(self):
		hashlist = open(self.filename,'r')
		wordlist = open(self.dictionery, 'r')		
		self.hashlist = [i.strip('\n') for i in hashlist.xreadlines()] 
		self.words = wordlist.xreadlines()
		self.result = open(self.output,'a')
		return

	def close_all_process(self):
		self.result.close()
		self.time_management()
		return
		
	def time_management(self):
		print "[*]	Starting Time ",self.starttime
		print "[*]	Closing  Time ",self.closetime
		print "[*]	Password Try  ",self.pwdtries
		print "[*]	Average Speed ",self.pwdtries/(self.closetime-self.starttime)
		return

# main trigger function
if __name__=="__main__":
	hash_crack_engine()
