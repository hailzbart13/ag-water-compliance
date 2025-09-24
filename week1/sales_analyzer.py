name=input('Enter file:')
if len(name)<1:
    name='sales.txt'
file=open(name)
kg_per_crop=dict()
rev_per_farm=dict()
for line in file:
    line=line.strip()
    if not line: continue 
    parts=line.split()
    farm=parts[1]
    crop=parts[2]
    qty=float(parts[3])
    price=float(parts[4])
    rev=qty*price
    rev_per_farm[farm]=rev_per_farm.get(farm,0)+rev
    kg_per_crop[crop]=kg_per_crop.get(crop,0)+qty
for crop,total in kg_per_crop.items():
    print(crop,total)
top_farm=None
top_rev=None
for farm, total_rev in rev_per_farm.items():
        if top_rev is None or total_rev>top_rev:
            top_farm=farm
            top_rev=total_rev
print(top_farm,top_rev)
