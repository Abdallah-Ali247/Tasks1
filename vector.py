
def vector_scaler(s,v):
    """ function that mult a scaler and vector """
    l=[]
    for i in range(len(v)):
        l.append(v[i]*s)
    print(f"Input : {s} , {v}")
    print(f'New Vector is : {l}')


vector_scaler(2,[1,2,3])

def vector_scaler1(s,v):
    """ function that mult a scaler and vector """
    l=[]
    for i in v:
        l.append(i*s)
    print(f"Input : {s} , {v}")
    print(f'New Vector is : {l}')


vector_scaler1(2,[1,2,3])


























