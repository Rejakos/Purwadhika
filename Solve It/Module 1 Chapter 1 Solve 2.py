# SQUARE
# __________________________________________________________________________________________
# VARIABLE
# - Localize language: ID
textOpen='Solve it! #2'
textIn='Nilai yang ingin diketahui kuadratnya:'
textOut=(
    'Kuadrat dari',
    'adalah'
)
# __________________________________________________________________________________________
# PROGRAM
print(f'\n{textOpen}\n')
num=int(input(f'{textIn} '))
sq=num**2
print(f'{textOut[0]} {num} {textOut[1]} {sq}')