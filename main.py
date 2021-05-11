# -*- coding: UTF-8 -*-
import os
import sys
import requests
from lxml import etree

# https://www.cnblogs.com/darcymei/p/9397173.html
# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def getPMIDXMLs(PMIDFile):
    resultFile = 'run/ids/result.'+PMIDFile+'.xml'
    outputDir = 'run/outputs/'+PMIDFile.replace('.','_')
    outputFile = outputDir+'/'+PMIDFile+'.xml'
    
    with open(PMIDFile, 'r', encoding="utf-8") as f:
        PMIDList = f.read().splitlines()
        # print(PMIDList)
        
        
        if not os.path.exists('run/downloads/'):
            os.makedirs('run/downloads')
        
        i = 1
        for PMID in PMIDList:
            with open('./run/downloads/'+PMID+'.xml', 'w', encoding="utf-8") as result:
                url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id='+PMID
                print('正在下载 {1}/{2} PMID: {0}'.format(PMID, i, len(PMIDList)))
                res = requests.get(url)
                result.write(res.text)
            i += 1
        
        if not os.path.exists('run/ids/'):
            os.makedirs('run/ids')
        
        with open(resultFile, 'w', encoding="utf-8") as results:
            # https://www.cnblogs.com/hont/p/5412432.html
            pwd = os.path.abspath('.').replace('\\','/')+'/run/downloads/'
            # https://blog.csdn.net/shyrainxy/article/details/110594159
            PMXMLAbsPaths = list(pwd+id+'.xml' for id in PMIDList)
            results.write('<PMIDs><PMID>'+'</PMID><PMID>'.join(PMXMLAbsPaths) + '</PMID></PMIDs>')
        
    with open(resultFile, 'r', encoding="utf-8") as results:
        
        mergeXSL = resource_path(os.path.join("res",'merge.xsl'))
        if os.path.exists(mergeXSL):
            try:
                with open(mergeXSL, 'r', encoding="utf-8") as xsl:
                    print('正在合并……')
                    xslt = etree.parse(xsl)
                    xml = etree.parse(results)

                    transform = etree.XSLT(xslt)
                    merged = transform(xml)

                    if not os.path.exists(outputDir):
                        os.makedirs(outputDir)
                    
                    with open(outputFile, 'w', encoding="utf-8") as output:
                        output.write(str(merged))
                        print(PMIDFile+'：合并成功！执行完毕。')
            except Exception as e:
                print(e)
        else:
            print('找不到文件：'+mergeXSL)

# https://blog.csdn.net/yuanxiang01/article/details/79118113
dirs = os.listdir('.')
for file in dirs:                             # 循环读取路径下的文件并筛选输出
    if os.path.splitext(file)[1] == ".txt":   # 筛选txt文件
        print('找到 '+file)
        getPMIDXMLs(file)                     # 输出所有的txt文件

# import platform
# if (platform.system()=='Windows'):
#     os.system('pause')
input('按 Enter 键结束')
