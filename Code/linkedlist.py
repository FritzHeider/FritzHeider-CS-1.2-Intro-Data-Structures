#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node

        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        #starting at head node
        node = self.head  # O(1) time to assign new variable
        #While loop untill node is none,
        while node is not None:  #avoid early return
            items.append(node.data)
            # append it and move on
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        num_nodes = 0
        pointer = self.head

        if self.head == None:
            return 0
        #Loop as long as there are more in list
        num_nodes = 1
        while pointer.next is not None:
        #keep adding to iterate
            pointer = pointer.next
            num_nodes += 1



        print(num_nodes)
        return num_nodes

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        #create node if needed
        if self.head == None:
            my_node = Node(item)
            self.head = my_node
            self.tail = my_node

        elif self.head != None:
            pointer = self.tail
            #Was long as there are more nodes
            #append the node to where we are at
            my_node = Node(item)
            pointer.next = my_node
            self.tail = my_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) because in each case there is only one thing to check
        and therefore to iterate over"""
        # create a new node
        if self.head == None:
            my_node = Node(item)
            self.head = my_node
            self.tail = my_node

        # Prepend node before head, if it exists
        elif self.head != None:
            my_node = Node(item)
            og_head = self.head
            self.head = my_node
            self.head.next = og_head

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If there is no head, then there is only one
        thing to check and iterate over.
        Worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""

        if self.head == None:
            return NotImplemented

        if self.head != None:
            pointer = self.head
            #Loop through everything
            while pointer != None:
                if (quality(pointer.data)):
                    return pointer.data
                pointer = pointer.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) because in the best case scenario, there are
        no nodes and therefore only one task has to be executed
        Worst case running time: O(n^2) because in all other scenarios there are many
        items that need to be iterated over in a few diffrent loops"""

        if self.length() == 0:
            raise ValueError('Item not found: {}'.format(item))

        pointer = self.head
        saved_previous = None

        #WHile no nodes
        while pointer != None:
                #if we find we are on it
            if pointer.data == item:
                if pointer.next != None:
                    if saved_previous != None:
                        saved_previous.next = pointer.next
                    if saved_previous == None:
                        self.head = pointer.next
                    pointer.next = None
                    return
                if pointer.next == None:
                    if saved_previous != None:
                        saved_previous.next = None
                        self.tail = saved_previous
                    if saved_previous == None:
                        self.head = None
                        self.tail = None
                    return
            saved_previous = pointer
            pointer = pointer.next
        raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

        print('\nTesting prepend:')
    for item in ['A', 'B', 'C']:
        print('prepend({!r})'.format(item))
        ll.prepend(item)
        print('list: {}'.format(ll))

    print('length: {}'.format(ll.length()))

    print(ll.find ('a'))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    after_del = True
    if after_del:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
