class Permutations(object):
    #Input: string, Output: all result of permutations in list
    #Core Idea: If input length is 1, put the only character in the array and return. 
    #If grater than 1, catch every character as head and send remains to Permutations in each loop, 
    #when array of result back, add the head character before every strings in return array, add to new array and return
    def Permutations(self, str_input):
        str_rt = ""
        list_rtStr = []
        i_lenInput = len(str_input)
        if i_lenInput == 0:
            pass
        #If input length is 1, put the only character in the array and return. 
        elif i_lenInput == 1:
            list_rtStr.append(str_input)
        else:
            for each_id in range(i_lenInput):
                str_tmp = str_input
                #catch every character as head
                str_tmpC = str_input[each_id]
                #send remains to Permutations
                list_tmp = self.Permutations(str_tmp[0:each_id]+str_tmp[each_id+1:i_lenInput])
                i_lenTmpL = len(list_tmp)
                #add the head character before every strings in return array
                for each_sub in range(i_lenTmpL):
                    tmp_addItem = str_tmpC+list_tmp[each_sub]
                    if tmp_addItem not in list_rtStr:
                        list_rtStr.append(tmp_addItem)
        return list_rtStr
            