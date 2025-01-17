def Table(n):
    v = ""
    for i in range(10):
        v += f"{n} x {i+1} = {n*(i+1)}\n"
    with open(f"tables/tableOf{n}.txt", 'w') as f:
        f.write(v)


for i in range(2, 21):
    Table(i)
