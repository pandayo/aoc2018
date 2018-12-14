def printRecipes(recipes, indices):
    output = ""
    for ind, score in enumerate(recipes):
        if not ind in indices:
            output += " {0} ".format(score)
        elif ind == indices[0]:
            output += "({0})".format(score)
        else:
            output += "[{0}]".format(score)
    print(output)

def printFlat(recipes):
    output = ""
    for score in recipes:
        output += "{0}".format(score)
    return(output)

def solvePart(puzzle_input, debug = False):

    recipes = [3,7]
    indices = (0,1)

    while len(recipes) < (puzzle_input+10):
        newRecipe = recipes[indices[0]]+recipes[indices[1]]
        if(newRecipe > 9):
            tens = newRecipe // 10
            recipes.append(tens)
            newRecipe = newRecipe % 10
        recipes.append(newRecipe)
        indices = ((indices[0]+1+recipes[indices[0]]) % len(recipes),
                   (indices[1]+1+recipes[indices[1]]) % len(recipes))
        if debug:
            printRecipes(recipes,indices)
    score = recipes[-10:]
    output = ""
    for s in score:
        output = output+str(s)
    return(output)

def solvePart2(puzzle_input):    
    recipes = [3,7]
    indices = (0,1)
    str_recipes = printFlat(recipes)
    check = [int(c) for c in str(puzzle_input)]
    count = len(check)

    while not (check == recipes[-count:] or
               check == recipes[-count-1:-1]):
        newRecipe = recipes[indices[0]]+recipes[indices[1]]
        if(newRecipe > 9):
            tens = newRecipe // 10
            recipes.append(tens)
            newRecipe = newRecipe % 10
        recipes.append(newRecipe)
        indices = ((indices[0]+1+recipes[indices[0]]) % len(recipes),
                   (indices[1]+1+recipes[indices[1]]) % len(recipes))
    if check == recipes[-count:]:
        return(len(recipes)-count)
    else:
        return(len(recipes)-count-1)
        
def part2(inp):
    scores = [3, 7]
    blah = list(map(int, inp))

    a, b = 0, 1

    while True:
        asd = str(scores[a] + scores[b])
        scores.extend(map(int, asd))
        a += scores[a] + 1
        b += scores[b] + 1
        a %= len(scores)
        b %= len(scores)
        if scores[-len(blah):] == blah or scores[-len(blah)-1:-1] == blah:
            break

    if scores[-len(blah):] == blah:
        print(len(scores) - len(blah))
    else:
        print(len(scores) - len(blah) - 1)
    
print(solvePart(9, True))
print(solvePart(18))
print(solvePart(2018))
print(solvePart(909441))

print(solvePart2("51589"))
print(solvePart2("01245"))
print(solvePart2("92510"))
print(solvePart2("59414"))
print(solvePart2("909441"))
