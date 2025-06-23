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

    def split_massages(self, massages: List[List[int]]) -> List[List[int]]:
        chunks = []

        for msg in massages:
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