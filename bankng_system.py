# Sistema Bancário Simples em Python - Versão 2
# Desafio do bootcamp Potência Tech powered by iFood | Ciência de Dados
# Desenvolvido para o módulo "Dominando Python para Ciência de Dados"

def menu():
    
    """
    Exibe o menu de opções e captura a escolha do usuário.
    
    Returns:
        str: Opção escolhida pelo usuário.
    """
    menu_text = """
        [c] - Criar nova conta
        [e] - Selecionar conta
        [q] - Sair
        =>
    """
    return input(menu_text).lower()

def account_menu():
    
    """
    Exibe o menu de opções da conta e captura a escolha do usuário.

    Returns:
        str: Opção escolhida pelo usuário.
    """
    account_menu_text = """
        [d] - Depositar
        [s] - Sacar
        [e] - Extrato
        [q] - Voltar
        =>
    """
    
    return input(account_menu_text).lower()

def create_account(accounts):
    
    """
    Cria uma nova conta vinculada a um CPF e a adiciona ao dicionário de contas.

    Args:
        accounts (dict): Dicionário de contas.

    Returns:
        str: CPF da nova conta.
    """
    cpf = input("Digite o CPF do usuário (somente números): ")
    
    if cpf in accounts:
        print("Já existe uma conta vinculada a esse CPF.")
        return cpf

    account_number = str(len(accounts) + 1)
    accounts[cpf] = {'account_number': account_number, 'balance': 0.0, 'transactions': []}
    print(f"Conta {account_number} criada com sucesso para o CPF {cpf}.")
    return cpf

def select_account(accounts):
    """
    Permite ao usuário selecionar uma conta para realizar operações.

    Args:
        accounts (dict): Dicionário de contas.

    Returns:
        str: CPF da conta selecionada.
    """
    if not accounts:
        print("Nenhuma conta disponível. Crie uma nova conta primeiro.")
        return None

    print("Contas disponíveis:")
    for cpf, details in accounts.items():
        print(f"Conta: {details['account_number']} - CPF: {cpf}")

    selected_cpf = input("Selecione o CPF da conta: ")
    if selected_cpf in accounts:
        return selected_cpf
    else:
        print("Conta inválida.")
        return None

def deposit(balance, transactions):
    
    """
    Realiza a operação de depósito na conta.

    Args:
        balance (float): O saldo atual da conta.
        transactions (list): Histórico de transações.

    Returns:
        float: O novo saldo atualizado.
        list: Histórico de transações atualizado.
    """
    amount = float(input('Valor para depósito: '))
    if amount > 0:
        balance += amount
        transactions.append(f"Depósito: R$ {amount:.2f}")
        print(f"Depósito de R$ {amount:.2f} realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")
        
    return balance, transactions

def withdraw(balance, transactions, daily_withdraw_count):
    
    """
    Realiza a operação de saque.

    Args:
        balance (float): O saldo atual da conta.
        transactions (list): Histórico de transações.
        daily_withdraw_count (int): Contador de saques realizados no dia.

    Returns:
        float: O novo saldo atualizado.
        list: Histórico de transações atualizado.
        int: Contador de saques atualizado.
    """
    LIMIT_WITHDRAW = 3
    LIMIT_WITHDRAW_VALUE = 500
    
    if daily_withdraw_count >= LIMIT_WITHDRAW:
        print("Limite diário de 3 saques atingido.")
        return balance, transactions, daily_withdraw_count

    amount = float(input("Valor para saque: "))
    if amount > 0 and amount <= LIMIT_WITHDRAW_VALUE:
        if amount <= balance:
            balance -= amount
            transactions.append(f"Saque: R$ {amount:.2f}")
            daily_withdraw_count += 1
            print(f"Saque de R$ {amount:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque.")
    else:
        print("Valor inválido para saque. O limite por saque é R$ 500,00.")
    
    return balance, transactions, daily_withdraw_count

def statement(balance, transactions):
    """
    Exibe o extrato de todas as transações realizadas e o saldo atual da conta.

    Args:
        balance (float): O saldo atual da conta.
        transactions (list): Histórico de transações.

    Returns:
        None
    """
    print("\n====== Extrato =======\n")
    if not transactions:
        print("Nenhuma transação realizada.")
    else:
        for transaction in transactions:
            print(transaction)
    
    print(f"Saldo atual: R$ {balance:.2f}")
    print("\n=======================\n")

def main():
    
    """
    Função principal que controla o fluxo do programa e gerencia as operações de contas.

    Returns:
        None
    """
    
    accounts = {}  # Dicionário para armazenar contas
    current_cpf = None
    
    while True:
        
        if current_cpf is None:
            option = menu()
            if option == 'c':
                current_cpf = create_account(accounts)
            elif option == 'e':
                current_cpf = select_account(accounts)
            elif option == 'q':
                break
            else:
                print("Opção inválida!")
        else:
            balance = accounts[current_cpf]['balance']
            transactions = accounts[current_cpf]['transactions']
            daily_withdraw_count = 0 

            option = account_menu()
            if option == 'd':
                balance, transactions = deposit(balance, transactions)
            elif option == 's':
                balance, transactions, daily_withdraw_count = withdraw(balance, transactions, daily_withdraw_count)
            elif option == 'e':
                statement(balance, transactions)
            elif option == 'q':
                accounts[current_cpf]['balance'] = balance  
                accounts[current_cpf]['transactions'] = transactions  
                current_cpf = None  
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
