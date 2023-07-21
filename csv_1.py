import pickle
def add():
    fp = open('sample.dat','wb')
    
    n = int (input('enter number:'))
    for i in range(n):
        id_=int(input('enter id'))
        name = input('enter name')
        lst = [id_,name]
        pickle.dump(lst,fp)
        
    fp.close()

add()

