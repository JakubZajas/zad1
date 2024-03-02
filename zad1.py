class zad1:
    def __init__(self,name,netto,vat) :
        self.name=name
        self.netto=netto
        self.vat=vat


values=[
    zad1("Clean Code, Robert C. Martin",100,0.08),
    zad1("Applying UML and Patterns, C. Larman",300,0.08),
    zad1("Shipping",50,0.23)
]
suma_netto=[0,0]
for v in values:
    if v.vat==0.08:
        suma_netto[0]+=v.netto
    elif v.vat==0.23:
        suma_netto[1]+=v.netto

suma_vat=[0,0]
for v in values:
    if v.vat==0.08:
        suma_vat[0]+=v.netto*v.vat
    elif v.vat==0.23:
        suma_vat[1]+=v.netto*v.vat

    # suma_vat.append(v.vat*v.netto)

print("|               | Total netto |     X     |")
print("|---------------|-------------|-----------|")
print("| VAT 8%        |   {:.2f} zł |   {:.2f} zł |".format(suma_netto[0], suma_vat[0]))
print("| VAT 23%       |   {:.2f} zł |   {:.2f} zł |".format(suma_netto[1], suma_vat[1]))
