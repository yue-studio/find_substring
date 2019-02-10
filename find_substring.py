#!/usr/bin/env python

import os
import sys

def find_substring(string, substring):

    def starts_with(string, substring):
        while True:
            if substring == '':
                return True

            if substring[0] == '+':
                string, substring = string[1:], substring[0:]
                return True 

            if substring[0] == '*' and string[0] == last_char:
                string, substring = string[1:], substring[0:]
                return True

            if len(string) > 1 and substring[0] == '.':
                # no more charecter in regex to match 
                if len(substring) == 1:
                   return True
                if string[1] == substring[1]:
                   string, substring = string[1:], substring[1:]
                   return True
                if string[1] == last_char:
                   string, substring = string[1:], substring[1:]
                   return True

            if string == '' or string[0] != substring[0]:
                return False

            last_char = string[0]

            string, substring = string[1:], substring[1:]

    n = 0

    while string != '' and substring != '':
        if starts_with(string, substring):
            return n

        string = string[1:]
        n += 1

    return -1


def main():

   if (len(sys.argv) < 3 or len(sys.argv) > 3):  
      print """\
This script will string (in regular expression in filename.txt 

Usage:  find_substring filename.txt 'AT+CG.*'
"""
      sys.exit(1)

   with open(sys.argv[1]) as fd:
     linenum = 0
     found = 0

     for line in fd:
       linenum += 1
       res = find_substring(line, sys.argv[2])
       if res != -1:
          found = 1
          print 'Found %s at index %d, line %d' % (sys.argv[2], res, linenum)

     if found == 0:
        print '%s has not been found in %d lines' % (sys.argv[2], linenum)

if __name__== "__main__":
  main()


