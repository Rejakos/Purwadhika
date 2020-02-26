# SIMPLE FORMULA
# __________________________________________________________________________________________
# VARIABLE
# - Localize language: ID
textOpen=(
    'Solve it! #1',
    'Diketahui W=((X+YxZ)/(XxY))^Z'
)
textInX='Nilai X:'
textInY='Nilai Y:'
textInZ='Nilai Z:'
textOut='Nilai W adalah'
# __________________________________________________________________________________________
# PROGRAM
print(f'\n{textOpen[0]}\n\n{textOpen[1]}\n')
x=int(input(f'{textInX} '))
y=int(input(f'{textInY} '))
z=int(input(f'{textInZ} '))
w=((x+y*z)/(x*y))**z
print(f'{textOut} {w}')