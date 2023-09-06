def some_linear_function(n):
    pass

def some_quadratic_function(n):
    pass

'''
n * n * O(1)
n * n * n * O(1)


// O(n^3)
'''
def function_a(n):
    for i in range(n):
        for j in range(n):
            x = 1 + 1 # constant and does not depend on n
        for j in range(n):
            for k in range(n):
                y = 2 + 2 # constant and does not depend on n


'''
n * n * O(n)

// O(n^3)
'''
def function_b(n):
    for i in range(n):
        for j in range(n):
            # This function is O(n):
            some_linear_function(n)



'''
n * O(h^2) <- constant lang ung h^2 kasi 25 rekta square lang
n * O(1)

// O(n)
'''
def function_c(n):
    h = 5
    for i in range(n):
        # This function is O(n^2):
        some_quadratic_function(h)


'''
O(k) * O(n)

// O(n * k)
'''
def function_d(n):
    k = 1000000000
    for i in range(k):
        for j in range(n):
            print("Pokemon 591")

'''
j * k^2 * O(k^2) * O(j^3)
O(j * k^2 * k^2 * j^3)

// O(j^4 * k^4)
'''
def function_e(j, k):
    for n in range(j + 1000000):
        for m in range(k * k):
            # This function is O(n^2)
            # dummy_call_n2(k)
            # This function is O(n^3)
            # dummy_call_n3(j)
            print("Pig scientific name")


'''
sqrt(n) * i^2 * i

// O(sqrt(n) * i^3)
'''
def function_f(n):
    #for i in range(sqrt(n)):
        # dummy_call_n2(i)
        #for j in range(i):
            print("25th Island")
            print("of Greece")