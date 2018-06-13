#def michael_pays(costs):
costs = float(input())
michael_part = 0.0
kate_part = 0.0
if costs <= 5:
    michael_part = costs
elif costs > 5 and costs <= 10:
    kate_part = costs * 0.3
    michael_part = costs - kate_part
else:
    kate_part = 10
    michael_part = costs - kate_part
#return michael_part
print(michael_part)