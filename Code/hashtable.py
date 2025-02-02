#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n2) all buckets then each key in all buckets must be accessed"""
        # Collect all keys in each bucket
        key_total = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                key_total.append(key)
        return key_total

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n2) again each bucket must be accessed then again nested loop for values"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        value_list = []
        for bucket in self.buckets:
            for _, value in bucket.items():
                value_list.append(value)
        return value_list

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) each bucket is accessed once """
        # Collect all pairs of key-value entries in each bucket
        item_list = []
        for bucket in self.buckets:
            item_list.extend(bucket.items())
        return item_list

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n2) another nested loop"""
        # TODO: Loop through all buckets
        # TODO: num_buckets number of key-value entries in each bucket
        num_buckets = 0
        for bucket in self.buckets:
            for _ in bucket.items():
                num_buckets += 1
        return num_buckets

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(n) worst case its the very last bucket best case 0(1) unlikely"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket = self.buckets[self._bucket_index(key)]
        for key_point, _ in bucket.items():
            if key == key_point:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(n) but its possible it could be O(1)"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]
        for key_point, key_value in bucket.items():
            if key == key_point:
                return key_value
        raise KeyError('Key not found: {}'.format(key))



    def set(self, key, value):
        bucket = self.buckets[self._bucket_index(key)]
        for key_point, key_value in bucket.items():
            if key == key_point:
                bucket.replace((key_point, key_value), (key, value))
                return

        bucket.append((key, value))
        """Insert or update the given key with its ass*****ociated value.
        TODO: Running time: O(n) single loop"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(n) single loop again """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]
        for key_point, key_value in bucket.items():
            if key == key_point:
                bucket.delete((key_point, key_value))
                return
        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))



if __name__ == '__main__':
    test_hash_table()
