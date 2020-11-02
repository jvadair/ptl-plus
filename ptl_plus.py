import os
from time import sleep
from math import sqrt

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
print("jvadair's ptl+")
sleep(5)

def find_perpendicular(x, original_slope):
    slope = -1/original_slope
    fractslope = '-1/' + str(original_slope)
    y = x[1]
    x = x[0]
    if x < 0:
        xx = float(str(x)[1:])
    elif x == 0:
        xx = 0
    else:
        xx = float('-' + str(x))
    if y < 0:
        y_operator = ' + '
        yy = float(str(y)[1:]) # Originally failed because i typed an x :/
    else:
        y_operator = ' - '
        yy = float('-' + str(y))
    if x < 0:
        x_operator = ' + '
        x = float(str(x)[1:])
    else:
        x_operator = ' - '
    print(yy)
    data = slope * xx
    data = data - yy
    if data < 0:
        data = str(data)
    else:
        data = '+' + str(data)
    return {'equation': 'y' + y_operator + str(y) + ' = ' + str(slope) + '(x ' + x_operator + str(x) + ')', 'simplified': 'y = ' + str(slope) + 'x ' + str(data), 'slope': slope, 'fractslope': fractslope}

def find_parallel(x, slope):
    y = x[1]
    x = x[0]
    if x < 0:
        xx = float(str(x)[1:])
    elif x == 0:
        xx = 0
    else:
        xx = float('-' + str(x))
    if y < 0:
        y_operator = ' + '
        yy = float(str(x)[1:])
    else:
        y_operator = ' - '
        yy = float('-' + str(y))
    if x < 0:
        x_operator = ' + '
        x = float(str(x)[1:])
    else:
        x_operator = ' - '
    data = slope * xx
    data = data - yy
    if data < 0:
        data = str(data)
    else:
        data = '+' + str(data)
    return {'equation': 'y' + y_operator + str(y) + ' = ' + str(slope) + '(x ' + x_operator + str(x) + ')', 'simplified': 'y = ' + str(slope) + 'x ' + str(data), 'slope': slope}

def solve(a, b):
    for i in range(0, len(a)):
        if a[i] == 'x':
            a_slope = float(a[4:i])
            a_y_intercept = float(a[i + 2:])
    a_y_intercept = str(a_y_intercept)
    if a_y_intercept.startswith('+'):
        a_y_intercept = float(a_y_intercept[1:])
    else:
        a_y_intercept = float(a_y_intercept)
    for i in range(0, len(b)):
        if b[i] == 'x':
            b_slope = float(b[4:i])
            b_y_intercept = float(b[i + 1:])
    b_y_intercept = str(b_y_intercept)
    print('\n\n' + str(a_y_intercept) + '\n\n')
    if b_y_intercept.startswith('+'):
        b_y_intercept = float(b_y_intercept[1:])
    else:
        b_y_intercept = float(b_y_intercept)
    # print(a_y_intercept)
    # print(b_y_intercept)
    # print(a_slope)
    # print(b_slope)
    eq_one = b_y_intercept - a_y_intercept
    eq_two = a_slope - b_slope
    # print(eq_one)
    # print(eq_two)
    x_value = eq_one/eq_two
    y_value = x_value * a_slope + a_y_intercept
    if a_y_intercept < 0:
        ay_op = ''
    else:
        ay_op = '+'
    return {'x_equation': str(eq_two) + 'x' + ' = ' + str(eq_one), 'x_value': x_value, 'y_value': y_value, 'y_equation': 'y = ' + str(x_value) + '*' + str(a_slope) + ay_op + str(a_y_intercept)}

def getdistance(a,b):
    d = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return {'distance':d, 'equation':'d = sqrt((' + str(a[0]) + ' - ' + str(b[0]) + ')² + (' + str(a[1]) + ' - ' + str(b[1]) + ')²)', 'step_two':str(a[0] - b[0]) + '² + ' + str(a[1] - b[1]) + '²', 'step_three':'sqrt(' + str((a[0] - b[0])**2 + (a[1] - b[1])**2) + ')'}
while True:
  clear()
  while True:
      try:
          coords = input('Enter coords of point ((x, y)): ')
          coords = eval(coords)
          if type(coords) is not tuple:
              raise Exception
          break
      except Exception as E:
          clear()
          print('Error, you may have mistyped')
          #print(E)
          #print(type(coords))
  clear()
  while True:
      try:
          linedata = input('Enter slope of line (y = mx+b) (with exact spacing): ')
          if not linedata.startswith('y = '):
              raise Exception
          for i in range(0,len(linedata)):
              if linedata[i] == 'x':
                  slope = float(linedata[4:i])
                  y_intercept = linedata[i+2:]
          break
      except Exception as E:
          clear()
          print('Error, you may have mistyped')
          #print(E)
          #print(type(coords))
  perpendicular_data = find_perpendicular(coords, slope)
  parallel_data = find_parallel(coords, slope)
  data = solve(perpendicular_data['simplified'], linedata)
  distance = getdistance((data['x_value'], data['y_value']), coords)
  clear()
  print('Point: ' + str(coords))
  print('Line: ' + linedata)
  print('---------------------------------------------------\nPerpendicular line\n')
  print(perpendicular_data['equation'])
  print(perpendicular_data['simplified'])
  print('Slope: ' + str(perpendicular_data['slope']))
  print('Slope as fraction: ' + perpendicular_data['fractslope'])
  print('---------------------------------------------------\nParallel line\n')
  print(parallel_data['equation'])
  print(parallel_data['simplified'])
  print('Slope: ' + str(parallel_data['slope']))
  print('---------------------------------------------------\nIntersection Point\n')
  print('Equation for x: ' + data['x_equation'])
  print('Equation for y: ' + data['y_equation'])
  print('Coordinates of intersection point: (' + str(data['x_value']) + ',' + str(data['y_value']) + ')')
  print('---------------------------------------------------\nDistance from point to line\n')
  print(distance['equation'])
  print(distance['step_two'])
  print(distance['step_three'])
  print('Distance: ' + str(distance['distance']))
  input('---------------------------------------------------\nPress enter to continue...')
  #reverse sign then add (in perp slope calc)