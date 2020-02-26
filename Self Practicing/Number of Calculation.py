# NUMBER OF CALCULATION
# __________________________________________________________________________________________
# VARIABLE
# - Localize language: ID
textOpen=(
    'Diketahui fungsi x akan mengalikan antar digit angka yang dimasukan.\n'
    'Program ini dapat mengetahui berapa kali fungsi x akan diproses\n'
    'sampai didapatkan angka terakhir yang berjumlah 1 digit\n'
    'sehingga tidak dapat lagi diproses oleh fungsi x.\n\n'
    'Misal:\n'
    'Angka yang dimasukan: 399\n'
    '399: 3 x 3 x 9 = 243 (pertama)\n'
    '243: 2 x 4 x 3 = 24  (kedua)\n'
    '24 : 2 x 4     = 8   (ketiga)\n'
    'Angka 399 dapat dikalkulasikan dengan fungsi x sebanyak 3 kali\n'
)
textIn='Angka yang dimasukan: '
textOut=('Angka','dapat dikalkulasikan dengan fungsi x sebanyak','kali')
# __________________________________________________________________________________________
# FUNCTION
def numCalc(numIn):
    check=0
    numList=list(numIn)
    num=int(numIn)
    while num>9:
        x=1
        for i in numList:
            i=int(i)
            x*=i
        num=x
        numStr=str(num)
        numList=list(numStr)
        check+=1    
    return check
# __________________________________________________________________________________________
# PROGRAM
print(textOpen)
numIn=input(textIn)
numCalc=numCalc(numIn)
print(f'{textOut[0]} {numIn} {textOut[1]} {numCalc} {textOut[2]}')