
def common_searches(common_words, products):

    keywords_list = []

    # Loop through products
    for product in products:
        # Loop through words
        for word in common_words:
            # Append combinations
            keywords_list.append(product + ' ' + word)
            keywords_list.append(word + ' ' + product)

    return keywords_list

def check_input(searches):

    inp = input()
    possible_searches = []

    for i in searches:
        if inp.lower() in i[0:len(inp)].lower():
            possible_searches.append(i[len(inp):])
    return possible_searches

if __name__ == '__main__':
    words = ["price", "discount", "promotion", "promo", 'cheap', 'low budget', 'led',
             'gaming', 'office', 'hp', 'lenovo', 'office']

    products = ['pc', 'laptop', 'mouse', 'keyboard', 'headsets', 'Processors', 'graphics cards']

    searches = common_searches(words, products)
    #search examples [pr, le, pc, lap, laptop]
    print(check_input(searches))
