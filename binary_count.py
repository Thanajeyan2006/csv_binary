import pickle
def count():
    fp = open('sample.dat','rb')
    c = 0
    try:
        while True:
            a = pickle.load(fp)
    
            c +=1
    except:
        fp.close()
        print(c)

count()