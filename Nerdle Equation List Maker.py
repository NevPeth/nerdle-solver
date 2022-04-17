import random

numList = [1,2,3,4,5,6,7,8,9,0]
newList = {"5+7+7=19", "23-8-6=9"}
for x in range(10000000):
    a = random.choice(numList)
    b = random.choice(numList)
    c = random.choice(numList)
    d = random.choice(numList)
    e = random.choice(numList)
    f = random.choice(numList)
    de = int(str(d)+str(e))
    abc = int(str(a)+str(b)+str(c))
    if(a*b-c==de and len(str(de))==2):
        newList.add(str(a)+"*"+str(b)+"-"+str(c)+"="+str(de))
    if(a-b*c==de and len(str(de))==2):
        newList.add(str(a)+"-"+str(b)+"*"+str(c)+"="+str(de))
    if(de-b*c==a and len(str(de))==2):
        newList.add(str(de)+"-"+str(b)+"*"+str(c)+"="+str(a))
    if(a*b+c==de and len(str(de))==2):
        newList.add(str(a)+"*"+str(b)+"+"+str(c)+"="+str(de))
        newList.add(str(c)+"+"+str(b)+"*"+str(a)+"="+str(de))
    if(b!=0 and a+de/b==c and len(str(de))==2):
        newList.add(str(a)+"+"+str(de)+"/"+str(b)+"="+str(c))
    if(b!=0 and a+de-b==c and len(str(de))==2):
        newList.add(str(a)+"+"+str(de)+"-"+str(b)+"="+str(c))
        newList.add(str(de)+"-"+str(b)+"+"+str(a)+"="+str(c))
        newList.add(str(a)+"-"+str(b)+"+"+str(de)+"="+str(c))
    if(b!=0 and de/b+a==c and len(str(de))==2):
        newList.add(str(de)+"/"+str(b)+"+"+str(a)+"="+str(c))
    if(b!=0 and de/b-a==c and len(str(de))==2):
        newList.add(str(de)+"/"+str(b)+"-"+str(a)+"="+str(c))
    if(abc-de==f and len(str(abc))==3 and len(str(de))==2):
        newList.add(str(abc)+"-"+str(de)+"="+str(f))
    if(abc-f==de and len(str(abc))==3 and len(str(de))==2):
        newList.add(str(abc)+"-"+str(f)+"="+str(de))
    if(a+b+c==de and len(str(de))==2):
        newList.add(str(a)+"+"+str(b)+"+"+str(c)+"="+str(de))
    if(de!=0 and abc/de==f and len(str(abc))==3 and len(str(de))==2):
        newList.add(str(abc)+"/"+str(de)+"="+str(f))
    if(f!=0 and abc/f==de and len(str(abc))==3 and len(str(de))==2):
        newList.add(str(abc)+"/"+str(f)+"="+str(de))
    ab = int(str(a)+str(b))
    cd = int(str(c)+str(d))
    ef = int(str(e)+str(f))
    if(len(str(ab))==2 and len(str(cd))==2 and len(str(ef))==2 and ab+cd==ef):
        newList.add(str(ab)+"+"+str(cd)+"="+str(ef))
    if(len(str(ab))==2 and len(str(cd))==2 and len(str(ef))==2 and ab-cd==ef):
        newList.add(str(ab)+"-"+str(cd)+"="+str(ef))
    if(len(str(abc))==3 and len(str(ef))==2 and ef*d==abc):
        newList.add(str(ef)+"*"+str(d)+"="+str(abc))
        newList.add(str(d)+"*"+str(ef)+"="+str(abc))
    if(c!=0 and a*b/c==de and len(str(de))==2):
        newList.add(str(a)+"*"+str(b)+"/"+str(c)+"="+str(de))
    if(b!=0 and a/b*c==de and len(str(de))==2):
        newList.add(str(a)+"/"+str(b)+"*"+str(c)+"="+str(de))
    if(a+b-c==de and len(str(de))==2):
        newList.add(str(a)+"+"+str(b)+"-"+str(c)+"="+str(de))
        newList.add(str(b)+"-"+str(c)+"+"+str(a)+"="+str(de))
    if(len(str(ab))==2 and ab-c-d==e):
        newList.add(str(ab)+"-"+str(c)+"-"+str(d)+"="+str(e))
    if(c!=0 and len(str(de))==2 and a+b/c==de):
        newList.add(str(a)+"+"+str(b)+"/"+str(c)+"="+str(de))
    if(len(str(de))==2 and a*b*c==de):
        newList.add(str(a)+"*"+str(b)+"*"+str(c)+"="+str(de))
    if(de!=0 and len(str(de))==2 and a*b/de==c):
        newList.add(str(a)+"*"+str(b)+"/"+str(de)+"="+str(c))
    if(len(str(de))==2 and b!=0 and a/b*de==c):
        newList.add(str(a)+"/"+str(b)+"*"+str(de)+"="+str(c))
print(str(newList).replace("\'", "\""))
print(len(newList))
file = open('c:/Users/futur/Desktop/Python Scripts/File.txt', 'w')
file.write(str(newList).replace("\'", "\""))
# Forms, a*b-c=de and a-b*c=de and de-b*c=a and a*b+c=de and a+b*c=de and a+de/b=c and a+de-b=c and de-b+a=c and de/b+a=c and de/b-a=c 
# and abc-de=f and abc-f=de and a+b+c=de and abc/de=f and abc/f=de ab+cd=ef and ab-cd=ef and ef*d=abc and d*ef=abc and a*b/c=de 
# and a/b*c=de and a+b-c=de and a-b+c=de and ab-c-d=e and a+b/c=de and a*b*c=de