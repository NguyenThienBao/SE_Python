def main():
    a = 5
    b = 5.5
    c = a + b
    print(c)

    d = int(c)
    print(d)

    e = a + d
    f = a - d
    g = a * d
    h = a / d

    print(f'e = a + d - {e}, e = a + d - {f}, e = a + d - {g}, e = a + d - {h}')

    m = 5
    n = 6
    u = m / n
    p = int(m / n)

    print(f'u = {u}, p = {p}')




if __name__ == '__main__':
    print("Test !!!")
    main()