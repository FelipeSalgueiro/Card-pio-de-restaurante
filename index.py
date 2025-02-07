pedidos = []
lanches = ['x-ratão', 'yakisopa', 'joelho']
count = 0

print("Bem Vindo ao Vai no Lanche\n")
num_pedidos_cliente = input("Quantos lanches deseja pedir? ")

print("\nNosso cardápio:\n")
while count < len(lanches):
    print(f"{int(count) + 1} - {lanches[count]}")
    count += 1

while len(pedidos) < int(num_pedidos_cliente):
    pedido = input(f"Digite o seu pedido: ")
    quantidade = 0
    if(pedido != lanches[0] and pedido != lanches[1] and pedido != lanches[2]):
        print("Lanche não está no cardápio!")
    else:
        quantidade = int(input(f"Quantos desse pedido você deseja? "))
    aux = 0
    while aux < quantidade:
        pedidos.append(pedido)
        aux += 1
        if len(pedidos) > int(num_pedidos_cliente):
            print(f"O número de pedidos ultrapassou o valor declarado anteriormente, limpando seu carrinho...\n")
            pedidos.clear()
            break
print(f"Lista com seus pedidos: ")
for item in pedidos: 
    print(item)
print(f"Estará chegando em até 1 hora. =3")