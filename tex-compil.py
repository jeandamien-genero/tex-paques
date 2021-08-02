#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author : Jean-Damien Généro
Affiliation : French National Center for Scientific Research (CNRS)
Assigned at the Centre de recherches historiques (CRH, UMR 8558)
Date : 2021-08-02
Update :
"""

import os
from lxml import etree
import sys


xslfile = sys.argv[1]
xmlfile = sys.argv[2]


def xsl_transformation(xslfile, xmlfile):
	"""
	Transforming xml file in tex file with an xslt stylesheet.
	:param xslfile: path to an xsl stylesheet
	:type xslfile: str
	:param xmlfile: path to an xml file
	:type xmlfile: str
	:return: tex file
	:rtype: lxml.etree._XSLTResultTree
	"""
	# parsing xml file
	source = etree.parse(xmlfile)
	# Remove namespace prefixes
	tei = source.getroot()
	for elem in tei.getiterator():
		elem.tag = etree.QName(elem).localname
	# Remove unused namespace declarations
	etree.cleanup_namespaces(tei)
	# xls transformation
	xsl_doc = etree.parse(xslfile)
	xsl_transformer = etree.XSLT(xsl_doc)
	output_doc = xsl_transformer(source)
	print(type(output_doc))
	return output_doc


xsl_transformation(xslfile, xmlfile)
