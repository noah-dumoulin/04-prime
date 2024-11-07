"""module qui permet de savoir si un nombre est premier ou non"""
from math import sqrt
def isprime(p):
    '''retourne si le nombre en paramètre est premier ou non'''
    if p==1:
        return False
    s=int(sqrt(p))
    for i in range (2,s+1):
        if p%i==0:
            return False
    return True

def main():
    '''permet de faire des appels de la fonction isprime()'''
    print(isprime(19))
    print(isprime(9))
    print(isprime(55))
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
if __name__ == '__main__':
    main()
