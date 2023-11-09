import textwrap
from entities.conta_corrente import ContaCorrente
from entities.pessoa_fisica import PessoaFisica
from entities.saque import Saque
from entities.deposito import Deposito


def menu():
    menu = f'''\n
    {' MENU '.center(100, '=')}
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [l]\tLimpar
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))


def listar_contas(contas):
    for conta in contas:
        print('=' * 100)
        print(textwrap.dedent(str(conta)))


def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'\n{ " Cliente não encontrado, fluxo de criação de conta encerrado! ".center(100, "@") }')
        return

    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f'\n{ " Conta criada com sucesso! ".center(100, "=") }')


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(f'\n{ " Cliente não possui conta! ".center(100, "@") }')
        return

    n_conta = int(input('Informe o número da conta do cliente: '))

    for conta in cliente.contas:
        print(conta.numero == n_conta)

    contas_filtradas = [conta for conta in cliente.contas if conta.numero == n_conta]

    return contas_filtradas[0] if contas_filtradas else None


def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'\n{ " Cliente não possui conta! ".center(100, "@") }')
        return

    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'\n{ " Cliente não possui conta! ".center(100, "@") }')
        return

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'\n{ " Cliente não possui conta! ".center(100, "@") }')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print(f'\n {" EXTRATO ".center(100, "=")} ')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Não foram realizadas movimentações.'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao["tipo"]}:\n\tR$ {transacao["valor"]:.2f}'

    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')
    print('=' * 100)


def criar_cliente(clientes):
    cpf = input('Informe o CPF (somente número): ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(f'\n{ " Já existe cliente com esse CPF! ".center(100, "@") }')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)

    clientes.append(cliente)

    print(f'\n{ " Cliente cadastrado com sucesso! ".center(100, "=") }')


def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f'\n{ " Cliente não encontrado, fluxo de criação de conta encerrado! ".center(100, "@") }')
        return

    conta = ContaCorrente.nova_conta(cliente, numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f'\n{ " Conta criada com sucesso! ".center(100, "=") }')
