#!/usr/bin/env python

import sys
import feedparser

APIURL = "http://ci.nii.ac.jp/books/opensearch/search?"

def findByFreeWord(word):
  try:
    return feedparser.parse(APIURL + "q=" + word)
     
  except IOError:
    print "I/O error"

  except :
    print "Unexpected error:", sys.exc_info()[0]

