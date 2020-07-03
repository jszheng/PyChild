for a, b, c, d, e, f, g, h in range(8):
    N = [
        {b, c, d, e, f},
        {c, e},
        {d},
        {e},
        {f},
        {c, g, f},
        {f, h},
        {f, g}
    ]

    print(b in N[a])