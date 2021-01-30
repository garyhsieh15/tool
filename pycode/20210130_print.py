

Tn = [1.1, 2.1, 3.1 , 4.1, 5.1]
Wn = []
for i in Tn:
    Wn.append(2 * 3.1415926 / i)

ksee = 0.05
delta_t = 0.005

print(" ------------------------------------------------------------------------------ ")
print("%12s %12s %12s %12s" % ("Tn", "Wn", "delta_t", "ksee"))
print(" ------------------------------------------------------------------------------ ")
print("%+12.4f %+12.4f %+12.4f %+12.4f" % (Tn[0], Wn[0], ksee, delta_t))
