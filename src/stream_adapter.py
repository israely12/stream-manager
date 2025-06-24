from typing import List


class StreamAdapter:
    def __init__(self):
        self.fill_numbers = [1, 2]
        self.fill_index = 0
        self.carry_over = []

    def fill_to_12(self, arr: List[int]) -> List[int]:
        while len(arr) < 12:
            arr.append(self.fill_numbers[self.fill_index])
            self.fill_index = (self.fill_index + 1) % 2
        return arr

    def replace_555_with_666(self, arr: List[int]) -> List[int]:
        arr = arr[:]
        i = 0
        while i < len(arr):
            if arr[i] == 5:
                count = 1
                j = i + 1
                while j < len(arr) and arr[j] == 5:
                    count += 1
                    j += 1
                if count >= 3:
                    for k in range(i, i + count):
                        arr[k] = 6
                    i = j
                else:
                    i += 1
            else:
                i += 1
        return arr

    def split_massages(self, massages: List[List[int]]) -> List[List[int]]:
        chunks = []

        for msg in massages:
            msg = self.replace_555_with_666(msg)
            if self.carry_over:
                needed = 12 - len(self.carry_over)
                to_take = msg[:needed]
                self.carry_over.extend(to_take)

                chunks.append(self.carry_over)
                self.carry_over = []

                msg = msg[needed:]
            start = 0
            length = len(msg)
            while start < length:
                part = msg[start:start + 12]
                if len(part) < 12:
                    filled = self.fill_to_12(list(part))
                    chunks.append(filled)
                    start = length
                else:
                    chunks.append(part)
                    start += 12

        return chunks
