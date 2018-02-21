#! /usr/bin/env python
# -*- coding: utf-8 -*-


import os,codecs
import matplotlib.pyplot as plt
from wordcloud import WordCloud
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
        text=open(l,"rb").read()
        #调用结巴分词
        wordlist = jieba.cut(text,cut_all=True)
        wl = " ".join(wordlist)
        lname=str(hash(os.path.splitext(l)[0]))
        #保存结果
        save_to_file(wl,"./result/"+lname+os.path.split(l)[1])

        #设置词云 
        wc = WordCloud(background_color = "#fefefe", #设置背景颜色
                    #mask = "图片",  #设置背景图片  
                    max_words = 1000, #设置最大显示的字数  
                    #stopwords = "没有", #设置停用词  
                    font_path = "./fonts/vista.ttf",  
                    #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）  
                    max_font_size = 70,  #设置字体最大值  
                    random_state = 0, #设置有多少种随机生成状态，即有多少种配色方案
        )
        myword = wc.generate(wl)#生成词云
        #展示词云图  
        #plt.imshow(myword)
        #plt.axis("off")
        #plt.show()
        #保存词云图
        wc.to_file("./result/"+lname+"result.png")
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))