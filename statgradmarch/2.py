print('x y z w f')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f = (not (x or z) or (y and x)) and ((w == z) or (not w or not y))
                if f and y:
                    print(x, y, z, w, int(f))