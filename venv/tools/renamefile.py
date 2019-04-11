import os;

def rename(datapath):
    #起始编号
    i=0;
    filelist=os.listdir(datapath)
    for files in filelist:
        i=i+1
        olddir=os.path.join(datapath,files);
        if os.path.isdir(olddir):
            continue
        filename=os.path.splitext(files)[0]
        filetype=os.path.splitext(files)[1]
        newdir=os.path.join(datapath,str(i)+filetype)
        os.rename(olddir,newdir)

def transpath(path):
    path=path.replace("\\","/")
    return path

#rename("C:/Users/Administrator/Desktop/日常/毕业设计/dataset/垃圾邮件数据集/ham_all")
#rename("C:/Users/Administrator/Desktop/日常/毕业设计/dataset/垃圾邮件数据集/spam_all")

