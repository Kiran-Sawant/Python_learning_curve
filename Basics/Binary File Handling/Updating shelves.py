import shelve

#_________creating objects to shelve___________#
blt = ['bacon', 'lettuce', 'tomato', 'bread']
beansOnToast = ['beans', 'bread']
scrambledEggs = ['eggs', 'butter', 'milk']
soup = ['tin of soup']
pasta = ['pasta', 'cheese']

#____________Creating a shelve________________#
with shelve.open('recipes', writeback=True) as recipes: #writeback allows the program to continuously access disk
    recipes['blt'] = blt                                #writeback=True consumes lot of memory
    recipes['beans on toast'] = beansOnToast
    recipes['scrambled eggs'] = scrambledEggs
    recipes['pasta'] = pasta
    recipes['soup'] = soup

#____________updating objects in shelve__________#
    recipes['blt'].append('butter') # Adding values to the list in shelve with key['blt']
    recipes['pasta'].append('Italian')

    #___updating without using writeback=True___#
    data = recipes['pasta']
    data.append('yummy')
    recipes['pasta'] = data

    for snack in recipes: #Iterating through the keys in shelve recipes
        print(snack, recipes[snack])