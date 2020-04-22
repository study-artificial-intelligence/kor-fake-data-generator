import random
import re


def chg_word(content, dict, alt=None):
    """
    change contents using wrong words

    Args:
        :param: content(list)
        :param: dict(dictionary): wrong word dictionary
        :param: alt(dictionary): integrated word dictionary.
                                 (default: None)
    Returns:
        contents which is changed wrong words
    """
    for i in range(len(content)):
        random.seed()
        if alt is not None:
            for key, value in alt.items():
                content[i] = re.sub(key, value, content[i])
        for key, value in dict.items():
            check = [m.start() for m in re.finditer(key, content[i])]

            if len(check) is not 0:
                randChg = value[random.randint(0, len(value)-1)]
                content[i] = content[i].replace(key, randChg)

    return content


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    verb = {
        "니다": [
            "니다",
            "습다", "슴다", "슷니다", "숩다", "스비다",
            "숩니다", "슷니다", "습닛다",
            "니당", "닌다", "니단", "니담", "님당"
        ],
    }

    alternative = {
        "습니다": "니다",
    }

    print("Origin: ", test)
    result = chg_word(test, verb)
    print("Result: ", result)
