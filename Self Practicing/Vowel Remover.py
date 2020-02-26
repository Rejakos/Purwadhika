# VARIABLE
# - Localize language: ID
textIn='Masukan kata yang akan dihapus huruf vokalnya:'
textOut='Hasil dari Vowel Remover adalah:'
# __________________________________________________________________________________________
# FUNCTION
def vowRemover(inText):
    for i in 'aiueo':
        return i not in inText
# __________________________________________________________________________________________
# PROGRAM
inText=input(f'{textIn}\n')
vowRemoved=filter(vowRemover,inText)
vowRemoved=''.join(vowRemoved)
print(f'{textOut}\n{vowRemoved}')