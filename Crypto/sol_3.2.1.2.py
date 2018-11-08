from pymd5 import md5,padding
from urllib import quote
import sys



def main():
    query=open(sys.argv[1],"r")
    command=open(sys.argv[2],"r")
    output=open(sys.argv[3],"w")

    x=query.readlines()
    token=x[0].split('&')[0].split("=")[1]
    user=x[0].split('&')[1]+'&'+x[0].split('&')[2]+'&'+x[0].split('&')[3]

    #user.append()
    #print(user)
    command3=command.readlines()[0]


    new_token=md5(state=token.decode("hex"),count=512)
    new_token.update(command3)

    pad=quote(padding(len(user)*8+8*8))
    command="token="+new_token.hexdigest()+'&'+user+pad+command3
    output.write(command)
    #print(command)



main()
