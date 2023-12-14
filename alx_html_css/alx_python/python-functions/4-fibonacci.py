def fibonacci_sequence(n):
    fibonacci = []
    if n==0 :
        return fibonacci
    if n==1 :
        fibonacci.append(0)
        return fibonacci
    if n>1 :
        fibonacci = [0,1]
        for i in range(2,n):
            fibo = fibonacci[i-1] + fibonacci[i-2]
            fibonacci.append(fibo)
    return fibonacci

