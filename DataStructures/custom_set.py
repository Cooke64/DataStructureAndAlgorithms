class MySet:
    def __init__(self):
        self.__set_size = 10
        self.__my_new_set = [[] for _ in range(self.__set_size)]

    def get_set(self):
        return self.__my_new_set

    def add_item(self, item):
        for finding in self.__my_new_set[item % self.__set_size]:
            if finding != item:
                self.__my_new_set[item % self.__set_size].append(item)

    def get_item(self, item):
        for finding in self.__my_new_set[item % self.__set_size]:
            if finding == item:
                return True
            else:
                return False

    def delete_item(self, item):
        list_of_items = self.__my_new_set[item % self.__set_size]
        for i in range(len(list_of_items)):
            if list_of_items[i] == item:
                list_of_items[i] = list_of_items[len(list_of_items)-1]
                list_of_items.pop()


custom_set = MySet()
