class Bakehouse():
    __occupied_table_list=[1,1,1,0,0,0,0,0,0,0]

    def get_occupied_table_list(self):
        #print("here3")

        global __occupied_table_list

        list=[]
        for i in range(len(self.__occupied_table_list)):
            
            if self.__occupied_table_list[i]==1:
                #print("append",i)
                list.append(i)
        return list

    def allocate_table(self):

            for i in range(10):
                if self.__occupied_table_list[i]==0:
                    self.__occupied_table_list[i]=1
                    #print("here allocated")
                    

                    break

    def deallocate_table(self,table_number):
            self.__occupied_table_list[table_number]=0

B=Bakehouse()
#print("here1")
print("initial state")
l=B.get_occupied_table_list()
for i in l:
    print(i)

#print("here2")
    
B.allocate_table()
B.allocate_table()
print("after allocating 2 more seats")
l=B.get_occupied_table_list()
for i in l:
    print(i)

    
B.deallocate_table(3)
print("after deallocating seat")

l=B.get_occupied_table_list()
for i in l:
    print(i)
print("again allocate")
B.allocate_table()

l=B.get_occupied_table_list()
for i in l:
    print(i)






        
