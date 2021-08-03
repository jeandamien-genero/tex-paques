#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author : Jean-Damien Généro
Affiliation : French National Center for Scientific Research (CNRS)
Assigned at the Centre de recherches historiques (CRH, UMR 8558)
Date : 2021-08-02
Update :
python3 tex-compil.py ./xsl-paques.xsl ./1865-02-castan-barnabe/1865-02-09-castan-barnabe.xml
"""

import os
import re
import sys
from lxml import etree


xsl_file = sys.argv[1]
xml_file = sys.argv[2]


def xsl_transformation(xsl_file, xml_file):
    """
    Transforming xml file in tex file with an xslt stylesheet.
    :param xsl_file: path to an xsl stylesheet
    :type xsl_file: str
    :param xml_file: path to an xml file
    :type xml_file: str
    :return: tex file
    :rtype: lxml.etree._XSLTResultTree
    """
    # parsing xml file
    source = etree.parse(xml_file)
    # Remove namespace prefixes
    tei = source.getroot()
    for elem in tei.getiterator():
        elem.tag = etree.QName(elem).localname
    # Remove unused namespace declarations
    etree.cleanup_namespaces(tei)
    # xls transformation
    xsl_doc = etree.parse(xsl_file)
    xsl_transformer = etree.XSLT(xsl_doc)
    output_doc = xsl_transformer(source)
    return output_doc


def tex_compil() -> None:
    """
    Compiling a tex document.
    """
    unnecessaries_extensions = ["toc", "gz", "xml", "out", "blg", "bcf", "bbl", "aux"]
    tex = xsl_transformation(xsl_file, xml_file)
    texfolder = re.sub(r"(\.\/.+)\/.+\.xml", "\\1", xml_file)
    texname = re.sub(r"\.\/.+\/(.+)\.xml", "\\1.tex", xml_file)
    logname = re.sub(r"\.\/.+\/(.+)\.xml", "\\1.log", xml_file)
    pdfname = re.sub(r"\.\/.+\/(.+)\.xml", "\\1.pdf", xml_file)
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
