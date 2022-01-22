def arithmetic_arranger(problems=None, val=True):
    if problems is None:
        problems = ['3 + 855', '988 + 40']

    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    # keep in mind for later :3
    # list comprehension (sets and generators(look more) and dic)
    operators = {
        '+': True,
        '-': True,
    }
    for x in problems:
        if x.split()[1] not in operators:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

    numbers = []
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda k: k.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda k: len(k) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    top_row = ''
    dashes = ''
    values = list(map(lambda k: eval(k), problems))  # never use eval() unsafe code
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += list(map(lambda k: k.split()[1], problems))[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems


