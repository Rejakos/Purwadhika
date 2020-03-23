# VOWEL REMOVER
# __________________________________________________________________________________________
# VARIABLE
# - Localize language: ID
textIn='Masukan kata yang akan dihapus huruf vokalnya:\n'
textOut='Hasil dari Vowel Remover adalah:\n'
# __________________________________________________________________________________________
# FUNCTION
def vowRemover(inText):
    for i in 'aiueo':
        return i not in inText
# __________________________________________________________________________________________
# PROGRAM
inText=input(f'{textIn}')
vowRemoved=filter(vowRemover,inText)
vowRemoved=''.join(vowRemoved)
print(f'{textOut}{vowRemoved}')