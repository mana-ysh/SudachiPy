from enum import IntEnum


class CategoryType(IntEnum):
    DEFAULT = 1
    SPACE = 1 << 1
    KANJI = 1 << 2
    SYMBOL = 1 << 3
    NUMERIC = 1 << 4
    ALPHA = 1 << 5
    HIRAGANA = 1 << 6
    KATAKANA = 1 << 7
    KANJINUMERIC = 1 << 8
    GREEK = 1 << 9
    CYRILLIC = 1 << 10
    USER1 = 1 << 11
    USER2 = 1 << 12
    USER3 = 1 << 13
    USER4 = 1 << 14

    def category_type(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_type(self, id):
        for type_ in CategoryType.values():
            if type_.get_id() is id:
                return type_
        return None