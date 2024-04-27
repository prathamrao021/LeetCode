class LengthOfLastWord {
    public static void main(String args[]){
        String s = "a";
        int j = lengthOfLastWord(s);
        System.out.println(j);
    }

    public static int lengthOfLastWord(String s){
        int ending_index = s.length()-1;
        int starting_index = s.length()-1;
        boolean set_ending = false;
        s = s.trim();
        for (int i=s.length()-1;i>-1;i--){
            if (s.charAt(i) == ' '){
                starting_index ++;
                return (ending_index - starting_index + 1);
            }
            if (Character.isAlphabetic(s.charAt(i))){
                if (set_ending){
                    starting_index--;
                    continue;
                }
                set_ending = true;
                starting_index--;
            }
        }
        if (starting_index == -1){
            return (ending_index + 1);
        }
        return (ending_index - starting_index + 1);
    }
}