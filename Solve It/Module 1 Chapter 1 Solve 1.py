# SIMPLE FORMULA
# __________________________________________________________________________________________
# VARIABLE
# - Localize language: ID
textOpen=(
    'Solve it! #1\n'
    'Diketahui W=((X+YxZ)/(XxY))^Z'
)
textInX='Nilai X : '
textInY='Nilai Y : '
textInZ='Nilai Z : '
textOut='Nilai W adalah'
# __________________________________________________________________________________________
# PROGRAM
print(textOpen)
x=int(input(textInX))
y=int(input(textInY))
z=int(input(textInZ))
w=((x+y*z)/(x*y))**z
print(f'{textOut} {w}')