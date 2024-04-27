import java.util.*;

class ValidSudoku{
    public static void main(String[] args) {
        char[][] board = {{'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}};
        boolean bool = false;
        bool = isValidSudoku(board);
        System.out.println(bool);
        return;
    }

    public static boolean isValidSudoku(char[][] board) {
        HashSet<String> seen = new HashSet<>();
        for (int i=0; i<board.length; i++){
            for (int j=0; j<board[i].length; j++){
                char number = board[i][j];
                if (number != '.'){
                    if ((!seen.add(number + " in row " + i)) || (!seen.add(number + " in column" + j)) || (!seen.add(number + " in block " + i/3 + " - "+ j/3))){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}