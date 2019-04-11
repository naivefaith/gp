import sys
import sklearn
import os
import renamefile
import cut
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.decomposition import PCA

import sklearn.naive_bayes as sk_bayes

def load_dataset(DATAPATH):
    #载入数据,输出list
    #慎用
    DATAPATH=renamefile.transpath(DATAPATH)
    filelist=[]
    filenamelist=[]
    files=os.listdir(DATAPATH)
    for f in files:
        olddir=os.path.join(DATAPATH,f)
        if os.path.isdir(olddir):
            continue
        fp=open(olddir,"r",encoding="utf-8")
        filelist.append(fp.read())
        filenamelist.append(olddir)
        fp.close()
    return filelist,filenamelist

def depose_dataset(filelist):
    #对数据进行停用词及其他符号处理,输出分词完毕的中文list
    #慎用
    STOPPATH=r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\stopword.txt"
    STOPPATH = renamefile.transpath(STOPPATH)
    train_data=list()
    for each in filelist:
        each=cut.remove_badwd(each)
        wordlist=cut.all_cut(each)
        wordlist=cut.cutstopword(wordlist,STOPPATH)
        wdstr=""
        wdstr=" ".join(wordlist)
        train_data.append(wdstr)
    return train_data

def get_dataortarget(datapath,target):
    #输出数据和标注
    #已封装
    testdata,targettest=[],[]
    filelist,filenamelist=load_dataset(datapath)
    testdata=depose_dataset(filelist)
    for i in range(len(testdata)):
        targettest.append(target)
    return testdata,targettest,filenamelist

def join_dataortarget(data1,target1,data2,target2):
    #对训练集和标注归并
    data1+=data2
    target1+=target2
    return data1,target1

def join_dataname(fname_1,fname_2):
    fname_1+=fname_2
    return fname_1

def create_wordmap(maptext,modelname):
    #构建词汇表并持久化
    DEFUALT_PATH="./"
    DEFUALT_PATH=DEFUALT_PATH+str(modelname)
    vectorizer = CountVectorizer()
    vectorizer.fit(maptext)
    mod_info=pickle.dumps(vectorizer)
    if os.access(DEFUALT_PATH, os.F_OK):
        raise IOError("File have exiested!")
    else:
        f=open(DEFUALT_PATH,'wb')
        f.write(mod_info)
        f.close()
    return vectorizer

def load_wordmap(modelname):
    #读取词汇表
    DEFUALT_PATH = "./"
    DEFUALT_PATH = DEFUALT_PATH + str(modelname)
    if os.access(DEFUALT_PATH,os.F_OK):
        f=open(DEFUALT_PATH, 'rb')
        mod_info=f.read()
        f.close()
        vectorizer=pickle.loads(mod_info)
    else:
        raise IOError("File is not exist!")
    return vectorizer

def create_vector(textdata,vectorizer):
    #建立词向量
    vec_train=vectorizer.transform(textdata)
    return vec_train

def pca_wordvec(train_x):
    #降维返回pca转换规则
    #@n_components
    pca=PCA(n_components=40)
    pca.fit(train_x)
    return pca

#print(v2)




