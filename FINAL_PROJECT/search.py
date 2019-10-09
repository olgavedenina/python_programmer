import re, sqlite3, pymorphy2
morph = pymorphy2.MorphAnalyzer()


def bd_parse(words):
    words = words.split()
    clean_words = []
    for word in words:
        word = re.sub('[^А-ЯЁёа-я]', '', word.lower())
        normalized = morph.parse(word)[0][2]
        clean_words.append(normalized)
    rel_dic = {}

    global c
    c.execute('SELECT * FROM idiotqueries ORDER BY post_id')
    all_posts = c.fetchall()
    for post in all_posts:
        rel_count = 0
        normalized_text = post[2]
        post_id = post[0]
        for lemma in clean_words:
            if lemma in normalized_text:
                rel_count += 1
        rel_dic.update({rel_count: post_id})
    best_count = sorted(rel_dic)[-1]
    if best_count == 0:
        winner = 'такого еще не спрашивали'
    else:
        winner = rel_dic[best_count]
        c.execute('SELECT * FROM idiotqueries WHERE post_id=?', (winner,))
        winner = (c.fetchone()[1])
    print(winner)
    return winner


# connects to db
def data_base():
    conn = sqlite3.connect('idiotqueries.db', check_same_thread=False)
    global c
    c = conn.cursor()


def main():
    data_base()
    words = 'что куда'
    bd_parse(words)


if __name__ == '__main__':
    main()

