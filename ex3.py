my_stack = []
top_index = 0
size = 50


def is_empty(stack):
    return len(stack) == 0


def push(argument):
    global my_stack,size,top_index

    if  0 <= top_index <= size-1:
        my_stack += [argument]
        top_index += 1
        return True
    if 0 > top_index >= size:
      return False

def pop():

    global my_stack,top_index
    if is_empty(my_stack):
        return False
    else:
        a = my_stack[top_index-1]
        my_stack = my_stack[:top_index-1]
        top_index -= 1
        return a


class node:

    def __init__(self ,data, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

class linkedlist:

    def __init__(self):
        self.head = None

    def showhead(self):
        return self.head

    def add_element(self,data):
        if self.head is None:
            self.head = node(data)
        else:
            our_node = self.head
            while our_node.next is not None:
                our_node = our_node.get_next()
            new_node = node(data)
            our_node.set_next(new_node)
    
    def add_at_start(self,data):
        currnode = self.head
        new = node(data)
        new.set_next(currnode)
        self.head = node

    def insert_after(self,x, data):

        currnode = self.head
        while currnode is not None:
            if currnode.get_data() == x:
                break
            currnode = currnode.get_next()

        if currnode is None:
            print("Item not in list")
        else:
            new = node(data)
            new.next = currnode.next
            currnode.set_next(new)

    def search_data(self,data):
        currnode = self.head

        if currnode is None:
            print("Empty list")
            return
        while currnode is not None:
            if currnode.get_data() == data:
                print("Item found")
                return True

            currnode = currnode.get_next()


        print("Item not found")
        return False


    def insert_before(self,x,data):
        currnode = self.head

        if currnode is None:
            print("Empty list")

        if x == currnode.get_data():
            new = node(data)
            new.set_next(self.head)
            self.head = new

        while currnode.get_next() is not None:
            if currnode.next.get_data() == x:
                break

        if currnode.get_next() is None:
            print("Item not in list")
        else:
            new = node(data)
            new.set_next(currnode.next)
            currnode.set_next(new)



    def size_of_list(self):
        if self.head is None:
            return 0
        our_node = self.head
        length = 1
        while our_node.get_next() is not None:
            length += 1
            our_node = our_node.get_next()
        return length


    def printlist(self):
        currnode = self.head
        while currnode is not None:
            print(currnode.get_data())
            currnode = currnode.get_next()


    def delate_element(self,data):

        headvalue = self.head
        previous = None

        if headvalue is not None:
            if headvalue.get_data() == data:
                self.head = headvalue.get_next()
                headvalue = None
                return

        while headvalue is not None:
            if headvalue.get_data() == data:
                break
            previous = headvalue
            headvalue = headvalue.get_next()

        if headvalue is None:
            return

        previous.next = headvalue.next
        headvalue = None


def check_palindrom():

    link = linkedlist()

    string = input("STRING: ")
    tokens = string.strip()

    for letter in tokens:
        push(letter)

    for token in my_stack:
        link.add_element(token)

    a = pop()
    data = link.head.get_data()

    if a != data:
        print("NOT A PALINDROM")
        return 1
    while not is_empty(my_stack):
        a = pop()
        link.head = link.head.get_next()
        data = link.head.get_data()
        if a != data:
            print("NOT A PALINDROM")
            return 1

    print("PALINDROM")
    return 0


if __name__ == '__main__':
    check_palindrom()

