import chardet

def find_top_ten_words(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        s = s.replace('\n', '')
        counting_dict = {}

        for word in s.split(' '):
            word = word.lower()
            if len(word) > 6:
                if counting_dict.get(word):
                    increased_counter = counting_dict[word] + 1
                    counting_dict[word] = increased_counter
                else:
                    counting_dict[word] = 1

        print('Статистика по файлу {0}:'.format(filename))
        sorted_count_pairs = sorted(counting_dict.items(), key=lambda x: x[1], reverse=True)
        top_10 = sorted_count_pairs[:10]

        for element in top_10:
            print('- слово "{0}" встречается {1} раз'.format(element[0], element[1]))

def main():
    find_top_ten_words('newsafr.txt')
    find_top_ten_words('newscy.txt')
    find_top_ten_words('newsfr.txt')
    find_top_ten_words('newsit.txt')

main()