cuts = 10000
per_length = 3 / cuts
per_distant = 3 / cuts
sum_prop = 0

for i in range(1, cuts + 1):
    height = 9 - (per_length ** 2)
    s = height * per_distant
    per_length = per_length + per_distant
    sum_prop = sum_prop + s

print(sum_prop)

print('========================================')


def prop(c):
    per_len = 3 / c
    per_dist = 3 / c
    tol_s = 0

    for i in range(1, c + 1):
        h = 9 - (per_len ** 2)
        per_s = h * per_dist
        per_len = per_len + per_dist
        tol_s = tol_s + per_s

    return tol_s

# Test
print(prop(10000))

