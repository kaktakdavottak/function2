
def adv_print(text, start='', max_line=6, in_file=False):

    if len(start + text) > max_line:
        result = (start + text)[:max_line] + '\n'
        print_line = start + text
        while len(print_line) >= max_line:
            print_line = print_line[max_line:]
            result += print_line[:max_line] + '\n'
        print(result)
        if in_file:
            with open('file.txt', 'w', encoding='utf-8') as f:
                f.write(result)
    else:
        result = start + text
        print(result)
        if in_file:
            with open('file.txt', 'w', encoding='utf-8') as f:
                f.write(result)


adv_print('123456789', max_line=9, in_file=True)
