a = [9,8,7,6,5, 4, 3, 2, 1]
a2= range(1,18)


for j in a2:
    if j>=10:
            j=j-(2*(j-9))
    if j%2==1:
        b=j*"*"
        print(b.center(10))


# for i in a:
#     if i%2==1:
#         b=i*"*"
#         print(b.center(10))


# for i in a:
#     c="*"*i
#     print (c.rjust(10))
    

# for i in a2:
#     if i%2==1:
#         b=i*"*"
#         print(b.center(10))
