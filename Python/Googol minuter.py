googol = 10**100

timmar = googol/60

timmar_under_dag = timmar % 24

tid_nu = round(float(input("Vad är klockan nu: ")), 1)

tiden = timmar_under_dag+tid_nu

if tiden > 24:
    tiden-=24

print(f"Klockan är: {tiden}")