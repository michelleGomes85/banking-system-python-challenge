
# Neste primeira versão o sistema irá trabalhar com somente 1 usuário.
# Todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato

def menu():
    
    """
    Exibe o menu de opções e captura a escolha do usuário.

    Returns:
        str: Opção escolhida pelo usuário.
    """
    
    menu_text = """
        [d] - Depositar
        [s] - Sacar
        [e] - Extrato
        [q] - Sair
        =>
    """
    return input(menu_text).lower()

def deposit(balance, transactions):
    
    """
    Realiza a operação de depósito na conta, permitindo apenas valores positivos.

    Args:
        balance (float): O saldo atual da conta.
        transactions (list): Histórico de transações.

    Returns:
        float: O novo saldo atualizado.
        list: Histórico de transações atualizado.
    """
    
    amount = float(input('Valor para deposito: '))
    if amount > 0:
        balance += amount
        transactions.append(f"Deposito: R$ {amount:.2f}")
        print(f"Deposito de R$ {amount:.2f} realizado com sucesso")
    else:
        print("Valor invalido para deposito")
        
    return balance, transactions

def withdraw(balance, transactions, daily_withdraw_count):
    
    """
    Realiza a operação de saque, respeitando o limite de 3 saques diários e R$ 500,00 por saque.

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
            print(f"Saque de R$ {amount:.2f} realizado com sucesso!!")
        else:
            print("Saldo insuficiente para saque")
    else:
        print("Valor invalido para saque. O limite por saque é R$ 500,00.")
    
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
        print("Nenhuma transação realizada")
    else:
        for transaction in transactions:
            print(transaction)
    
    print(f"Saldo atual: R$ {balance:.2f}")
    print("\n=======================\n")
    
def main():
    
    """
    Função principal que controla o fluxo do programa e gerencia as operações de depósito, saque e extrato.

    Returns:
        None
    """
    balance = 0.0
    transactions = []
    daily_withdraw_count = 0
    
    while True :
        option = menu()
        
        if option == 'd':
            balance, transactions = deposit(balance, transactions)
        
        elif option == 's':
            balance, transactions, daily_withdraw_count = withdraw(balance, transactions, daily_withdraw_count)
        
        elif option == 'e':
            statement(balance, transactions)
            
        elif option == 'q':
            break
        
        else :
            print("Opção invalida!!!")
            
if __name__ == "__main__":
    main()
        
        
    


    