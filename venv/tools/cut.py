import jieba;
from string import digits;
import re;

def default_cut(sentence):
    #jieba默认
    return jieba.lcut(sentence,cut_all=False)

def all_cut(sentence):
    #全模式
    return jieba.lcut(sentence,cut_all=True)

def HMM_cut(sentence):
    #HMM
    return jieba.lcut(sentence,HMM=True)

def cutstopword(wdlist,stoppath):
    dirlist=[]
    fp=open(stoppath,"r",encoding='utf-8')
    stopwds=fp.readlines()
    stopwds = set(w.strip() for w in stopwds)
    for wd in wdlist:
        if wd in stopwds:
            continue
        else :
            dirlist.append(wd)
    while ' 'in dirlist:
        dirlist.remove(' ')
    return dirlist

def remove_badwd(text):
    #去除无关符号
    text = re.sub("[A-Za-z0-9\_\─\←\↓\+\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", text)
    text = text.replace('\r', '').replace('\n', '').replace('\t', '').replace('\u3000','')
    return text