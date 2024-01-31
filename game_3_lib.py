from random import choice

WORDS = [
    # easy
    ['парк', 'кукла', 'звук', 'паркет', 'космос', 'молоко', 'окно', 'мечта', 'кресло', 'печь', 'корова', 'кофе',
     'щенок', 'вода', 'дом', 'трюк', 'колесо', 'дракон', 'тень', 'компас', 'гоблин', 'футбол', 'синий', 'овощи',
     'зонтик', 'фото', 'салат', 'луна', 'солнце', 'король', 'цветы', 'спорт', 'радуга', 'замок', 'торт', 'мост',
     'шапка', 'пальто', 'зима', 'юбка', 'глобус', 'осень', 'белый', 'ракета', 'дождь', 'камень', 'малина', 'вата',
     'шторы', 'вино', 'робот', 'книжка', 'озеро', 'гриль', 'экран', 'долина', 'часы', 'танец', 'рыжик', 'собака',
     'река', 'снег', 'рюкзак', 'опера', 'карта', 'камин', 'конь', 'фонтан', 'дерево', 'фитнес', 'песок', 'весна',
     'море', 'лето', 'пижама', 'поток', 'чайник', 'чашка', 'голубь', 'звезда', 'чудо', 'компот', 'краска', 'билет',
     'вишня', 'свет', 'фрукты', 'платье', 'свитер', 'лес', 'черный', 'комета', 'кружка', 'танцор', 'кот', 'гитара',
     'диван', 'гусь', 'плита', 'птица', 'ключ', 'яблоко', 'цветок', 'музыка', 'зебра', 'стол', 'лимон', 'ящик', 'пицца',
     'топор', 'ритм', 'цвет', 'зонт', 'ноготь', 'печка', 'магия', 'школа', 'батон', 'жираф', 'лампа', 'банан', 'пенал',
     'роман', 'тайна', 'город', 'птичка', 'молния', 'радио', 'гора', 'бублик', 'чай', 'эльф', 'фрукт', 'камера',
     'папка', 'желтый', 'слон', 'картон', 'гном', 'машина', 'книга', 'флаг', 'гриб'],
    # normal
    ['шоколадка', 'мандарин', 'барабан', 'зеленый', 'принтер', 'телефон', 'парашют', 'фиолетовый', 'планета',
     'перчатки', 'виолончель', 'футболка', 'котенок', 'бабочка', 'косметика', 'попугай', 'клавиатура', 'картина',
     'велосипед', 'лампочка', 'картошка', 'ватрушка', 'карандаш', 'крокодил', 'шоколад', 'принцесса', 'красота',
     'пирамида', 'крыльцо', 'голубой', 'творчество', 'корабль', 'оранжевый', 'пианино', 'мороженое', 'лужайка',
     'яблочко', 'пастель', 'розовый', 'рисунок', 'ноутбук', 'чемодан', 'пельмени', 'балерина', 'красный', 'медведь',
     'бутерброд', 'галактика', 'контингент', 'счастье', 'бассейн', 'снежинка', 'печенье', 'пингвин', 'гармония',
     'праздник', 'фантазия', 'корзина', 'программа', 'завтрак', 'конфета', 'смайлик', 'подушка', 'троллейбус',
     'бутылка', 'фотосинтез', 'самолет', 'тетрадь', 'водопад', 'детство', 'гиппопотам', 'кабинет', 'пружина', 'мелодия',
     'автомобиль', 'автобус', 'чемпион', 'бабушка', 'загадка', 'волшебство', 'магнитофон', 'зеркало', 'тапочки',
     'ресторан', 'бинокль', 'радость', 'здоровье', 'светофор', 'палитра', 'компьютер', 'вертолет', 'гармоника',
     'звездопад', 'варенье', 'шахматы', 'подкова', 'тропинка', 'космонавт'],
    # hard
    ['мегаломанский', 'макроэкономический', 'гипертрофированный', 'телекоммуникационный', 'дезоксирибонуклеиновый',
     'экспериментатор', 'экспериментаторский', 'трансконтинентальный', 'холодильник', 'электрокомпьютерный',
     'экзопланетарный', 'псевдоинтеллект', 'саморегулирующийся', 'птица-синица', 'галактический', 'эксплуатационный',
     'компромиссный', 'антарктический', 'зубная щетка', 'интеллектуальный', 'коллаборация', 'электродвигатель',
     'аэродинамический', 'программирование', 'космополитический', 'параллелепипед', 'интернационализация',
     'мультимедийный', 'трансцендентальный', 'автоматизированный', 'треугольник', 'фотоаппарат', 'конгрессуальный',
     'рецидивировать', 'трансгрессивный', 'экспериментальный', 'контрпродуктивный', 'экстравагантный',
     'инфраструктурный', 'самоконтроль', 'антропоморфный', 'псевдоинтеллектуальный', 'астрофизика', 'электромагнитный',
     'трансформационный', 'ретроспективный', 'рентгеноструктурный', 'магниторезонанс', 'политико-экономический',
     'путешествие', 'аудиокомпозитор', 'библиографический', 'концентрационный'],
]


def get_word(level=1):
    if level not in range(0, 3):
        level = 1
    return choice(WORDS[level])


if __name__ == "__main__":
    for i in range(0, 3):
        for _ in range(10):
            print(get_word(i), end=", ")
        print()
