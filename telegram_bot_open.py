def OPEN_NAMES_TASKS():
    """Выводим названия задач"""
    names_tasks = open(r'names_tasks.txt', encoding='utf-8')
    names_tasks_list = [line for line in names_tasks.readlines()]
    names_tasks.close()
    return names_tasks_list

def OPEN_CATALOG():
    """Выводим задание"""
    catalog = open(r'catalog.txt', encoding='utf-8')
    catalog_zd_list = [line.strip() for line in catalog.readlines()]
    catalog.close()
    return catalog_zd_list

def OPEN_ANSWER():
    """Выводим ответ"""
    answer = open(r'answer.txt', encoding='utf-8')
    answer_zd_list = [line.strip() for line in answer.readlines()]
    answer.close()
    return answer_zd_list

def OPEN_DECISION():
    """Выводим решение"""
    decision = open(r'decision.txt', encoding='utf-8')
    decision_zd_list = [line.strip() for line in decision.readlines()]
    decision.close()
    return decision_zd_list

def OPEN_STIKER():
    """Открыть стикер если пользователь отправил стикер"""
    sticker = open(r'AnimatedSticker_sticker.tgs', "rb")
    return sticker

def OPEN_PHOTO():
    """Открыть стикер если пользователь отправил фото"""
    photo = open(r'AnimatedSticker_foto.tgs', "rb")
    return photo