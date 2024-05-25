# You and your books

class Solution:
    # Function should return an integer
    # a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        max_books = 0
        current_books = 0
        start = 0

        for end in range(n):
            if arr[end] <= k:
                current_books += arr[end]
                max_books = max(max_books, current_books)
            else:
                current_books = 0

        return max_books
