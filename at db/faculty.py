def faculty(n):
    print ('faculty has been called with n = ' + str(n))
    if n == 1:
        return 1
    else:
        res = n * faculty(n - 1)
        print("intermediate result for ", n, " * faculty(" ,n-1, "): ",res)
        return res

print(faculty(5))
