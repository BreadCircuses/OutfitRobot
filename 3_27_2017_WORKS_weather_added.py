import random

f = open("C:\__KATROSS DELL\_PROGRAMMING\SQL\MySQL Code\Table data_mar_28_comment_fixed.csv", 'r')
data = f.read()

rows = data.split("\n")
nested_list = []

#makes a list of lists with each record as a separate list
for el in rows:
    x = el.split(',')
    nested_list.append(x)
    
#test
#the values start at [1] because the header is ni4 removed
#print (nested_list[217])
print("\n")
#print(nested_list[100][20])

# the 1st one works!
nested_list = [[x.replace(' ','_') for x in l] for l in nested_list]
#it does take the double quotes off longer-than-one-word strings
nested_list = [[x.replace('"',' ') for x in l] for l in nested_list]
#this doesn't work at all  
nested_list = [[x.replace(', ','----') for x in l] for l in nested_list]       
           
def categories(list_name, category_name, category_ID):
# appends lists corresponding to a certain category to a new, empty list
# the values in the inner lists have ni4 been converted to integers/booleans, 
#they are all strings
    for i in list_name:
        catID = i[len(i)-1]
        the_rest = i[0:len(i)-1]
        if catID == category_ID:
            category_name.append(the_rest) 
    return           

print("\n")

list_name = nested_list

tops = []
category_name = tops
categories(nested_list, tops, "1")

bottoms = []
category_name = bottoms
categories(nested_list, bottoms, "2")

outwear = []
category_name = outwear
categories(nested_list, outwear, "3")

dresses_etc = []
category_name = dresses_etc
categories(nested_list, dresses_etc, "4")

shoes = []
category_name = shoes
categories(nested_list, shoes, "5")

bags = []
category_name = bags
categories(nested_list, bags, "6")

def inner_f():
                   
    i1 = random.choice(tops)
    i2 = random.choice(bottoms)
    i3 = random.choice(shoes)
    i4 = random.choice(outwear)
    i5 = random.choice(bags)
    # i6 = random.choice(dresses_etc)
        
    #the whole outfit goes in a list of lists
    #dresses will be dealt with later
    global outfit 
    outfit = []
    outfit.extend((i1, i2, i3, i4, i5))
    
    print("OUTFIT FOR TODAY:" + "\n")
    
    # works but doesn't look nice
    #print('\n''\n'.join(', '.join(map(str,sl)) for sl in outfit))
    # have to at least remove all digits
    
    '''
    #this doesn't work ('int' object has no attribute '__getitem__')
    for i in range(len(outfit)):
        print(i[2]  + ", " + i[3] + ", " + i[5] + ", " + i[7] + ", " + i[9] + "\n" + "+")
    '''
    # old one - result looks cleaner
    print(i1[2] + ", " + i1[3] + ", " + i1[5] + ", " + i1[7] + ", " + i1[9])
    print("+")
    print(i2[2] + ", " + i2[3] + ", " + i2[5] + ", " + i2[7] + ", " + i2[9])
    print("+")
    print(i3[2] + ", " + i3[3] + ", " + i3[5] + ", " + i3[7] + ", " + i3[9])
    #print("+")
    #print(i4[2] + ", " + i4[3] + ", " + i4[5] + ", " + i4[7] + ", " + i4[9])
    print("+")
    print(i5[2] + ", " + i5[3] + ", " + i5[5] + ", " + i5[7] + ", " + i5[9])    
    print("\n")
                                             
    return outfit

def inner_f2(inner_f):
    item = random.choice(outfit)
    return item

def create_outfit():   
        
    
    outfit = inner_f() # creates a list of 5 lists
    item  = inner_f2(outfit) 
    #outfit.remove(item)
    
    def weather(outfit):
        if any(t[6] for t in f) == "CLD" and any(t[6] for t in f) == "WRM":
            inner_f()
        #if item[6] == "WRM" and any(t[6] for t in f) != "WRM" or any(t[6] for t in f) != "ALL":
        #    inner_f()
        if any(t[6] for t in f) == "WNT" and any(t[6] for t in f) != "CLD":
            inner_f()
        #outfit.append(item)
        return outfit  
    
    def shape(outfit):
    # shape check    
        while item[len(item)-6] == any(t[len(t)-6] for t in f):
            inner_f()
            break
        if item[len(item)-1] == "1" and any(t[len(t)-1] for t in f) == "2":
            if item[len(item)-6] == "2" and item[len(item)-6] == "1":
                inner_f()
        outfit.append(item)
        return outfit        
    
    
    def occasion(outfit):
    # occasion check 
        #if item[8] == "C" and any(t[len(t)-10] for t in f) == "C":
        #    inner_f()
        if item[8] == "D" and any(t[len(t)-10] for t in f) == "C":
            inner_f()  
        outfit.append(item)
        return outfit     
     
    
    def color(outfit):
    # COLOR CHECK - new, works!
        while item[len(item)-10] == "bright" and any(t[len(t)-10] for t in f) != "neutral":
            inner_f()
            break
        while item[len(item)-10] == "jewel" and any(t[len(t)-10] for t in f) != "neutral":
            inner_f()
            break
        while item[len(item)-10] == "earth" and any(t[len(t)-10] for t in f) != "neutral" or any(t[len(t)-10] for t in f) != "metallic":
            inner_f()
            break
        while item[len(item)-10] == "pastel" and any(t[len(t)-10] for t in f) != "neutral" or any(t[len(t)-10] for t in f) != "metallic":
            inner_f()
            break
        while item[len(item)-10] == "multi" and any(t[len(t)-10] for t in f) != "neutral" or any(t[len(t)-10] for t in f) != "metallic":
            inner_f()
            break
        while item[len(item)-10] == "neutral" and any(t[len(t)-10] for t in f) != "earth" or any(t[len(t)-10] for t in f) != "metallic" or any(t[len(t)-10] for t in f) != "neutral":
            inner_f()
        while item[len(item)-10] == "metallic" and any(t[len(t)-10] for t in f) != "metallic":
            inner_f()
            break     
        
        outfit.append(item)    
        return outfit
    
    def style(outfit):                
    # style check 
    # "M" stands for "modern", "E" for "everyday" 
    # the probability that either "M" or "E" won't occur in the list
    # at least once, is negligible
        if "M" or "E" in any(t[len(t)-5] for t in f):
            for i in outfit:
                ct = (i[len(t)-5]).count("M")
                ct2 = (i[len(t)-5]).count("E")
            if ct < 1 and ct2 < 1:
                inner_f()
        outfit.append(item)
        # bohemian items look interesting with futuristic ones
        while "B" in any(t[len(t)-5] for t in f) and "F" not in any(t[len(t)-5] for t in f) or "C" not in any(t[len(t)-5] for t in f):
            inner_f()
        # classic and bohemian do not work well together 
        while "B" in any(t[len(t)-5] for t in f) and "C" in any(t[len(t)-5] for t in f):
            inner_f()
        # there must be only one statement item in an outfit
        while "T" in item([len(item)-5]) and "T" in any(t[len(t)-5] for t in f):
            inner_f()
        # add a condition for S HERE
        
        # fabrick check  
        # no wool on wool
        if item[4] == "1" and any(t[4] for t in f) == "1":
            inner_f()
        # no leather on leather, except for shoes
        if item[4] == "4" and any(t[4] for t in f) == "4":
            if [len(item)-1] == "1" and any(t[len(t)-1] for t in f) == "2":
                inner_f()
        return
    
   # add fabric check: no wool on wool, leather on leather
    
    return
    
# NO, there must be main()!
create_outfit()
create_outfit()

#test
#print(nested_list[100:105])












