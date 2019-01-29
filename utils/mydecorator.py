from datetime import datetime


def log_writer_with_path(path):
    def log_writer(some_function):
        def wrapper(*args, **kwargs):
            result = some_function(*args, **kwargs)
            with open(path + 'log_file.txt', 'a', encoding='utf-8') as f:
                f.write('{} {} {} {} {}\n'.format(datetime.now(), some_function.__name__, args, kwargs, result))
            print(datetime.now(), some_function.__name__, args, kwargs, result)
            return result
        return wrapper
    return log_writer


if __name__ == '__main__':
    @log_writer_with_path('C:\\Users\\semen\\Documents\\GitHub\\decorators\\')
    def my_foo(*args, multi=5):
        return args * multi

    my_foo('sds', 'ssg', 'sgf', multi=2)

