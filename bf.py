#!/usr/bin/python

import zipfile
import os

zip_file = input("[+] ZIP file: ")
word_list = input("[+] Password list: ")

def main(zip_file, wordlist):
	
	try:
		zipf = zipfile.ZipFile(zip_file)
	except zipfile.BadZipfile:
		print("\n[!] Bad ZIP file.")
		os.sys.exit()
	except FileNotFoundError:
		print("\n[!] ZIP file notfound.")
		os.sys.exit()
		
	try:
		open(wordlist, "rb")
	except FileNotFoundError:
		print("\n[!] Password list notfound.")
		os.sys.exit()
		
	with open(wordlist, "rb") as f:
		passes = [x.strip() for x in f.readlines()]
		for x in passes:
			print(f"Trying {x.decode('latin-1')}")
			try:
				zipf.extractall('results', None, x)
				print("\n[*] Password found :)")
				print(f"[*] Password: {x.decode('latin-1')}\n") 
				os.sys.exit()
			except Exception:
				pass
		print("[x] Sorry, Password not found :(")
main(zip_file, word_list)