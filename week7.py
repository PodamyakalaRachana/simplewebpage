from collections import defaultdict
jug1=int(input("enter the capacity of jug1"))
jug2=int(input("enter the capacity of jug2"))
target=int(input("enter the capacity to be measured within the range of Max(jug1,jug2)"))
visited=defaultdict(lambda:False)
print(visited)
def waterjugproblem(amount1,amount2):
    if(amount1==target and amount2==0)or (amount==target and amount1==0):
        print(amount1,amount2)
        return True
    if visited[(amount1,amount2)]==False:
        print(amount1,amount2)
        visited[(amount1,amount2)]=True
        return(waterjugroblem(0,amount2) or
               waterjugproblem(amount1,0)or
               waterjugproblem(jug1,amount2) or
               waterjugproblem(amount1,jug2) or
               waterjugproblem(amount1+min(amount2,(jug1-amount1)),
                    amount2-min(amount2,(jug1-amount1))) or
               waterjugproblem(amount1 - min(amount1,(jug2-amount)),
                               amount2+min(amount1,(jug2-amount2))))
    else:
        return False
    print("steps: ")
    waterjugproblem(0,0)
