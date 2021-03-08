# pubmedXML4CiteScape
## 针对问题
- [《新版 pubmed 不能导出 xml 格式的文件，但是想用 citespace 分析，怎么进行数据转换？》](https://www.zhihu.com/question/410257993)
- [《citespace 如何分析新版 pubmed 的文献数据？》](https://www.zhihu.com/question/403062331)
## 使用方法
- 在新版 PubMed 搜索结果点击 Save 按钮
- Selection 选 All results，Format 选 PMID
- 点击 Create file 下载到 pmid-transcript-set.txt 文件
- 覆盖我的示例 pmid-transcript-set.txt 文件
- 在控制台运行下列命令，产生的 output.xml 文件应该就是我们需要的XML文件了。
```
python main.py
```
## 注意事项
其中用到的两个Python包：requests 和 lxml 是需要事先安装好的。  
如何使用pip安装我就不赘述了，百度一下自然就有。
## 特别感谢
- 华天清大神在其博文[《Python使用xslt提取网页数据》](https://www.cnblogs.com/gooseeker/p/5501716.html)中提供的在 Python 中使用 xslt 的指导
