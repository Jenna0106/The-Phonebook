import csv
def add():
    with open('Library.csv','a',newline='') as f:
        w=csv.writer(f)
        y=int(input('How many contacts are to be added? '))
        for i in range(y):
            x=int(input('Enter the contact to be added: '))
            z=input('Enter the owner of the contact: ')
            w.writerow([x,z])
        print('Data saved')

def remove():
    with open ('Library.csv') as f:
        s=csv.reader(f)
        rows=[]
        l=[]
        y=int(input('Number of contacts to be deleted:'))
        for rec in s:
            l.append(rec[1])
            rows.append(rec)
        print(l)
        for k in range(y):
            q=input('Enter the contact to be deleted: ')
            if q in l:
                for i in rows:
                    if i[1]==q:
                        rows.remove(i)
                print('Data deleted')
            else:
                print('contact not found')
    with open ('Library.csv','w',newline='') as g:
        w=csv.writer(g)
        for i in rows:
            w.writerow(i)

def display():
    with open("Library.csv","r")as f:
        s=csv.reader(f)
        print("NUMBER","%50s"%"OWNER")
        print('________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
        for i in s:
            print(i[0],"%20s"%i[1])
        print('________________________________________________________________________________________________________________________________________________________________________________________________________________________________')

def search():
    n=input("Enter the name of the contact to be searched")
    with open("Library.csv","r") as f:
        s=csv.reader(f)
        a=0
        for i in s:
            if i[1].lower()==n.lower():
                a=1
                break
        if a==1:
            print("%10s"%"contact Number","%10s"%"OWNER")
            print("%10s"%i[0],"%20s"%i[1])
        else:
            print("Not found")



c='yes'
while c=='yes' or c=='Yes' or c=='YES':
    print('-------------------------------------')
    print('            MENU                     ')
    print('-------------------------------------')
    print('1.Add a contact')
    print('2.Delete a contact')
    print('3.Display the contents')
    print('4.Search for your desired contact')
    print('____________________________________')
    x=int(input('Enter your choice:'))
    if x==1:
        add()
    elif x==2:
        remove()
    elif x==3:
        display()
    elif x==4:
        search()
    else:
        print('Invalid Choice')
    c=input('Do you want to go back to menu?(yes/no) ')
    print('THANK YOU!')
    print('_________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
    print('_________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
            
         
        
