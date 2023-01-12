TOIs={"mon":3,"tue":3,"wed":3,"thr":3,"fri":3,"sat":5,"sun":6}
TOI_sum=sum(TOIs.values())

HINDUs={"mon":2.5,"tue":2.5,"wed":2.5,"thr":2.5,"fri":2.5,"sat":4,"sun":4}
HINDU_sum=sum(HINDUs.values())

ETs={"mon":4,"tue":4,"wed":4,"thr":4,"fri":4,"sat":4,"sun":10}
ET_sum=sum(ETs.values())

BMs={"mon":1.5,"tue":1.5,"wed":1.5,"thr":1.5,"fri":1.5,"sat":1.5,"sun":1.5}
BM_sum=sum(BMs.values())

HTs={"mon":2,"tue":2,"wed":2,"thr":2,"fri":2,"sat":4,"sun":4}
HT_sum=sum(HTs.values())

budget=float(input("Enter weekly budget: "))
bud=budget
temp='{'
result=[]
news_paper=['TOI','HINDU','ET','BM','HT']
np_cost=[26,20.5,34,10.5,18]

for i in range(len(np_cost)):
    if np_cost[i]<=budget:
        temp+=news_paper[i]
        #temp+=','
        budget-=np_cost[i]
    for j in range(i+1,len(np_cost)):
        if np_cost[j]<=budget:
            
            temp+=','
            temp+=news_paper[j]
            budget-=np_cost[j]
    temp+='}'
    result.append(temp)
    temp='{'
    budget=bud    
print(result)