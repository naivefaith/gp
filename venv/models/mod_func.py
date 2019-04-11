import sklearn
import pickle

def save_model(model,name):
    #保存模型
    DEFUALT_PATH = "../models/"
    DEFUALT_PATH = DEFUALT_PATH + str(name)
    mod_info=pickle.dumps(model)
    if os.access(DEFUALT_PATH, os.F_OK):
        raise IOError("File have exiested!")
    else:
        f=open(DEFUALT_PATH,'wb')
        f.write(mod_info)
        f.close()
    return 0

def load_model(name):
    #加载模型
    DEFUALT_PATH = "../models/"
    DEFUALT_PATH = DEFUALT_PATH + str(name)
    if os.access(DEFUALT_PATH,os.F_OK):
        f=open(DEFUALT_PATH, 'rb')
        mod_info=f.read()
        f.close()
        model=pickle.loads(mod_info)
    else:
        raise IOError("File is not exist!")
    return model

