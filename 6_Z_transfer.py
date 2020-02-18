class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        my_list = ["" for i in range(numRows)]
        down = True  #控制row++ 还是 row--
        row = 0

        for char in s:

            # if down == True:
            #     my_list[row] += char
            #     row += 1
            # else:
            #     my_list[row] += char
            #     row -= 1

            my_list[row] += char
            row = row+1 if down == True else row-1

            if row == 0 or row == numRows-1:
                down = False if down == True else True

        res = "".join(my_list)
        return res


