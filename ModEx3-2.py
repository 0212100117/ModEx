def cube(a):
    return a**3, 6*a**2


volume, area = cube(3)
print('The volume of the cube is {} unit cube'.format(volume))
print('The area of the cube is {} unit square'.format(area))
