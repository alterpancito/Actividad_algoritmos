def primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for i in range(2,100):
    if primo(i):
        print(i,end=' ')
