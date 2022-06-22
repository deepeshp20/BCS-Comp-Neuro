#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_menu():
    print("MENU\nType one of the following letter to do as stated")
    print("P: print array")
    print("A: add number")
    print("S: sort array")
    print("R: number at rth position if the array is sorted")
    print("N: disallow/allow duplicate entries")
    print("Q: quit ")


# In[2]:


arr=[]


# In[ ]:


ue=False
while 1:
    print_menu()
    c= input("type the command ")
    
    if(c=='P'):
        print("\n")
        print(arr)
        print("\n")
        
    elif(c=='A'):
        num=int(input("type the number you want to add "))
        if(ue==True):
            i=0
            for x in arr:
                if(num==x):
                    print("\nnumber is alredy present\n")
                    break
                i=i+1
            if(i==len(arr)):
                arr.append(num)
        else:
            arr.append(num)
        flag=0
        
    elif(c=='S'):
        t=input("to sort small to large type \"s\" otherwise to sort large to small type \"l\" ")
        if(t=='s'):
            arr.sort()
        if(t=='l'):
            arr.sort(reverse=True)
        flag=1
        print("\narray is sorted\n")
        
    elif(c=='R'):  
        if(flag==1):
            index=int(input("Type the rth position you want search "))
            print("\n",arr[index])
            print("\n")
        else:
            print("\narray is not sorted\n")
            
    elif(c=='N'):
        if(ue==False):
            ue=True
        else:
            ue=False
            
    elif(c=='Q'):
        break 
        
    else:
        print("\nInvalid Command")

