import sys
sys.path.append("./tools")
sys.path.append("./models")
from sklearn.naive_bayes import MultinomialNB
import dataset
import pickle
import renamefile
import os
import gc
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from numpy import *
import numpy as np

def bayes_train():
    #数据集目录
    trainpath_1 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\训练1"
    trainpath_0 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\训练0"

    train_1, target_1, fname_tr1 = dataset.get_dataortarget(trainpath_1, 1)
    train_0, target_0, fname_tr2 = dataset.get_dataortarget(trainpath_0, 0)
    train_word, target_x = dataset.join_dataortarget(train_1, target_1, train_0, target_0)
    fname_train=join_dataname(fname_tr1,fname_tr2)
    del train_0, target_0, train_1, target_1
    gc.collect()

    clf_bayes = MultinomialNB()
    try:
        vectorizer=dataset.create_wordmap(train_word,"word.txt")
    except IOError:
        vectorizer=dataset.load_wordmap("word.txt")
    train_x = dataset.create_vector(train_word, vectorizer)
    train_mx = train_x.todense()

    clf_bayes.fit(train_mx, target_x)
    mod_func.save_model(clf_bayes,"bayes_model")
    return clf_bayes

def bayes_test():
    testpath_1 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\测试1"
    testpath_0 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\测试0"

    test_1, test_target_1, fname_t1 = dataset.get_dataortarget(testpath_1, 1)
    test_0, test_target_0, fname_t2 = dataset.get_dataortarget(testpath_0, 0)
    test_word, target_tx = dataset.join_dataortarget(test_1, test_target_1, test_0, test_target_0)
    fname_test = join_dataname(fname_t1, fname_t2)

    del test_target_1,test_0,test_target_0
    gc.collect()
    try:
        clf_bayes = mod_func.load_model("bayes_model")
    except IOError:
        clf_bayes = bayes_train()
    vectorizer = dataset.load_wordmap("word.txt")
    test_x = dataset.create_vector(test_word, vectorizer)
    test_mx = test_x.todense()
    predicted_porb=












def bayes_toLDA():
    #data
    trainpath_1 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\训练1"
    trainpath_0 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\训练0"
    testpath_1 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\测试1"
    testpath_0 = r"C:\Users\Administrator\Desktop\日常\毕业设计\dataset\随意测试\测试0"

    train_1,target_1,fname_tr1=dataset.get_dataortarget(trainpath_1,1)
    train_0,target_0,fname_tr2=dataset.get_dataortarget(trainpath_0,0)
    test_1, test_target_1,fname_t1= dataset.get_dataortarget(testpath_1, 1)
    test_0, test_target_0,fname_t2= dataset.get_dataortarget(testpath_0, 0)
    train_word,target_x=dataset.join_dataortarget(train_1,target_1,train_0,target_0)
    test_word,target_tx=dataset.join_dataortarget(test_1,test_target_1,test_0,test_target_0)
    #测试和训练分离

    del train_0,target_0,train_1,target_1,test_1,test_target_1,test_0,test_target_0
    gc.collect()

    clf_bayes=MultinomialNB()
    try:
        vectorizer=dataset.create_wordmap(train_word,"word.txt")
    except IOError:
        vectorizer=dataset.load_wordmap("word.txt")

    train_x = dataset.create_vector(train_word, vectorizer)
    test_x=dataset.create_vector(test_word,vectorizer)
    train_mx=train_x.todense()
    test_mx=test_x.todense()

    clf_bayes.fit(train_mx,target_x)
    ##############
    predicted_porb=clf_bayes.predict_proba(test_mx)
    #print(predicted)

    #@为垃圾的概率
    param_recall_prob=0.00000000001

    resort_index=list()
    for i in range(len(predicted_porb)):
        sum_prob=predicted_porb[i][0]+predicted_porb[i][1]
        if predicted_porb[i][1]/sum_prob<1-param_recall_prob and predicted_porb[i][1]/sum_prob>param_recall_prob:
            resort_index.append(i)
    #test_mx = delete(test_mx, resort_index, axis=0) 删除矩阵相关的行
    test_word_toLDA=list()
    for i in range(len(resort_index)):
        test_word_toLDA.append(test_word[resort_index[i]])

    #print(test_word_toLDA)

    num_del=0
    target_toLDA=list()
    for i in range(len(resort_index)):
        target_toLDA.append(target_tx[resort_index[i]-num_del])
        num_del=num_del+1
    return test_word_toLDA,target_toLDA




bayes_toLDA()


