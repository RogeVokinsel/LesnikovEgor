# for n in range(500):
#     r = bin(n)[2:]
#     if n % 2 == 0:
#         r = r + '10'
#     if n % 2 != 0:
#         r = '1' + r + '10'
#     c = int(r, 2)
#     if c > 441:
#         print(n)




# S = []                                                №18130
# for n in range(500):
#     r = bin(n)[2:]
#     if n % 3 == 0:
#         r = '1' + r[-2:] + '11'
#     if n % 3 != 0:
#         r = '10' + r + '0'
#     c = int(r, 2)
#     if c > 999 and n % 2 == 0:
#         S.append(c)
#         print(min(S))



# for n in range (500):                                               #6588
#     r = bin(n)[2:]
#     r = r.replace('1', '*')
#     r = r.replace('0', '#')
#     r = r.replace('*', '0')
#     r = r.replace('#', '1')
#     r = '1' + r
#     b = sum(map(int, list(r)))
#     if b % 2 == 0:
#         r = r + '0'
#     if b % 2 != 0:
#         r = r + '1'
#     a = int(r, 2)
#     if a > 180:
#         print(a, n)


