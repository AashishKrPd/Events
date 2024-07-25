def remove_match_char(list1, list2):
    list1 = list(list1)
    list2 = list(list2)
    # print(type(list1))
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.append(c)
                list2.append(c)
                list3 = list1 + ["*"] + list2
                return [list3, False]
    # print(type(list1))
    list3 = list1 + ["*"] + list2
    return [list3, False]


if __name__ == '__main__':
    p1 = input("Player 1 name: ")
    # p1 = "Aashish"
    p1 = p1.lower()
    p1 = p1.replace(" ", "")
    p1_list = list(p1)
    
    # p2 = "Kumar"
    p2 = input("Player 2 name: ")
    p2 = p2.lower()
    p2 = p2.replace(" ", "")
    p2_list = list(p2)
    
    proceed = True
    
    while proceed:
        print(proceed)
        re_list = remove_match_char(p1_list, p2_list)
        con_list = re_list[0]
        proceed = re_list[1]
        
        star_index = con_list.index("*")
        p1_list = con_list[star_index]
        p2_list = con_list[star_index + 1]
        
        count = len(p1_list) + len(p2_list)
        result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
        
        while len(result) < 1:
            split_index = (count%len(result) - 1)
            if split_index <= 0:
                right = result[split_index + 1]
                left = result[split_index]
                result = right+left
            else:
                result = result[:len(result) - 1]
        print("Relationship Status :", result[0])
    
    