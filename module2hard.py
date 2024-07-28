def generate_password(n):
    result = ""
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n):
            if (number % (i + j) == 0) and ((i + j) <= number) and (i != j):
                result += str(i) + str(j)
    return result

number = 0
while number < 3 or number > 20:
    number = int(input("Введите число от 3 до 20: "))

password = generate_password(number)
print(f"Пароль: {password}")
