
class Fibonacci_sequence:
    def fibonacci(self):
        j = int(input("number:"))
        count = 2
        n = 0
        old = 1
        x = 1
        while j < 0:
            j = int(input("The j cannot less 1"))
        fibonacci = []
        fibonacci.append(x)
        fibonacci.append(old)
        while count < j:
            n = x + old
            fibonacci.append(n)
            count +=1
            x = old + n
            fibonacci.append(x)
            count +=1
            old = n + x
            fibonacci.append(old)
            count +=1
        return fibonacci
fibonacci_sequence = Fibonacci_sequence()
fibonacci_list = fibonacci_sequence.fibonacci()
print(fibonacci_list)
for i in fibonacci_list:
    print(i,end=" ")

