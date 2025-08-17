def withdraw(current_balance: float, amount: float) -> float:
    """Returns a new balance after withdrawing an amount from the current balance.

    Args:
        current_balance (float): The existing balance in the account.
        amount (float): The amount to withdraw from the account.

    Returns:
        float: Final balance after the withdrawal.
    """

    if current_balance < amount:
        raise ValueError("Insufficient funds for withdrawal.")
    elif amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    else:
        return current_balance - amount
    


def deposit(current_balance: float, amount: float) -> float:
    """Returns a new balance after depositing an amount into the current balance.

    Args:
        current_balance (float): The existing balance in the account.
        amount (float): The amount to deposit into the account.

    Returns:
        float: Final balance after the deposit.
    """

    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    else:
        return current_balance + amount