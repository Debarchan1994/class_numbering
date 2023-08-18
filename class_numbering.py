class class_numbering():
        def __init__(self, my_list):

            
            self.my_list = my_list

            # self.name = name

            assert isinstance(self.my_list, list), "Only list type is allowed as input and the provided data type is {}".format(type(self.my_list)) 

            # self.name = '{}'.format(my_list)
            # self.vari = [ i for i, j in locals().items() if j == my_list][0]
            
            self.x_cat_new = []

            # self.numbering()

        def numbering(self): 

            
            var = len(self.my_list)
            
            for i in range(var):
                class_num = 'cl_{:02d}'.format(i+1)
                new_class = str(class_num) + '_' + str(self.my_list[i])
                self.x_cat_new.append(new_class)

            return self.x_cat_new