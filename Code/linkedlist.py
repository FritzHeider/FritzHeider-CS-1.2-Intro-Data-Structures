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
        self.head = None
        self.tail = None
        self.count = 0
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
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def count_length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because we traverse through all nodes."""
        count = 0
        targ_node = self.head
        while targ_node is not None:
            count += 1
            targ_node = targ_node.next

        return count

    def length(self):
        """ Return count for the length of the linked list."""
        return self.count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
         Running time: O(1) under any circumstances because you add new node after the tail."""

        next_node = Node(item)
        if self.head is None:
            self.head = next_node
            self.tail = next_node
        else:
            targ_node = self.tail
            targ_node.next = next_node
            self.tail = targ_node.next

        self.count += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
         Running time: O(1) because you add new item at the beginning of the list"""
         
        next_node = Node(item)
        if self.head is None:
            self.head = next_node
            self.tail = next_node
        else:
            next_node.next = self.head
            self.head = next_node

        self.count += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
         Best case running time: O(1) when first item satisfies the given quality
         Worst case running time: O(n) because you have to traverse through all nodes when the last item satisfiesthe given quality or there is no item"""

        targ_node = self.head
        while targ_node is not None:
            if quality(targ_node.data):
                return targ_node.data
            targ_node = targ_node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
         Best case running time: O(1) when given item is equal to the head.
         Worst case running time: O(n) when given item is equal to the tail or there is no item in list"""

        first_len = self.length()
        targ_node = self.head
        last_node = None
        while targ_node is not None:
            if targ_node.data == item:
                self.count -= 1
                if last_node is not None:
                    last_node.next = targ_node.next
                    if self.tail.data == item:
                        self.tail = last_node

                else:

                    if targ_node.next is None:
                        self.tail = None
                        self.head = None
                        break

                    else:
                        self.head = targ_node.next
                        targ_node = self.head
            last_node = targ_node
            targ_node = targ_node.next

        new_len = self.length()
        if first_len == new_len:
            raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, new_item):
        """Replace the given item from the linked list with a new item."""
        node = self.head
        while node is not None:
            if node.data == item:
                node.data = new_item
                return

            node = node.next

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
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
