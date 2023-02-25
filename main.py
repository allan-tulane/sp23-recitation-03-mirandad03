"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))

    def __add__(self, other):
        return BinaryNumber(self.decimal_val + other.decimal_val)

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return [binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:])]

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y

def quadratic_multiply(x, y):
    return _quadratic_multiply(x, y).decimal_val

def _quadratic_multiply(x, y):
    xvec = x.binary_vec
    yvec = y.binary_vec
    
    xvec, yvec = pad(xvec, yvec)
    
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)
    
    x_left, x_right = split_number(xvec) 
    y_left, y_right = split_number(yvec)

    p1 = _quadratic_multiply(x_left, y_left)
    p2 = _quadratic_multiply(x_left, y_right)
    p3 = _quadratic_multiply(x_right, y_left)
    p4 = _quadratic_multiply(x_right, y_right)
    
    p1 = bit_shift(p1, 2*(len(xvec)//2))
    p2 = bit_shift(p2, len(xvec)//2)
    p3 = bit_shift(p3, len(xvec)//2)
    
    return (p1 + p2) + (p3 + p4)
   
## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
  a = BinaryNumber(1234)
  b = BinaryNumber(567)
  c = quadratic_multiply(a, b)
  print(c) 
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x, y)
    return (time.time() - start)*1000
    
test_multiply()
a = BinaryNumber(1234)
b = BinaryNumber(567)
timetaken = time_multiply(a, b, quadratic_multiply)
print("Elapsed time: %.2f ms" % timetaken)

