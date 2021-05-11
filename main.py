with open('pmid-transcript-set.txt', 'r', encoding="utf-8") as f:
    PMIDList = f.read().splitlines()
    # print(PMIDList)
    
    import requests
    import os
    if not os.path.exists('results/'):
        os.makedirs('results')
    for PMID in PMIDList:
        with open('./results/'+PMID+'.xml', 'w', encoding="utf-8") as result:
            url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id='+PMID
            res = requests.get(url)
            result.write(res.text)
    
    with open('result.xml', 'w', encoding="utf-8") as results:
        results.write('<PMIDs><PMID>'+'</PMID><PMID>'.join(PMIDList) + '</PMID></PMIDs>')
    
with open('result.xml', 'r', encoding="utf-8") as results:
    from lxml import etree
    with open('merge.xsl', 'r', encoding="utf-8") as xsl:
        xslt = etree.parse(xsl)
        xml = etree.parse(results)

        transform = etree.XSLT(xslt)
        merged = transform(xml)

        with open('output.xml', 'w', encoding="utf-8") as output:
            output.write(str(merged))
