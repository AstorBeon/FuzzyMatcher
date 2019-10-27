
def count_similarity_percent(one, two):
    one=one.upper().replace(" ",'')
    two=two.upper().replace(" ",'')

    #todo combine all different combinations of multiple words

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




    print("Longest similar: " + str(longestsimilar))
    if len(two)>len(one):

        return longestsimilar*100/len(two)
    else:
        return longestsimilar * 100 / len(one)
    #todo cover scenario with sentences, not only words

def match_by_length(one,two,handicap):
    if len(one) in range(len(two)-handicap,len(two)+handicap):
        return True
    else:
        return False

def simple_fuzzy_match(one,two, percent):

    if count_similarity_percent(one,two)>=percent:
        return True
    else:
        return False



print(simple_fuzzy_match("Brad ford","cityradf ord",40))
