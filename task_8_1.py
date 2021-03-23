import re


def parse_email(email):
    RE_EMAIL = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_EMAIL.match(email):
        raise ValueError(f'некорректный адрес')
    else:
        print(RE_EMAIL.match(email).groupdict())


try:
    parse_email('VasiliyPupkin@yandex.ru')
    parse_email('Vasiliy.Pupkin@yandex.ru')
except ValueError as error:
    print(error)
