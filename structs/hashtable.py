def hash_func(num_buckets, key):
    return key % num_buckets


class ChainingHashTable:
    def __init__(self, initial_capacity=10):
        """
        Constructor with optional initial capacity parameter.
        Assigns all buckets with an empty list.
        """
        self.table = [[] for i in range(initial_capacity)]

    def _get_bucket_index(self, item):
        return hash(item) % len(self.table)

    def insert(self, item):
        """Inserts a new item into the hash table."""
        bucket = self._get_bucket_index(item)
        self.table[bucket].append(item)

    def search(self, key):
        """Searches for an item with matching key"""
        bucket = self._get_bucket_index(key)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            index = bucket_list.index(key)
            return bucket_list[index]  # return item at index

        return None

    def remove(self, key):
        """Removes an item with matching key from the hash table"""
        bucket = self._get_bucket_index(key)
        bucket_list = self.table[bucket]

        if key in bucket_list:
            bucket_list.remove(key)


class EmptyBucket:
    """Class to represent an empty bucket type"""

    pass


class LinearHashTable:
    """Each bucket holds single item and we insert in next available empty position"""

    def __init__(self, num_buckets=10):
        # special constants for two types of empty buckets
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        self.table = [self.EMPTY_SINCE_START for _ in range(num_buckets)]
        self.num_buckets = num_buckets

    def __str__(self):
        return str([str(item) for item in self.table])

    def insert(self, key):
        bucket = hash_func(self.num_buckets, key)
        buckets_probed = 0

        while buckets_probed < self.num_buckets:
            # insert item in next empty bucket
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = key
                return True

            # increment bucket index (constrained with modulo)
            bucket = (bucket + 1) % self.num_buckets

            # increment number of buckets probed
            buckets_probed += 1
        return False

    def remove(self, key):
        # determine initial bucket
        bucket = hash_func(self.num_buckets, key)
        probed = 0

        while (
            self.table[bucket] is not self.EMPTY_SINCE_START
            and probed < self.num_buckets
        ):
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL
                return

            bucket = (bucket + 1) % self.num_buckets
            probed += 1

    def search(self, key):
        # initial bucket
        bucket = hash_func(self.num_buckets, key)
        probed = 0

        while (
            self.table[bucket] is not self.EMPTY_SINCE_START
            and probed < self.num_buckets
        ):
            if self.table[bucket] == key:
                return self.table[bucket]

            bucket = (bucket + 1) % self.num_buckets
            probed += 1
        return None  # not found


class DoubleHashingTable:
    """Hash table with double hashing"""

    def __init__(self, initial_capacity=10):
        # the 'is' check will which instance it is
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()
        self.table = [self.EMPTY_SINCE_START for _ in range(initial_capacity)]

    def _compute_double_hash(self, item, i):
        h2 = 7 - hash(item) % 7
        return (hash(item) + h2 * i) % len(self.table)

    def insert(self, item):
        for i, _ in enumerate(self.table):
            # calculate bucket index using i
            bucket = self._compute_double_hash(item, i)
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item  # can insert
                return True
        return False

    def search(self, key):
        for i, _ in enumerate(self.table):
            bucket = self._compute_double_hash(key, i)
            if self.table[bucket] == key:
                return self.table[bucket]
        return None

    def remove(self, key):
        for i, _ in enumerate(self.table):
            bucket = self._compute_double_hash(key, i)
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL


class QuadHashTable:
    """Each bucket holds single item and we insert in next available empty position"""

    def __init__(self, num_buckets):
        self._empty = "E"
        self._removed = "R"
        self.table = [self._empty for _ in range(num_buckets)]
        self.num_buckets = num_buckets

    def _quadratic_probing_sequence(self, first_hash, i):
        return (first_hash + i + (i * i)) % self.num_buckets

    def __str__(self):
        return str([str(item) for item in self.table])

    def insert(self, key):
        i = 0
        probed = 0
        bucket = hash_func(self.num_buckets, key)
        first_hash = bucket

        while probed < self.num_buckets:
            # insert item in next empty bucket
            if self.table[bucket] in (self._empty, self._removed):
                self.table[bucket] = key
                return True

            # increment i and recompute bucket
            i += 1
            bucket = self._quadratic_probing_sequence(first_hash, i)
            probed += 1
        return False

    def remove(self, key):
        i = 0
        probed = 0
        bucket = hash_func(self.num_buckets, key)
        first_hash = bucket

        while self.table[bucket] != "empty" and probed < self.num_buckets:
            if self.table[bucket] != self._empty and self.table[bucket] == key:
                self.table[bucket] = self._removed
                return True
            i += 1
            # compute next index
            bucket = self._quadratic_probing_sequence(first_hash, i)
            # increment buckets probed
            probed += 1
        return False

    def search(self, key):
        i = 0
        probed = 0
        bucket = hash_func(self.num_buckets, key)
        first_hash = bucket

        while self.table[bucket] != self._empty and probed < self.num_buckets:
            if self.table[bucket] == key:
                return self.table[bucket]

            i += 1
            # compute next index
            bucket = self._quadratic_probing_sequence(first_hash, i)
            # increment buckets probed
            probed += 1
        return None  # not found


if __name__ == "__main__":
    ht = QuadHashTable(16)
    ht.insert(32)
    ht.insert(16)
    ht.insert(64)
    print(ht)
    ht.remove(64)
    print(ht)
    print(ht.search(16))
