name = input("Enter file:")
if len(name) < 1:
    name = "grain_prices.csv"
handle = open(name)
counts=dict()
for line in handle:
    if line.startswith('Date'):continue
    line=line.strip()
    sections=line.split(',')
    time=sections[1]
    hour=time.split(':')[0]
    counts[hour]=counts.get(hour,0)+1
for key in sorted(counts):
    print(key,counts[key])
