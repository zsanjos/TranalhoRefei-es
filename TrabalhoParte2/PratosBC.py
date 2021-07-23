def servico_bordo (qtPaxBC, prato1, prato2):
    return qtPaxBC * prato1, prato2

qtPaxBC = int(input("Informe a quantidade de passageiros BC: "))
prato1 = qtPaxBC * 0.6
prato2 = qtPaxBC * 0.4

print ("Quantidade de pratos op1: {:.2f}".format (round(prato1)))
print ("Quantidade de pratos op1: {:.2f}".format (round(prato2)))

