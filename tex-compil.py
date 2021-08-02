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
import re
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
	return output_doc


def tex_compil():
	unnecessaries_extensions = ["toc", "gz", "xml", "out", "blg", "bcf", "bbl", "aux"]
	tex = xsl_transformation(xslfile, xmlfile)
	texfolder = re.sub(r"(\.\/.+)\/.+\.xml", "\\1", xmlfile)
	texname = re.sub(r"\.\/.+\/(.+)\.xml", "\\1.tex", xmlfile)
	logname = re.sub(r"\.\/.+\/(.+)\.xml", "\\1.log", xmlfile)
	pdfname = re.sub(r"\.\/.+\/(.+)\.xml", "\\1.pdf", xmlfile)
	texpath = os.path.join(texfolder, texname)
	with open(texpath, 'w', encoding="utf-8") as newtexfile:
		newtexfile.write(str(tex))
	print("***** COMPILATION N°1 *****")
	os.system("xelatex ./{}".format(texpath))
	print("***** COMPILATION N°2 *****")
	os.system("xelatex ./{}".format(texpath))
	print("{} ----> Sucess !".format(pdfname))
	os.system("mv ./{} ./{}".format(pdfname, texfolder))
	os.system("mv ./{} {}".format(logname, texfolder))
	for file_extension in unnecessaries_extensions:
		os.system("rm *.{}".format(file_extension))
		print("*.{} ----> deleted !".format(file_extension))


tex_compil()
