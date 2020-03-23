# MINORITY ODD OR EVEN REMOVER
# __________________________________________________________________________________________
# VARIABLE
# - Localize language: ID
textListNum='Jumlah angka yang ingin diproses:'
textNumIn='Masukan angka ke-'
textListIn='List yang akan diproses:'
textListOut='List hasil penghapusan:'
# __________________________________________________________________________________________
# FUNCTION
def minorityRemover(listIn):
    listEven=[]
    listOdd=[]
    for i in listIn:
        if i%2==0:
            listEven.append(i)
        else:
            listOdd.append(i)
    if len(listEven)>len(listOdd):
        return listEven
    else:
        return listOdd
def listNumIn(listNum):
    listIn=[]
    for i in range(listNum):
        numIn=int(input(f'{textNumIn}{i+1}: '))
        listIn.append(numIn)
    return listIn
# __________________________________________________________________________________________
# PROGRAM
listNum=int(input(f'{textListNum} '))
listIn=listNumIn(listNum)
print(f'\n{textListIn}\n{listIn}')
listOut=minorityRemover(listIn)
print(f'{textListOut}\n{listOut}')