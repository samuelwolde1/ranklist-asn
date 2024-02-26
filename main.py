loop = True
rank_list = []

while loop == True:
    print('*** MAIN MENU ***')
    print('1: Print List')
    print('2: Add Item to End')
    print('3: Remove Last Item')
    print('4: Insert at Position')
    print('5: Remove at Position')
    print('6: Move to Position')
    print('7: Edit item')
    print('8: Exit')

    selection = input('Enter option #: ')

    if selection == '1':
        print('Rank List')
        if len(rank_list) <= 0:
            print('No items in the Rank List')
        else:
            for item in rank_list:
                print(str(rank_list.index(item) + 1) + ": " + str(rank_list[rank_list.index(item)]))
    elif selection == '2':
        print('Add Item to End')
        new_item = input('Enter item: ')
        rank_list.append(new_item)
        print('\n Rank List')
        for item in rank_list:
            print(str(rank_list.index(item) + 1) + ": " + str(rank_list[rank_list.index(item)]))
    elif selection == '3':
        print('Remove last item')
        print(str(rank_list.pop()) + " removed from end of list")
        for item in rank_list:
            print('\nRank List')
            print(str(rank_list.index(item) + 1) + ": " + str(rank_list[rank_list.index(item)]))
    elif selection == '4':
        print('\nInsert Item')
        position = input('Insert Position: ')
        item = input('Item to Insert: ')
        rank_list.insert(int(position) - 1, item)
        print('\nRank List')
        for item in rank_list:
            print(str(rank_list.index(item) + 1) + ": " + str(rank_list[rank_list.index(item)]))
    elif selection == '5':
        print('Remove at Position')
        position = input('Position to remove: ')
        print(rank_list[int(position) - 1] + ' removed from position ' + str(position))
        rank_list.pop(int(position) - 1)
        print('\nRank List')
        for item in rank_list:
            print(str(rank_list.index(item) + 1) + ": " + str(rank_list[rank_list.index(item)]))
    elif selection == '6':
        print('Move to Position')
        from_pos = input('Move Item from: ')
        to_pos = input('Move Item to: ')
        moved_item = rank_list.pop(int(from_pos) - 1)
        rank_list.insert(int(to_pos) - 1, moved_item)
        print('\nRank List')
        for item in rank_list:
            print(str(rank_list.index(item) + 1) + ": " + str(rank_list[rank_list.index(item)]))
    elif selection == '7':
        print('Edit Item')
        position = input('Enter position: ')
        new_item = input('Replace with: ')
        rank_list.insert(int(position) - 1, new_item)
        rank_list.pop(int(position) - 1)
        print('\nRank List')
        for item in rank_list:
            print(str(rank_list.index(item) + 1) + ": " + str(rank_list[rank_list.index(item)]))