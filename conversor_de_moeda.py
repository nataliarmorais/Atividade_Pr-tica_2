#Dados
reais = 100.00
taxa_dolar = 5.20
taxa_euro= 6.15

dolares = reais / taxa_dolar
euros = reais / taxa_euro

#Extraindo os resultados

print(f"Valor em reais :R${reais:.2f} ")
print(f"Convertido para dolares: ${dolares:.2f} ")
print(f"Convertido para euros: €{euros:.2f} ")

