This function is used to put the class number in front of each class used during unpivot operation or other operations because sometimes when using Power BI or Palantir Foundary the axises are organized based on the 1st letter or value of
an element and hence often results in an unordered axis resulting in a confusing visual representation of data in charts. 
TO mitigate the issue it is good to append a class number infront of a each element so even if the BI tool is using the 1st letter or value of the elements to order the axis still it gets ordered in a correct accending or deccending fashion
as and when required.
        The format is like cl_<postion of the class in the list of classes>. 
        Example : x_cat = [0 ... 2 , 2 ... 4, 4 ...6] . Then after using this function the x_cat will be [cl_01_0 ... 2, cl_02_2 ... 4 , cl_03_4 ... 6]
