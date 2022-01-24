
a = None
b = None
c = None
d = None

result_a = a is None
result_b = b is not None
result_c = bool(bool(c) is not bool(c)) == False
result_d = bool(bool(d) is not bool(d)) == False and bool(d)
