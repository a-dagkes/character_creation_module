from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Return a message with a number of damage points inflicted."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')
    return (f'{char_name} нанёс урон противнику равный 5')


def defence(char_name: str, char_class: str) -> str:
    """Return a message with a number of damage points blocked."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал '
                f'{10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал '
                f'{10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал '
                f'{10 + randint(2, 5)} ед. урона')
    return (f'{char_name} блокировал 10 ед. урона')


def special(char_name: str, char_class: str) -> str:
    """Return a message w/ a number of special skill points after using it."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение '
                f'«Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение '
                f'«Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Return messages with comments during training mode.
    Train to use "attack", "defence" and "special" commands.
    Results of using them depends on character's class.
    """
    if char_class == 'warrior':
        print(f'{char_name}, '
              'ты Воитель — отличный боец ближнего боя.')
    elif char_class == 'mage':
        print(f'{char_name}, '
              'ты Маг — превосходный укротитель стихий.')
    elif char_class == 'healer':
        print(f'{char_name}, '
              'ты Лекарь — чародей, способный исцелять раны.')
    else:
        return 'Класс персонажа не распознан'
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
        else:
            print('Команда не распознана')
            continue
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Return selected character class: warrior, mage, or healer."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        elif char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        elif char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        else:
            print('Класс персонажа не распознан')
            continue
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    """Start game banner.
    Greetings.
    Choosing character name and class.
    Performing the training.
    """
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
