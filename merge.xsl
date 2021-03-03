<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
    <xsl:template match="/">
        <PubmedArticleSet>
            <xsl:for-each select="PMIDs/PMID">
                <xsl:variable name="dName">results/<xsl:value-of select="." />.xml</xsl:variable>
                <xsl:copy-of select="document($dName)/PubmedArticleSet/PubmedArticle" />
            </xsl:for-each>
        </PubmedArticleSet>
    </xsl:template>

    <xsl:output
        method="xml"
        version="1.0"
        doctype-public="-//NLM//DTD PubMedArticle, 1st January 2019//EN"
        doctype-system="https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd"
        indent="yes"/>
</xsl:stylesheet>