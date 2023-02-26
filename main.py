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

#Obtain xvec and yvec, the binary_vec values of x and y
    xvec = x.binary_vec
    yvec = y.binary_vec

#Pad xvec and yvec so they are the same length by adding leading 0s if necessary
    lenmax = max(len(xvec), len(yvec))
    xvec = ['0'] * (lenmax - len(xvec)) + xvec
    yvec = ['0'] * (lenmax - len(yvec)) + yvec

#Base case: If both x and y are ≤ 1, then just return their product.
    if x.decimal_val == 0 or y.decimal_val == 0:
        return BinaryNumber(0)
    if x.decimal_val == 1 and y.decimal_val == 1:
        return BinaryNumber(1)

#Otherwise, split xvec and yvec into two halves each. Call them x_left x_right y_left y_right
    x_left, x_right = split_number(xvec) 
    y_left, y_right = split_number(yvec)
  
#Now you can apply the formula above directly. Anywhere there is a multiply, call _quadratic_multiply. Use bit_shift to do the 2 n and 2 n/2 multiplications.
    form1 = _quadratic_multiply(x_left, y_left)
    form1 = bit_shift(form1, 2*(len(xvec)//2))
    form2 = _quadratic_multiply(x_left, y_right)
    form2 = bit_shift(form2, len(xvec)//2)
    form3 = _quadratic_multiply(x_right, y_left)
    form3 = bit_shift(form3, len(xvec)//2)
    form4 = _quadratic_multiply(x_right, y_right)    

  #Finally, you have to do three sums to get the final answer.    
    return (form1 + form2) + (form3 + form4)
   
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

#printing things out to get a better visual
test_multiply()
a = BinaryNumber(1234)
b = BinaryNumber(567)
timetaken = time_multiply(a, b, quadratic_multiply)
print("Time: %.2f ms" % timetaken)

