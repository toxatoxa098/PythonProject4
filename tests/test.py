def info_expenses():

    with open("../tests/expenses.txt", "r") as file:
        line = file.read().split()
        sum_ = 0
        max_ = 0
        min_ = 10**10
        for element in line:
            if int(element) < min_:
                min_ = int(element)
                if int(element) > max_:
                    max_ = int(element)
            sum_ += int(element)

    with open("info.txt", "w", encoding="utf=8") as file:
        file.write(f"'сумма': {sum_}\n")
        file.write(f"'минимум': {min_}\n")
        file.write(f"'максимум': {max_}\n")

    return "Информация успешно записана в файл info.txt"


print(info_expenses())
