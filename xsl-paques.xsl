<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tei="http://www.tei-c.org/ns/1.0"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="xs" version="2.0">
    <xsl:output method="text" indent="yes" encoding="UTF-8"/>
    <xsl:template match="/">\documentclass{article}
        \usepackage[utf8]{inputenc}
        \usepackage{xcolor}
        \usepackage[colorlinks=true, allcolors=darkgray]{hyperref}
        \usepackage{chngcntr}% http://ctan.org/pkg/chngcntr
        \counterwithout{subsubsection}{subsection}
        \renewcommand\thesubsection{\Roman{subsection}.}
        \renewcommand\thesubsubsection{§ \arabic{subsubsection}}
        \renewcommand*\contentsname{\centering{Sommaire}}
        
        \title{<xsl:value-of select="//titleStmt/title"/>\footnote{Ce texte, originellement publié dans \textit{<xsl:value-of select=".//monogr/title[@level='j']"/>} n°<xsl:value-of select="//monogr/biblScope[@unit='issue']"/>, <xsl:value-of select="//monogr/imprint/pubPlace"/>, <xsl:value-of select="//monogr/imprint/date/@when"/>, pp.<xsl:value-of select="//monogr/biblScope[@unit='page']/@from"/>-<xsl:value-of select="//monogr/biblScope[@unit='page']/@to"/>, a été encodé dans un document XML puis transformé en fichier \LaTeX{} grâce à une feuille de transformation XSL, par Jean-Damien Généro, ingénieur d'études du CNRS affecté au Centre de recherches historiques (UMR 8558/ CNRS-EHESS).}}
        \author{<xsl:value-of select="//titleStmt//author/forename"/><xsl:text> </xsl:text><xsl:value-of select="//titleStmt//author/surname"/>}
        \date{Valparaiso, 9 février 1865}
        
        \begin{document}
        \maketitle
        <xsl:apply-templates select="//text"/>
        \end{document}</xsl:template>
    <xsl:template match="//text//p">
        <xsl:apply-templates/>
    </xsl:template>
    <xsl:template match="//text//p"><xsl:text>
        
    </xsl:text><xsl:apply-templates/></xsl:template>
    <xsl:template match="//hi[@rend='i']">\textit{<xsl:value-of select="."/>}</xsl:template>
    <xsl:template match="//pb"><xsl:variable name="url_page"><xsl:value-of select="translate(./@facs, '#', '')"/></xsl:variable><xsl:text>\href{</xsl:text><xsl:value-of select="./ancestor::TEI/facsimile[@xml:id = $url_page]/graphic/@url"/><xsl:text>}{\textbf{[</xsl:text><xsl:value-of select="normalize-space(./@n)"/><xsl:text>]}}</xsl:text>
    </xsl:template>
    <xsl:template match="//note">\footnote{<xsl:value-of select="."/>}</xsl:template>
</xsl:stylesheet>