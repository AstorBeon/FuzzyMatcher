
############## tech functs
def generate_possible_combinations(string):
    #returns list of possible strings
    tab=string.split(" ")
    result=[]
    for i in range(0, len(tab) + 1):
        for combo in itertools.combinations(tab, i):
            result.append(combo)


####################
def count_similarity_percent(one, two):
    one=one.upper().replace(" ",'')
    two=two.upper().replace(" ",'')



    if two.__contains__(one):
        return len(one) * 100 / len(two)

    elif one.__contains__(two):
        return len(two) * 100 / len(one)


    #If none contains none, lets check for longest similar
    longestsimilar=0
    #from 1 because from 0 would check whole word, and it doesnt make sence
    for i in range(1,len(one)):
       if two.__contains__(one[i:]) or two.__contains__(one[:(-1)*(len(one)-i)]):
           if len(one)-i> longestsimilar:
               longestsimilar=len(one)-i

    for i in range(1,len(two)):
       if one.__contains__(two[i:]) or one.__contains__(two[:(-1)*(len(two)-i)]):
           if len(two)-i> longestsimilar:
               longestsimilar=len(two)-i

    if len(two)>len(one):

        return longestsimilar*100/len(two)
    else:
        return longestsimilar * 100 / len(one)
    #todo cover scenario with sentences, not only words

def match_by_length(one,two,diff):
    if len(one) in range(len(two)-diff,len(two)+diff):
        return True
    else:
        return False

def simple_match(one,two, percent):

    if count_similarity_percent(one,two)>=percent:
        return True
    else:
        return False



print(simple_match("Brad ford","cityradf ord",40))

for i in generate_possible_combnations("uno dos tres"):
    print(i)



#todo function to merge dataframes