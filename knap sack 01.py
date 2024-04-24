def knap_Sack01(w,wt,val,n):
    if n==0 or w==0: # base case
        return 0
    if (wt[n-1]>w):  # if nth item> capacity then it is not included
        return knap_Sack01(w,wt,val,n-1)
    else:
        #return two max cases 
        return max(val[n-1]+knap_Sack01(w-wt[n-1],wt,val,n-1),knap_Sack01(w,wt,val,n-1))
if __name__=="__main__":
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    w=20
    n=len(profit)
    print(knap_Sack01(w,weight,profit,n))