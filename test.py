


# data=open('database','a')
# uname='name'
# l='lllll'
# data.write(f'\n{uname} {l}')
data=open('database','r')
dline=data.readlines()

print(dline[1][1])


data.close()