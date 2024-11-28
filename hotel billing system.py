items={1:'poha',2:'tea',3:'idli',4:'vada pav',5:'samosa',6:'dosa'}
price={1:20,2:10,3:30,4:15,5:20,6:40}
ik=[]
qua=[]
print('-'*100)
print(f"{' '*50} Hotel Raj")
print('-'*100)
while True:
    print("""
                              Menu
        
                        1.poha    2.tea 
                        3.idli    4.vada pav
                        5.samosa  6.dosa        
    """)
    item=int(input('enter item='))
    qunt=int(input('enter quantity='))
    ik.append(item)
    qua.append(qunt)
    ch=input('enter your choise (yes/no)')
    if ch=='no':
        
        print("-"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("itemname","quantity","price","amount"))
        print("-"*85)
        sum=0
        for i in range(len(ik)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(items[ik[i]],qua[i],price[ik[i]],qua[i]*price[ik[i]]))
            print("-"*85)
            sum=sum+price[ik[i]]*qua[i]
        break
print('Total amount =',sum)
print('Thank You visit again')
    


