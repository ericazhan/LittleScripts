import pandas as pd

# file="test.don"
# soil="min"

#--start def get_ctable(file,soil)
def get_combi(file,soil):
    resu = []
    # 1---get a concatenate table with 8 copy
    for i in range(1,9):
        data = pd.read_table(file,sep='\s+',dtype='str')
        data['0'] = str(900+i) + data['0'].astype(str)
        data.columns=data.columns.str.replace('330', '250')
        resu.append(data) # store DataFrame in list
        print(len(resu))
    resu = pd.concat(resu)

    # 2---get a lsit for fixed point coef
    tot=len(resu.index)
    num1=len(data.index)
    fp=[None]*tot
    fp_tot=[]
    for m in range(8):
        fp=[None]*tot
        fp[num1*m:num1*(m+1)]=[1]*num1
        for n in range(len(fp)):
            if fp[n]==None:
                fp[n]=0
        fp_tot.append(fp)

    # 3---add columns (fixed point coeff) to the dataframe
    sol={"min":0,"med":10,"max":20}
    for i in range(8):
        col=str(500+i+sol[soil])
        resu.insert(resu.columns.get_loc("250001"), col, fp_tot[i])

    resu.to_csv(file,index=False,sep='\t')


# get_combi("combill.txt")
import os
import fnmatch
path=os.getcwd()

for filenames in os.listdir('.'):
    if fnmatch.fnmatch(filenames,"*min.don"):
        print("min",filenames)
        get_combi(filenames,"med")
    elif fnmatch.fnmatch(filenames,"*med.don"):
        print("med",filenames)
        get_combi(filenames,"med")
    elif fnmatch.fnmatch(filenames,"*max.don"):
        print("max",filenames)
        get_combi(filenames,"max")




# for (dirpath, dirnames, filenames) in os.walk(path): #return (dirpath,dirnames,filenames)
    # print(filenames)

