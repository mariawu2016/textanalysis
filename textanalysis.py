#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,codecs
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import chardet
import jieba
import time

#遍历文件夹下txt文档  
def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L.append(os.path.join(root, file))
    return L

def save_to_file(list, filename):                                           
    with codecs.open(filename, 'a', encoding='utf-8') as f:                 
        #f.writelines(list)
        f.write(list)

def main(args):
    #获取当前文件夹下txt文件
    L=file_name(os.getcwd()+'/from')
    for l in L:
        lname=str(hash(os.path.splitext(l)[0]))
        #text=open(l,"rb").read()
        myfile = codecs.open(l,"r")
        str1 = myfile.read()                             
        #content = str1.replace("\n"," ")
        #content = content.decode('utf-8','ignore')   #使用utf-8解码成unicode格式
        #判断文本类型，并转为unicode

        wordlist = jieba.cut(str1,cut_all=True)
        wl = " ".join(wordlist)
        
        #保存结果
        save_to_file(wl,"./result/"+lname+os.path.split(l)[1])

        #设置词云 
        wc = WordCloud(background_color = "#fefefe", #设置背景颜色
                    #mask = "图片",  #设置背景图片 
                    width = 800,
                    height = 500,
                    max_words = 2000, #设置最大显示的字数  
                    #stopwords = "没有", #设置停用词  
                    font_path = "./fonts/vista.ttf",  
                    #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）  
                    max_font_size = 120,  #设置字体最大值  
                    random_state = 80, #设置有多少种随机生成状态，即有多少种配色方案
        )
        wc2 = wc.generate(wl)
        #myword = wc.generate(wl)#生成词云
        #展示词云图  
        #plt.imshow(myword)
        #plt.axis("off")
        #plt.show()
        #保存词云图
        wc2.to_file("./result/"+lname+"wordcloud.png")
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))