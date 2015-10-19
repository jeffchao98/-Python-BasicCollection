class Search(object):
    def BinarySearch(self, list_input, m_searchItem):
        #Input: list and search element, Output: id of the founded position, but return -1 if no found
        #Core idea: Set the i_low and i_high as the left border and the right border, determine the i_mid(the middle position) by i_low and i_high
        #if search item not equal as the value of the middle position, rearrange i_low or i_high, if do equal, return the middle position
        i_rtPosition = -1
        i_lenList = len(list_input)
        
        if i_lenList==0:
            pass
        else:
            list_input.sort()
            i_low = 0
            i_high = i_lenList-1
            while i_high>=i_low:
                i_mid = int((i_low+i_high)/2)
                #If do equal, return the middle position
                if list_input[i_mid] == m_searchItem:
                    i_rtPosition = i_mid
                    break
                else:
                    #rearrange i_low if search item grater than the middle value
                    if m_searchItem > list_input[i_mid]:
                        i_low = i_mid+1
                    #rearrange i_high if search item less than the middle value
                    else:
                        i_high = i_mid-1
        return i_rtPosition
    
    
    def SelectionSearch(self, list_input, m_bigK):
        #Also know as the Selection Problem
        #Input: list and specified position k, Output: value of k-th biggest in array, but return None if no found or k grater list length
        #Core idea:Gather front k elements of the input list in a new list (non-sort), sort from large to small, compare rest of elements
        #if grater then kth in the new list->insert to the proper position and kick out the last one(the original kth element), if less or equal then pass
        #Return the latest kth element in final
        
        #TBM: insert and pop must be replaced with no-BIF way
        i_rtVal = None
        i_lenList = len(list_input)
        
        if i_lenList==0 or m_bigK>i_lenList:
            pass
        else:
            list_tmpSub = []
            #Gather front k elements of the input list in a new list
            for each_id in range(m_bigK):
                list_tmpSub.append(list_input[each_id])
            #Sort from large to small
            list_tmpSub.sort(reverse=True)
            for each_id in range(m_bigK,i_lenList):
                #If grater then kth in the new list->insert to the proper position and kick out the last one
                if list_input[each_id]>list_tmpSub[m_bigK-1]:
                    for each_sub in range(m_bigK):
                        if list_input[each_id]>list_tmpSub[each_sub]:
                            list_tmpSub.insert(each_sub, list_input[each_id])
                            list_tmpSub.pop()
                            break
            i_rtVal = list_tmpSub[m_bigK-1]
        return i_rtVal