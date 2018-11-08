import urllib2
url="http://72.36.89.198:8081/mp3/yuguang2/?"
def get_status(u):
    req=urllib2.Request(u)
    try:
        f=urllib2.urlopen(req)
        return f.code
    except urllib2.HTTPError,e:
        return e.code
# valid padding     
def crack_block(y,b):
    # Find the last oracle element 
    #r=[0xff]*16
    r=[0]*16
    x=[0]*16
    for w in range(0xff,-1,-1):
        r[15]=w    #format(w,'02x')
        #print r[15]
        r_block=''.join('{:02x}'.format(i)for i in r)
        #print(r_block)
        if valid_padding(r_block,y):
            x[15]=w^0x10
            #print("find the last orcale {}".format(r[15]))
            break   
    for j in range(14,-1,-1):
        
        for counter in range(j+1,b):
            #print (type(0x10-(counter-j)),type(x[counter]))
            r[counter]=(0x10-(counter-j))^x[counter]
            
            #r[counter]=format(temp,'02x') 

        for w in range(0xff,-1,-1):
            r[j]=w   #format(w,'02x')
            r_block=''.join('{:02x}'.format(i)for i in r)

            if valid_padding(r_block,y):
                x[j]=w^0x10
                #print(j,"find oracle as",x[j])
                #break
    #print x
    return x
        
    
def valid_padding(r,y):
    
    query=url+r+y
    if get_status(query)==404:
        return True
    else:
        return False


with open("3.2.3_ciphertext.hex") as cipher:
    cipher_text=cipher.read()
    y=[]
    x=[]
    for i in range(len(cipher_text)/2/16):
        y.append(cipher_text[i*32:(i+1)*32])# List for Yn
        
    for i in range(8):
        x.append(crack_block(y[i],16))
#x=crack_block(y[7],16)
y_block=[]
y_block=[[y[i][2*j:2*j+2] for j in range(16)]for i in range(8)]
for i in range(8):
    for j in range(16):
        y_block[i][j]=int(y_block[i][j],16)

x_block=[[0 for each in range(16)] for each in range(8)]
for i in range(7,0,-1):
        for j in range(16):
              x_block[i][j]=(y_block[i-1][j])^(x[i][j])
plaintext=[]
for i in range(1,8,1):
    for j in range(16):
        plaintext.append(x_block[i][j])
Read_text="".join(chr(p) for p in plaintext) 

print(Read_text)