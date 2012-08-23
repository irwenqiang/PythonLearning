def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

def mult3(n):
    if n == 1:
        return 3
    else:
        return 3 + mult3(n - 1)

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

# don't understand yet!
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))
