global D
D={}
global L
L=[]

def delete():
    global D
    global L
    
    i=int(input("Enter id to delete..\n"))
    ind=0
    for l in L:
        if i == L[ind]['id']:
            x=L.pop(ind)
            print("The following value deleted successfully",x)
        else:
            ind+=1

    cnt()
        
def updt():
    global D
    global L
    
    i=int(input("Enter id to update..\n"))
    ind=0
    for l in L:
        if i == L[ind]['id']:
            i=int(input("enter the id"))
            for l in L:
                ind1=0
                while(ind1<=len(L)-1):
                    if ind==ind1:
                        break        
                    elif i==L[ind1]["id"]:
                        print("Entered ID not available\nTry another")
                        i=int(input("enter the id"))
                        ind1=0
                    
                    else:
                        ind1+=1
            
            name=input("enter the name")
            salary=input("Enter the salary")
            L[ind]["id"]=i
            L[ind]["name"]=name
            L[ind]["salary"]=salary
            break
        else:
            ind+=1

    cnt()
        
    
def fin():
    global D
    global L
    i=int(input("Enter id to find..\n"))
    ind=0
    for l in L:
        if i == L[ind]['id']:
            print(L[ind])
        else:
            ind+=1

    cnt()


def emp1():
    D={}
    global L
    i=int(input("enter the id"))
    
    for l in L:
        ind=0
        while(ind<=len(L)-1):
            
            if i==L[ind]["id"]:
                print("Entered ID not available\nTry another")
                i=int(input("enter the id"))
                ind=0
            else:
                ind+=1
    name=input("enter the name")
    salary=input("Enter the salary")
    D['id']=i
    D['name']=name
    D['salary']=salary
    L.append(D)
    print("Value inserted Successfully..!!")
    
    cnt()
       
def cnt():
    ch=input("Do you want to continue...!!  (Y/N)")
    if(ch=="y" or ch=="Y"):
        get()
    else:
        pass
def dis():
    global D
    global L
    ind=0
    for l in L:
        
        s=str(L[ind]["id"])
        
        s1=str(L[ind]["name"])
        
        s2=str(L[ind]["salary"])
       
        print("---"*15)
        data=s+"   "+s1+"   "+s2
        print(data)
        ind+=1
    
    cnt()
    
def get():
    print('''Choose the option
    1.Enter the employee details
    2.Find
    3.Delete a record
    4.Update
    5.view
    6.exit''')
    ent=int(input("Enter the option"))
    
    
    if ent == 1:        
        emp1()
    elif ent==3:
        delete()
    elif ent==2:
        fin()
    elif ent==4:
        updt()
    elif ent==5:
        dis()
    elif ent==6:
        print('Thank you!!')
        pass
    else:
        print('invalid input')
        pass


          

if __name__=="__main__":
    get()
        




