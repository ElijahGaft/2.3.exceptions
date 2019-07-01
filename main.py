# Нужно реализовать Польскую нотацию для двух положительных чисел.

# Эта функция отслеживает верный ввод выражения
def correct_input():

    try:
        expression = input('Введите вырожение для двух положительных чисел в формате в префиксном виде: ')
        expression = expression.strip()
        assert expression[0] in ('+','-','*','/')
        sign = expression[0]
        expression = expression.replace(expression[0], ' ')
    except:
        print('Первый смысловой символ обязательно должен быть оператор!')
        return correct_input()
    try:
        expression = expression.strip()
        gaps =0
        for symbol in expression:
            if symbol == ' ':
                gaps += 1
            else:
                try:
                    assert symbol in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                except:
                    print('Кажется здесь есть лишние символы...')
                    return correct_input()
        if gaps != 1:
            raise ValueError
        else:
            num = expression.split()
            first_num = num[0]
            second_num = num[1]
            return sign, first_num, second_num
    except ValueError:
        print('Значений по условию должно быть два (разделённые знаком пробела)')
        return correct_input()

# Это функция производит все необходимые расчёты
def do_expression(sign, first_num, second_num):
    if (sign == '/'):
        if second_num == 0:
            return 'Делить на ноль нельзя'
        result = int(first_num) / int(second_num)
    elif (sign == '+'):
        result = int(first_num) + int(second_num)
    elif (sign == '-'):
        result = int(first_num) - int(second_num)
    elif (sign == '*'):
        result = int(first_num) * int(second_num)
    return result

# Это основная функция выполнения программы
def main():
    expression = correct_input()
    print(do_expression(expression[0], expression[1], expression[2]))

main()