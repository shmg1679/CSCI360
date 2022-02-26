import random
def MR_Test(n,s):
    if n%2==0:#all even numbers are false
        return False
    u=0
    p1=n-1
    while p1 % 2 == 0:
        u+=1
        p1//=2
    for i in range(1,s):#iterate it for s times
        a=random.randrange(2,n-1)
        z=pow(a,p1,n)
        if z==1 or z==n-1:
            continue
        for i in range(u-1):
            z=pow(z,2,n)
            if z==n-1:
                break
        else:
            return False
    return True

def get_prime():#recursive function until it gets a prime number
    a=random.randrange(2**512)
    if MR_Test(a,40)!=True:#not prime, try again
        return get_prime()
    else:
        return a           #prime, return it

def find_gcd_EA(a,b):  #recursive function to find gcd
    if(b==0):
        return a
    else:
        return find_gcd_EA(b,a%b)

def get_e(phi_N):       #get e with find gcd function
    e=random.randrange(1,phi_N-1)#get a random e from range 1 to phi of n-1
    if find_gcd_EA(phi_N,e)!=1:
        return get_e(phi_N)
    else:
        return e

def eea(a, b):
    if a == 0 :
        return b,0,1
    gcd,si,ti = eea(b%a, a)
    s= ti - (b//a) * si
    t = si
    return gcd,s,t

def get_d(phi_N,e):
    gcd,s,t=eea(phi_N,e)
    while t<0:
        t=t+phi_N
    return t

def powmod_sm(base, exp, n):
    exp_b = bin(exp)
    value = base
    for i in range(3, len(exp_b)): #0b1...0 or 1 skip 0b and the first 1
        value = (value**2)%n
        if(exp_b[i:i+1] == '1'):
            value = (value*base)%n
    return value

#main body of code
p=get_prime()
q=get_prime()
#uncomment the print() statement to use for seeing
# p and q and making sure they're prime
#print("P="+str(p)+"\n"+str(MR_Test(p,40)))
#print("Q="+str(q)+"\n"+str(MR_Test(q,40)))

n=p*q
phi_N=(p-1)*(q-1)   #phi of N = (p-1)(q-1)
#print("N=")
#print(n)
#print("phi of n=")
#print(phi_N)

e=get_e(phi_N)
#print("E=")
#print(e)

d=get_d(phi_N,e)
#print("d=")
#print(d)

print("Kpub:")
print("N=")
print(n)
print("E=")
print(e)
print("Kpr:")
print("d=")
print(d)

print("Encrypting with square and multiply algorithm")
x=int(input("Please enter a string of numbers:"))
enc=powmod_sm(x,e,n)#y=x^e mod n
print("Encryption=")
print(enc)
print("Decrypting encryption back to plain text:")
dec=powmod_sm(enc,d,n)
print("Decryption=")
print(dec)