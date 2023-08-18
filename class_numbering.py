# Author: Debarchan Chatterjee
# creation date : 1 Aug 2023

class class_numbering():

    """
        This function is used to put the class number in front of each class used during unpivot operation.
        The format is like cl_<postion of the class in the list of classes>. 
        Example : x_cat = [0 ... 2 , 2 ... 4, 4 ...6] . Then after using this function the x_cat will be [cl_01_0 ... 2, cl_02_2 ... 4 , cl_03_4 ... 6].

        Parameters :: \n
                       my_list : type(list) --> The list containing the classes without class numbering.

    """
    def __init__(self, my_list):
        
        self.my_list = my_list

        # self.name = name

        assert isinstance(self.my_list, list), "Only list type is allowed as input and the provided data type is {}".format(type(self.my_list)) 
            
        self.x_cat_new = []

        # self.numbering()

    def numbering(self): 

            
        var = len(self.my_list)
            
        for i in range(var):
            class_num = 'cl_{:02d}'.format(i+1)
            new_class = str(class_num) + '_' + str(self.my_list[i])
            self.x_cat_new.append(new_class)

        return self.x_cat_new
