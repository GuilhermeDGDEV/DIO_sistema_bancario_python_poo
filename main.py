from os import system
import functions.banco as b


def main():
    clientes = []
    contas = []

    while True:
        opcao = b.menu()

        if opcao == 'd':
            b.depositar(clientes)

        elif opcao == 's':
            b.sacar(clientes)

        elif opcao == 'e':
            b.exibir_extrato(clientes)

        elif opcao == 'nu':
            b.criar_cliente(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            b.criar_conta(numero_conta, clientes, contas)

        elif opcao == 'lc':
            b.listar_contas(contas)

        elif opcao == 'l':
            system('cls')

        elif opcao == 'q':
            break

        else:
            print(f'\n{ " Operação inválida, por favor selecione novamente a operação desejada. ".center(100, "@") }')


if __name__ == '__main__':
    main()
