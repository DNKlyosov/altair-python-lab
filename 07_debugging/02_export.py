import csv
from pathlib import Path
from time import perf_counter
from itertools import product
output=Path(__file__).resolve().parent.parent/'results'/'timing.csv'
output.parent.mkdir(exist_ok=True)
with output.open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f); writer.writerow(['bits','variants','seconds'])
    for n in [4,8,12,16]:
        start=perf_counter(); count=sum(1 for _ in product([0,1],repeat=n))
        elapsed=perf_counter()-start
        writer.writerow([n,count,elapsed]); print(n,count,elapsed)
print(output)
