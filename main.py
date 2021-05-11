import os
import requests
from lxml import etree

def getPMIDXMLs(PMIDFile):
    resultFile = 'result.'+PMIDFile+'.xml'
    outputFile = 'output.'+PMIDFile+'.xml'
    
    with open(PMIDFile, 'r', encoding="utf-8") as f:
        PMIDList = f.read().splitlines()
        # print(PMIDList)
        
        
        if not os.path.exists('results/'):
            os.makedirs('results')
        
        i = 1
        for PMID in PMIDList:
            with open('./results/'+PMID+'.xml', 'w', encoding="utf-8") as result:
                url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id='+PMID
                print('正在下载 {1}/{2} PMID: {0}'.format(PMID, i, len(PMIDList)))
                res = requests.get(url)
                result.write(res.text)
            i += 1
        
        with open(resultFile, 'w', encoding="utf-8") as results:
            results.write('<PMIDs><PMID>'+'</PMID><PMID>'.join(PMIDList) + '</PMID></PMIDs>')
        
    with open(resultFile, 'r', encoding="utf-8") as results:
        
        mergeXSL = 'merge.xsl'
        if os.path.exists(mergeXSL):
            with open(mergeXSL, 'r', encoding="utf-8") as xsl:
                print('正在合并……')
                xslt = etree.parse(xsl)
                xml = etree.parse(results)

                transform = etree.XSLT(xslt)
                merged = transform(xml)

                with open(outputFile, 'w', encoding="utf-8") as output:
                    output.write(str(merged))
                    print(PMIDFile+'：合并成功！执行完毕。')
        else:
            print('找不到文件：'+mergeXSL)

# https://blog.csdn.net/yuanxiang01/article/details/79118113
dirs = os.listdir('.')
for file in dirs:                             # 循环读取路径下的文件并筛选输出
    if os.path.splitext(file)[1] == ".txt":   # 筛选txt文件
        print('找到'+file)
        getPMIDXMLs(file)                     # 输出所有的txt文件

# import platform
# if (platform.system()=='Windows'):
#     os.system('pause')
input('按 Enter 键结束')
