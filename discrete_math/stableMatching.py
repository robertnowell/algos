def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n                      
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n                      
    # Each man made 0 proposals, which means that 
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n                       

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]                      
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]       
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]] 
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]

# if she doesn't have a husband, current man is her husband
# else: check her preference.
# If she ranks current man higher than her husband:
# make current man her husband
# add previous husband to unmarriedMen


        # Now "he" proposes to "she". 
        # Decide whether "she" accepts, and update the following fields
        # 1. manSpouse
        # 2. womanSpouse
        # 3. unmarriedMen
        # 4. nextManChoice
        # import pdb; pdb.set_trace()

        if currentHusband is None:
            manSpouse[he] = she
            womanSpouse[she] = he
            unmarriedMen.remove(he)
            nextManChoice[he] += 1
        else:
            if herPreferences.index(he) < herPreferences.index(currentHusband):
                manSpouse[he] = she
                womanSpouse[she] = he
                unmarriedMen.remove(he)
                nextManChoice[he] += 1
                unmarriedMen.append(currentHusband)
            else:
                nextManChoice[he] += 1
    # Note that if you don't update the unmarriedMen list, 
    # then this algorithm will run forever. 
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse

# You might want to test your implementation on the following two tests:
# print stableMatching(1, [ [0] ], [ [0] ]) == [0]
# print stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1]
print stableMatching(2, [ [0,1], [0,1] ], [ [0,1], [1,0] ])