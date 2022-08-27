# febonachi
import  math
def Fibonachi():
    n = int(input("Введите порядковый номер последовательности Фибоначи : "))
    # formula Bine f(n)= (q^n-w^n)/5**0.5  where q=(1+5**0.2)/2 w=(1-5**0.2)/2
    q=(1+5**0.5)/2
    w=(1-5**0.5)/2
    for i in range(10):
        print (" Число с порядковым номером {}   :" .format(n+i-1),round((q**(n+i)-w**(n+i))/5**0.5))

    Fibonachi()
# neuron
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))
class Neuron:
    def __init__(self,weights,bias):
        self.bias=bias
        self.weights=weights
    def feedforward(self,input):
        total=np.dot(self.weights, input)+self.bias
        return sigmoid(total)
weights = np.array([0, 1])
bias = 4
n = Neuron(weights, bias)

x = np.array([2,3])
print(n.feedforward(x))

