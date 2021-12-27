import math

print(math.log(8, 2))


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def p(value):
    return '{:.10f}'.format(value)


def getTheoretical_insertion(n, tn, x, tx, u):
    result = 100 * tn
    print("""
    (%u). To be proven = T(10 * %s) = T (%s)
    T(N) = cN^2 = T(%s) = %s       ----  practical measurement
    Therefore :
    T(10*N) = c(10N)^2 = cN^2 * 100 = T(N)* 100 = %s * 100 = %s  
    We have calculated T(%s) = %s
    But practically    T(%s) = %s 
    """ % (u, n, x, n, p(tn), p(tn), p(result), x, p(result), x, p(tx)))


def getC_merge(n, tn, x):
    c = round_up((tn / (n * math.log(n, 2))), 10)
    print("""
    To be proven = T(10 * %s) = T (%s)

    N = %s
    T(N) = c*N*LogN = %s           ------------- practical experiment
    c = T(N) / N*LogN = %s / (%s * Log%s) = %s
    """ % (n, x, n, p(tn), p(tn), n, n, p(c)))
    return c


def getTheoretical_merge(n, tn, x, tx):
    log10 = round_up(math.log(10, 2), 10)
    c = getC_merge(n, tn, x)
    result = round_up(((tn * 10) + (c * n * log10)), 10)
    print("""
    T(10 N) = c10NLog10N = 10*T(N) + 10*c*N*Log10
    Therefore :
    T(10 * %s) = (10 * %s) + (10 * %s * %s * %s )= %s
    We have calculated T(%s) = %s
    But practically    T(%s) = %s
    """ % (n, p(tn), p(c), n, p(log10), p(result), x, p(result), x, p(tx)))


def getC_quick(n, tn, x):
    c = round_up((tn / (n * math.log(n, 2))), 10)
    print("""
    To be proven = T(10 * %s) = T (%s)

    N = %s
    T(N) = c*N*LogN = %s           ------------- practical experiment
    c = T(N) / N*LogN = %s / (%s * Log%s) = %s
    """ % (n, x, n, p(tn), p(tn), n, n, p(c)))
    return c


def getTheoretical_quick_median(n, tn, x, tx):
    log10 = round_up(math.log(10, 2), 10)
    c = getC_quick(n, tn, x)
    result = round_up(((tn * 10) + (c * n * log10)), 10)
    print("""
    T(10 N) = c10NLog10N = 10*T(N) + 10*c*N*Log10
    Therefore :
    T(10 * %s) = (10 * %s) + (10 * %s * %s * %s )= %s
    We have calculated T(%s) = %s
    But practically    T(%s) = %s
    """ % (n, p(tn), p(c), n, p(log10), p(result), x, p(result), x, p(tx)))


def getC_binary(n, tn, x):
    c = round_up(tn / math.log(n, 2), 10)
    print("""
    To be proven = T(10 * %s) = T (%s)

    N = %s
    c = T(N) / LogN = %s / Log%s = %s
    """ % (n, x, n, p(tn), p(n), p(c)))
    return c


def getTheoretical_binary(n, tn, x, tx):
    log10 = round_up(math.log(10, 2), 10)
    c = getC_binary(n, tn, x, )
    result = round_up((tn + c * log10), 10)
    print("""
    T(10 N) = c Log10N = c LogN + c Log10 = T(N) + c Log10
    Therefore :
    T(10 * %s) = T(%s) + %s * %s = %s
    We have calculated T(%s) = %s
    But practically    T(%s) = %s
    """ % (n, n, p(c), p(log10), p(result), x, p(result), x, p(tx)))


insertion = [0.0525046667, 5.4508064333, 503.1272646333, 418995.591001122]
binary = [0.0000260667, 0.0000408667, 0.0000420667, 0.0000520667]
merge = [0.0039567, 1.9126667, 23.6859572333, 350.2600634]
median = [0.0030661, 0.26545292, 7.02600634, 149.2600634]
y = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]

print('**' * 30, '  Quick Sort Median of three pivot')
for i in range(0, len(y)):
    if i == 3: break
    getTheoretical_quick_median(y[i], median[i], y[i + 1], median[i + 1])
    print('--' * 20)
print(math.log(8, 2))

print('**' * 30, '  Merge Sort')
for i in range(0, len(y)):
    if i == 3: break
    getTheoretical_merge(y[i], merge[i], y[i + 1], merge[i + 1])
    print('--' * 20)
print(math.log(8, 2))

print('**' * 30, '  Insertion Sort')
for i in range(0, len(y)):
    if i == 3: break
    getTheoretical_insertion(y[i], insertion[i], y[i + 1], insertion[i + 1], i + 1)
    print('--' * 20)
print(math.log(8, 2))
print('**' * 30, '  Binary Search')
for i in range(0, len(y)):
    if i == 3: break
    getTheoretical_binary(y[i], binary[i], y[i + 1], binary[i + 1])
    print('--' * 20)
print(math.log(8, 2))
