import random

import data_foodMenu as menu


def getRandomFood(foodType):
    # 아무 메뉴나 상관 없는 경우
    if foodType == None:
        size1 = len(menu.koreanFood)
        size2 = len(menu.japaneseFood)
        size3 = len(menu.chineseFood)
        size4 = len(menu.weasternFood)
        randomNum = random.randint(0, size1+size2+size3+size4-1)

        if 0 <= randomNum < size1:
            return menu.koreanFood[randomNum]
        elif size1 <= randomNum < size1+size2:
            return menu.japaneseFood[randomNum-size1]
        elif size1+size2 <= randomNum < size1+size2+size3:
            return menu.chineseFood[randomNum-size1-size2]
        else:
            return menu.weasternFood[randomNum-size1-size2-size3]
    # 한식에서 고르는 경우
    elif foodType == "한식":
        return menu.koreanFood[random.randint(0, len(menu.koreanFood)-1)]
    # 일식에서 고르는 경우
    elif foodType == "일식":
        return menu.japaneseFood[random.randint(0, len(menu.japaneseFood)-1)]
    # 중식에서 고르는 경우
    elif foodType == "중식":
        return menu.chineseFood[random.randint(0, len(menu.chineseFood)-1)]
    # 양식에서 고르는 경우
    elif foodType == "양식":
        return menu.weasternFood[random.randint(0, len(menu.weasternFood)-1)]
    elif foodType == "다":
        return menu.koreanFood[random.randint(0, len(menu.koreanFood)-1)] + ", " + \
            menu.japaneseFood[random.randint(0, len(menu.japaneseFood)-1)] + ", " + \
            menu.chineseFood[random.randint(0, len(menu.chineseFood)-1)] + ", " + \
            menu.weasternFood[random.randint(0, len(menu.weasternFood)-1)]
    else:
        return "Error"
