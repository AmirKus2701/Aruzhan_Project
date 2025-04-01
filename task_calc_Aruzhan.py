from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

def calculate_tax(income, tax_rate):
    tax = income * tax_rate / 100
    income_after_tax = income - tax
    return tax, income_after_tax

def main():
    print(Fore.CYAN + "Выберите тип налогоплательщика:")
    print(Fore.GREEN + "1. Физлицо (10%)")
    print(Fore.GREEN + "2. Частная практика (9%)")
    print(Fore.GREEN + "3. ИП (5%)")
    print(Fore.GREEN + "4. КФХ (3%)")
    print()
    choice = input(Fore.YELLOW + "Введите номер типа налогоплательщика (1-4): ")
    
    if choice not in ['1', '2', '3', '4']:
        print(Fore.RED + "Неверный выбор. Пожалуйста, попробуйте снова.")
        return
    
    income = float(input(Fore.YELLOW + "Введите доход: "))
    
    tax_rates = {
        '1': 10,
        '2': 9,
        '3': 5,
        '4': 3
    }
    
    tax_rate = tax_rates[choice]
    tax, income_after_tax = calculate_tax(income, tax_rate)
    
    print(Fore.BLUE + f"Налог к уплате: {tax:.2f}")
    print(Fore.BLUE + f"Доход после уплаты налогов: {income_after_tax:.2f}")
    print()

if __name__ == "__main__":
    while True:
        main()