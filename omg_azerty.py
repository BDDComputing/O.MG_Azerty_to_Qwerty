#!/usr/env/python
# -*- coding: utf-8 -*-

# Script by BDD Computing - 2021
# Using the incredible OMG Cable made by @_MG_ (https://twitter.com/_mg_)

import sys, getopt
import re 
import sys
import os

def FR_TO_US(line):
	##############################################################################################
	# Windows Layout
	#layout_1 = 'qbcdefghijkl,noparstuvzxywQBCDEFGHIJKL?NOPQRSTUVZXYW!@#$%^&*()=.><+1234567890'
	#layout_2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-:/._!@#$%^&*()'
	##############################################################################################
	#MacOS Layout
	layout_1 = """ qbcdefghijkl;noparstuvzxywQBCDEFGHIJKL:NOPARSTUVZXYW!@#$%^&*()=.><+185-/\"'_ """
	layout_2 = """ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-:/._&!()=%ù° """
	##############################################################################################
	my_dict = dict(zip(layout_2, layout_1))
	line = line.replace('\n', '')
	translated_str = ''.join(my_dict[c] for c in line.replace('\\', ''))
	return translated_str
	

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'Usage : python omg_azerty.py -i <payload_in_azerty.txt> -o <payload_in_qwerty.txt>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'Usage : python omg_azerty.py -i <payload_in_azerty.txt> -o <payload_in_qwerty.txt>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   if inputfile == '' or outputfile == '':
   	print 'Usage : python omg_azerty.py -i <payload_in_azerty.txt> -o <payload_in_qwerty.txt>'
   	sys.exit(1)
   print '######################################'   
   print 'Input file is :', inputfile
   print 'Output file is :', outputfile
   print '######################################'
   print ''
   
   try:
	filepath = inputfile
	filepath_new = outputfile
	with open(filepath, 'rb') as fp:
		with open(filepath_new, 'w') as fp2:
			lines = fp.readlines()
			cnt = 1
			for line in lines:
				print("Original line {}: {}".format(cnt, line.strip()))
				if line.startswith('STRING'):
					payload_to_convert = line[7:]
					new_line = FR_TO_US(payload_to_convert)
					new_line = new_line.replace('', '')
					converted_line = 'STRING ' + new_line + '\n'
					fp2.write(converted_line)
					cnt += 1
					print("Converted line : {}".format(converted_line.strip()))
					print ''
				else:
					cnt += 1
					print("Untouched line : {}".format(line.strip()))
					print ''
					simple_line = line
					fp2.write(simple_line)
				
   finally:
	fp.close()
	fp2.close()
	readoutput = "cat " + outputfile
	print '######################################'
	print '#########FOR COPY AND PASTE###########'
	print '######################################'
	os.system(readoutput)
	print ''

if __name__ == "__main__":
   main(sys.argv[1:])
