# -*- coding:utf-8 -*-

import unittest
from mock import Mock
import cinii.books
import feedparser
import sys
import os

class TestFunctions(unittest.TestCase):
  def setUp(self):
    print 'setUp'

  def tearDown(self):
    print 'tearDown'

  def testFindByFreeWord(self):
    # create mock
    response_tmp = ('<?xml version="1.0" encoding="UTF-8"?> '
    '<feed xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/" xmlns:cinii="http://ci.nii.ac.jp/ns/1.0/" xmlns="http://www.w3.org/2005/Atom">' 
    '<title>CiNii Books OpenSearch - test</title>' 
    '<link href="http://ci.nii.ac.jp/books/search/?count=20&amp;sortorder=1&amp;q=test&amp;advanced=false"/>'
    '<link rel="self" type="application/atom+xml" href="http://ci.nii.ac.jp/books/opensearch/search?q=test"/>'
    '<id>http://ci.nii.ac.jp/books/opensearch/search?q=test</id>'
    '<updated>2013-09-16T12:16:28+0900</updated>'
    '<opensearch:totalResults>27326</opensearch:totalResults>'
    '<opensearch:startIndex>0</opensearch:startIndex>'
    '<opensearch:itemsPerPage>20</opensearch:itemsPerPage>'
    '<entry>'
    '<title>California Test Bureau manual</title>'
    '<link href="http://ci.nii.ac.jp/ncid/BA76174068"/>'
    '<link rel="alternate" type="application/rdf+xml" href="http://ci.nii.ac.jp/ncid/BA76174068.rdf"/>'
    '<id>http://ci.nii.ac.jp/ncid/BA76174068</id>'
    '<author>'
    '<name/>'
    '</author>'
    '<dc:publisher>California Test Bureau</dc:publisher>'
    '<cinii:ownerCount>0</cinii:ownerCount>'
    '</entry>'
    '<entry>'
    '<title>Multiple choice secrets</title>'
    '<link href="http://ci.nii.ac.jp/ncid/BB11520477"/>'
    '<link rel="alternate" type="application/rdf+xml" href="http://ci.nii.ac.jp/ncid/BB11520477.rdf"/>'
    '<id>http://ci.nii.ac.jp/ncid/BB11520477</id>'
    '<author>'
    '<name>Complete Test Preparation</name>'
    '</author>'
    '<dc:publisher>Complete Test Preparation</dc:publisher>'
    '<prism:publicationDate>2011</prism:publicationDate>'
    '<updated>2011</updated>'
    '<dcterms:hasPart>urn:isbn:9781477539880</dcterms:hasPart>'
    '<cinii:ownerCount>1</cinii:ownerCount>'
    '</entry>'
    '</feed>'
    )
    feedparser.parse = Mock(return_value=feedparser.parse(response_tmp))
    expectUrl = "http://ci.nii.ac.jp/books/opensearch/search?q=test"

    #call method
    result = cinii.books.findByFreeWord("test")

    #checking
    feedparser.parse.assert_called_once_with(expectUrl)
    self.assertEqual(len(result['entries']), 2) 
    self.assertEqual(result['entries'][0].title, "California Test Bureau manual") 

  def testfindByFreeWordIfErrorRaised(self):
    # create mock
    feedparser.parse = Mock(side_effect=IOError)
    sys.stdout = open("tmp.txt","w+")

    #call method
    result = cinii.books.findByFreeWord("test")
    sys.stdout.close()

    #checking
    expected_msg = "I/O error"
    out = open('tmp.txt', 'r+')
    self.assertEqual(out.readline().rstrip(), expected_msg)

    #closing
    out.close()
    sys.stdout = sys.__stdout__
    os.remove('tmp.txt')

if __name__ == '__main__':
  unittest.main()
