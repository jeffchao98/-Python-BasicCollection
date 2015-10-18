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