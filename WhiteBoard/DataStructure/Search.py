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