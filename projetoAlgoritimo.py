placa = str(input("Placa do veículo: "))
nome = str(input("Nome do motorista: "))
vm = int(input("Velocidade registrada: "))
vmp = int(input("Velocidade máxima permitida: "))
multa = input("O motorista ja foi multado antes? (Sim/Não): ").lower()
pm = input("Deseja pagar a multa agora? (Sim/Não): ").lower()

if(vm <= vmp): #2 e 3. Classificação da Infração e calculo de multa com base na velocidade registrada
    descricao = "Não foi aplicada multas"
else:
    if(vm <= vmp * 1.2):  
        valor_multa = 130.16
        descricao = "Infração leve: multa de R$ 130,16 e nenhum ponto na CNH."
    elif(vm <= vmp * 1.5):  
        valor_multa = 195.23
        descricao = "Infração grave: multa de R$ 195,23 e adição de 5 pontos na CNH."
    else:  
        valor_multa = 880.41
        descricao = "Infração gravíssima: multa de R$ 880,41, adição de 7 pontos na CNH e suspensão imediata do direito de dirigir."

def dobra(valor_multa): #4. Verifica reincidência
    global a
    a = valor_multa * 2
    return a   

print(f"Nome: {nome} \nPlaca: {placa} \nVelocidade: {vm} km/h \nVelocidade da via: {vmp} km/h \n{descricao}") #imprime o cabeçalho 
print("-"*40)

if multa in("sim",'s'): #verificar se houve multas anteriores, se sim dobrar a multa 
    print(f"Atenção: Multa DOBRADA por reincidência! \nO valor da multa sera de: R$ {dobra(valor_multa)}")
if(valor_multa == 880.41): #verificar se houve infração gravissima e se sim suspender a cnh e fazer reciclagem
    print("Atenção: Você precisa fazer um curso de reciclagem no Detran. \n Atenção: CNH suspensa! Compareça ao Detran.")

if pm in("sim",'s'): #verificar se o usuario quer pagar agr e aplicar o desconto
    print("Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$ ", a - (valor_multa*0.2))