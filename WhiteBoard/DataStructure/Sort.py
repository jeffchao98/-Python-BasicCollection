class Sort(object):
    #Insert Sort : Input Type - array, No Output and we will change the content of the input
    def InsertSort(self, list_input):
        i_lenlist = len(list_input)
        if i_lenlist>1:
            #Do scan from 2nd to the last
            for each_id in range(1,i_lenlist):
                for each_sub in reversed(range(0,each_id)):
                    #When we scan, we will switch pair by pair to the head, however, we will break it when the last one is not grater than current one
                    if list_input[each_sub+1]<list_input[each_sub]:
                        m_tmp = list_input[each_sub+1]
                        list_input[each_sub+1] = list_input[each_sub]
                        list_input[each_sub] = m_tmp
                    else:
                        #print("===>>>"+str(list_input))
                        break
    #Selection Sort : Input Type - array, No Output and we will change the content of the input
    def SelectionSort(self, list_input):
        i_lenlist = len(list_input)
        if i_lenlist>1:
            for each_id in range(i_lenlist):
                i_minId = each_id
                #We will scan in a range [k, input length], k is between in 0 and input length
                for each_sub in range(each_id,i_lenlist):
                    if list_input[i_minId]>list_input[each_sub]:
                        i_minId = each_sub
                #The lowest position will determined in the loop
                #Then we switch the value of the position with the head position of the sub range
                i_tmp = list_input[each_id]
                list_input[each_id] = list_input[i_minId]
                list_input[i_minId] = i_tmp