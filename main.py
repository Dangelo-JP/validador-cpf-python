import sys

#GERANDO O PRIMEIRO DIGITO DO CPF '74682489070'

print("\n-----------BEM-VINDO AO VERIFICADOR DE CPF---------------\n")
entrada = input("Digite o CPF a ser verificado: ").replace(".","").replace("-","")

teste_sequencial = entrada == entrada[0]*len(entrada) #Verificação inicial

if teste_sequencial:
    print("ERRO: Você inseriu números sequenciais!")
    sys.exit()

nove_digitos = entrada [:9] #Pegamos os 9 primeiros digitos do CPF
contador_regressivo_1 = 10 

resultado_dig_01 = 0 
for digito in nove_digitos:
    resultado_dig_01 += (int(digito) * contador_regressivo_1) #Fazemos uma multiplicação de cada digito por cada número de uma contagem regressiva começando do 10 e somamos cada resultado
    contador_regressivo_1 -= 1

digito_01 = (resultado_dig_01 * 10) % 11 #Agora, pegamos a soma resultante e multiplicamos por 10 e vemos o resto da divisão desse valor por 11 para obter o dígito.

digito_01 = digito_01 if digito_01 <= 9 else 0 #Caso o digito obtido seja menor do que 9, o valor será o mesmo obtido; caso maior, ele será igual a 0.

# GERANDO O SEGUNDO DIGITO DO CPF

dez_digitos = entrada[:9] + str(digito_01)
contador_regressivo_2 = 11

resultado_dig_02 = 0
for digito in dez_digitos:
    resultado_dig_02 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1

digito_02 = (resultado_dig_02 * 10) % 11

digito_02 = digito_02 if digito_02 <= 9 else 0

# RESULTADO FINAL

resultado_final = f'{nove_digitos}{digito_01}{digito_02}'

if entrada == resultado_final:
    print("O CPF inserido é válido!")
else:
    print("CPF inválido!")