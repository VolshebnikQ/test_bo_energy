from functools import reduce

#   находим числа
def get_num(arr_argument):
        num = []
        str_nums = reduce(lambda x, y: x+y, arr_argument)
        for a in str_nums.split("*"):
            if len(a) > 0 and a != "-":
                try:
                    n = int(a)
                except ValueError:
                    n = float(a)
                num.append(n)
            if a == "-":
                n = -1
                num.append(n)
        return reduce(lambda x, y: x*y, num)

#   находим аргументы уравнения
def get_arguments(equation):
    arguments = [0, 0, 0]
    for e in equation.replace("-", "+-").replace(",", ".").split("+"):
        if len(e) > 0:
            if e.find("x^2") != -1:
                arguments[0] += get_num(e.replace("x^2","*1"))
            elif e.find("x") != -1:
                arguments[1] += get_num(e.replace("x","*1"))
            else:
                arguments[2] += get_num(e)

    return arguments

#   решаем уравнение
def solve_equation(equation):
    a, b, c = 0, 0 ,0
    x = []

    if equation.find('x') == -1:
        return "Неизвестная переменная не найдена"

    equation_list = equation.replace(" ", "").split("=")
    if len(equation_list) == 2:
        a, b, c = get_arguments(equation_list[0])
        if equation_list[1] != "0":
            a, b, c = list(map(lambda x, y: x+y, [a, b, c], get_arguments(equation_list[1])))
    elif len(equation.split("=")) == 1:
        a, b, c = get_arguments(equation.replace(" ", ""))
    else:
        return "Некорректное уравнение"

    if a == 0:
        x.append(round(c/(-b), 3))
        return f"Уравнение не квадратное, но имеет один корень и он равен <br>x = {x[0]}"
    
    discriminant = b**2 - 4*a*c 

    if discriminant < 0:
        return f"Уравнение не имеет решения так как дискриминант = {discriminant}"
    if discriminant == 0:
        x.append(round(-b/(2*a), 3))
        return f"Уравнение имеет один корень и он равен <br>x = {x[0]}"
    if discriminant > 0:
        x.append(round(-b + (discriminant)**(1/2)/(2*a), 3))
        x.append(round(-b - (discriminant)**(1/2)/(2*a), 3))
        return f"Уравнение имеет два корня<br>x1 = {x[0]}<br>x2 = {x[1]}"

    return "Некорректное уравнение"
