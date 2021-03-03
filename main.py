with open('pmid-transcript-set.txt', 'r') as f:
    PMIDList = f.read().splitlines()
    # print(PMIDList)
    
    import requests
    import os
    os.makedirs('results')
    for PMID in PMIDList:
        with open('./results/'+PMID+'.xml', 'w') as result:
            url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id='+PMID
            res = requests.get(url)
            result.write(res.text)
    
    with open('result.xml', 'w') as results:
        results.write('<PMIDs><PMID>'+'</PMID><PMID>'.join(PMIDList) + '</PMID></PMIDs>')
    
with open('result.xml', 'r') as results:
    from lxml import etree
    with open('merge.xsl', 'r') as xsl:
        xslt = etree.parse(xsl)
        xml = etree.parse(results)

        transform = etree.XSLT(xslt)
        merged = transform(xml)

        with open('output.xml', 'w') as output:
            output.write(str(merged))
