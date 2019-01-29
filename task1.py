from utils.mycontextmanager import TimeDelta
from utils.mygenerator import my_iter


def adv_print(*args, start='', sep='\n', max_line=6, in_file=False):

    for text in args:
        if len(start + text) > max_line:
            result = (start + text)[:max_line] + '\n'
            print_line = start + text
            while len(print_line) >= max_line:
                print_line = print_line[max_line:]
                result += print_line[:max_line] + '\n'
            print(result + sep)
            if in_file:
                with open('file.txt', 'a', encoding='utf-8') as f:
                    f.write(result)
        else:
            result = start + text + sep
            print(result)
            if in_file:
                with open('file.txt', 'a', encoding='utf-8') as f:
                    f.write(result)
    for item in my_iter('C:\\Users\\semen\\Documents\\GitHub\\function2\\file.txt'):
        print(item)


if __name__ == '__main__':
    with TimeDelta():
        adv_print('1234567891', '123456789', '123456789', sep='\n', start='new', max_line=10, in_file=True)
