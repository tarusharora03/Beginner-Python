large = 0
small = None
while True:
    num = input('Enter Number: ')
    if num == 'done':
        break
    try:
       n = int(num)
    except:
          print('Invalid input')
          print('Maximum is ',large)
          print('Minimum is ',small)
          break
    if n > large:
        large = n
    if small is None:
        small = n
    elif n < small:
        small = n
