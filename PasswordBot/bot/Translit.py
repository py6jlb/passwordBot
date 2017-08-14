class Translit():
    ru_to_eng = {  'А': 'A', 'а': 'a',
                    'Б': 'B', 'б': 'b',
                    'В': 'V', 'в': 'v',
                    'Г': 'G', 'г': 'g',
                    'Д': 'D', 'д': 'd',
                    'Е': 'E', 'е': 'e',
                    'Ё': 'JO', 'ё': 'jo',
                    'Ж': 'GH', 'ж': 'gh',
                    'З': 'Z', 'з': 'z',
                    'И': 'I', 'и': 'i',
                    'Й': 'J', 'й': 'j',
                    'К': 'K', 'к': 'k',
                    'Л': 'L', 'л': 'l',
                    'М': 'M', 'м': 'm',
                    'Н': 'N', 'н': 'n',
                    'О': 'O', 'о': 'o',
                    'П': 'P', 'п': 'p',
                    'Р': 'R', 'р': 'r',
                    'С': 'S', 'с': 's',
                    'Т': 'T', 'т': 't',
                    'У': 'U', 'у': 'u',
                    'Ф': 'F', 'ф': 'f',
                    'Х': 'H', 'х': 'h',
                    'Ц': 'C', 'ц': 'c',
                    'Ч': 'CH', 'ч': 'ch',
                    'Ш': 'SH', 'ш': 'sh',
                    'Щ': 'SHh', 'щ': 'shh',
                    'Ъ': '', 'ъ': '',
                    'Ы': 'Y', 'ы': 'y',
                    'Ь': '\'', 'ь': '\'',
                    'Э': 'JE', 'э': 'je',
                    'Ю': 'YU', 'ю': 'yu',
                    'Я': 'YA', 'я': 'ya'
                    }
    ru_to_bot_eng = {  'А': 'A', 'а': 'a',
                        'Б': '6', 'б': '6',
                        'В': 'B', 'в': 'B',
                        'Г': 'r', 'г': 'r',
                        'Д': 'g', 'д': 'g',
                        'Е': 'E', 'е': 'e',
                        'Ё': 'E', 'ё': 'e',
                        'Ж': '}|{', 'ж': '}|{',
                        'З': '3', 'з': '3',
                        'И': 'u', 'и': 'u',
                        'Й': 'u', 'й': 'u',
                        'К': 'K', 'к': 'k',
                        'Л': 'Jl', 'л': 'Jl',
                        'М': 'M', 'м': 'M',
                        'Н': 'H', 'н': 'H',
                        'О': 'O', 'о': 'o',
                        'П': 'n', 'п': 'n',
                        'Р': 'P', 'р': 'p',
                        'С': 'C', 'с': 'c',
                        'Т': 'T', 'т': 't',
                        'У': 'Y', 'у': 'y',
                        'Ф': 'qp', 'ф': 'qp',
                        'Х': 'X', 'х': 'x',
                        'Ц': 'U,', 'ц': 'u,',
                        'Ч': '4', 'ч': '4',
                        'Ш': 'LLl', 'ш': 'w',
                        'Щ': 'LLl,', 'щ': 'w,',
                        'Ъ': '`b', 'ъ': '`b',
                        'Ы': 'bl', 'ы': 'bl',
                        'Ь': 'b', 'ь': 'b',
                        'Э': '-)', 'э': '-)',
                        'Ю': 'l-O', 'ю': 'l-O',
                        'Я': '9l', 'я': '9l'
                        }

    def transliterate(self, mystring):
        translit_word = []
        for char in str(word):
            if self.ru_to_eng.get(char, 'null') != 'null':
                translit_word.append(map_dict[char])
            else:
                translit_word.append(str(char))
        return ''.join(translit_word)
