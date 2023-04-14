PopulaçãoA = 80000
TaxaPais_A = 0.03

PopulaçãoB = 200000
TaxaPais_B = 0.015

anos = 0

while PopulaçãoA < PopulaçãoB:
    anos += 1
    PopulaçãoA *= 1 + TaxaPais_A
    PopulaçãoB *= 1 + TaxaPais_B

print(f"Serão necessários {anos} anos para a população do país A ultrapassar ou igualar a população do país B")