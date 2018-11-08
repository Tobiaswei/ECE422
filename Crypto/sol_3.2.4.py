import pbp
from fractions import gcd
from Crypto.PublicKey import RSA
from Crypto.Util import number

def producttree(X):
    result = [X]
    while len(result[-1]) > 1:
        X = result[-1]
        Y = []
        L = len(X)
        Y = [X[i*2]*X[i*2+1] for i in range(L/2)]
        if L % 2 == 1:
            Y.append(X[L-1])
        result.append(Y)
    return (result)
def remaindersusingproducttree(n,T):
       result = [n]
       for t in reversed(T):
         result = [result[(i//2)] % t[i] for i in range(len(t))]
       return result

def squaretree(T):
        Y=[]
        for j in range(len(T)):
            Y.append([T[j][i]**2 for i in range(len(T[j]))])
        return Y
def find_gcd(remainder_list,moduli_list):
    potential_pair=[]
    if len(remainder_list)==len(moduli_list):
        remainder_list=[remainder_list[i]/moduli_list[i] for i in range(len(moduli_list))]
        for r,m in zip(remainder_list,moduli_list):
             q=gcd(r,m)
             if (q>1):

                potential_pair.append((m,q))

    else:
        print("error, not pair")
        exit(1)

    return potential_pair
# recostruct RSA by useing the potential list
def find_private_key_list(potential_pair):
    e=65537
    private_keys=[]
    for each in potential_pair:

        p=each[0]/each[1]
        q=each[1]
        assert(number.isPrime(p))
        assert(number.isPrime(q))
        d = number.inverse(e, (p-1)*(q-1))
        private_keys.append(RSA.construct((long(each[0]),long(e),long(d))))

    return private_keys
def Decrypt_AES(keys,cipher_text):
    for key in keys:
        try:
            plaintext = pbp.decrypt(key, cipher_text)
            print(plaintext)
            return plaintext

        except ValueError:
            a=0

def main():
     with open("moduli.hex") as moduli:
         moduli_list=moduli.readlines()
         moduli_list=[each.strip() for each in moduli_list]
         moduli_list=[int(each,16) for each in moduli_list]

     with open("3.2.4_ciphertext.enc.asc") as cipher:
         cipher_text=cipher.read()

     print("calculating product tree......")
     pt=producttree(moduli_list)
     print("calculating square product tree......")
     pt_square=squaretree(pt)
     print("calculating remainder tree......")
     r_l=remaindersusingproducttree(pt[-1][0],pt_square)
     print("calculating potential moudli list......")
     potential_pair=find_gcd(r_l,moduli_list)
     print("calculating private keys......")
     private_keys=find_private_key_list(potential_pair)
     print("Decrpt Message......")
     plain_text=Decrypt_AES(private_keys,cipher_text)

main()
