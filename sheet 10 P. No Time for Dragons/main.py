arrange_sold = [list(map(int, input().split())) for i in range(int(input()))]
    
easiest_way = sorted(arrange_sold, key=lambda x: (x[1]-x[0]))
current_lvi =0
tot_sold=0
for x,y in easiest_way:
    if current_lvi <=x:
        tot_sold+=x-current_lvi
        current_lvi=x-y
    else:
        current_lvi -=y
    
print(tot_sold )