from random import randint

from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон равный {value_attack}'

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона'

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}')

    def full_desc(self):
        return f'{self.name}, ты - {self.BRIEF_DESC_CHAR_CLASS}'

    def __str__(self):
        return (
            f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'
        )


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = ('дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

    def full_desc(self):
        return (f'{self.name}, ты '
                'Воитель - великий мастер ближнего боя.')


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = ('находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

    def full_desc(self):
        return (f'{self.name}, ты '
                'Маг — превосходный укротитель стихий.')


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = ('могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'

    def full_desc(self):
        return (f'{self.name}, ты '
                'Лекарь — чародей, способный исцелять раны.')


def choice_char_class(char_name: str) -> Character:
    """Return a Character object according to selected character class."""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = ''

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: '
                               'Воитель — warrior, Маг — mage, '
                               'Лекарь — healer: ')

        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character: Character) -> str:
    print(character.full_desc())
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd_list = ('attack', 'defence', 'special')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in cmd_list:
            print(getattr(character, cmd)())
    return 'Тренировка окончена.'


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
          f'Сейчас твоя выносливость — {DEFAULT_STAMINA}, '
          f'атака — {DEFAULT_ATTACK} и защита — {DEFAULT_DEFENCE}.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    character = choice_char_class(char_name)
    print(start_training(character))
