class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashset = defaultdict(set)
        col_hashset = defaultdict(set)
        sub_hashset = defaultdict(set)

        for x in range(9):
            for y in range(9):

                if board[x][y] == '.':
                    continue
                curr_value = board[x][y]
                # checking no duplicates in row
                
                if curr_value in row_hashset[x]:
                    return False
                row_hashset[x].add(curr_value)
                # checking no duplicates in col
                
                if curr_value in col_hashset[y]:
                   return False
                col_hashset[y].add(curr_value)
                
                # checking duplicates in sub boxes
                
                if curr_value in sub_hashset[x//3, y//3]:
                   return False
                sub_hashset[x//3,y//3].add(curr_value)
        return True

                