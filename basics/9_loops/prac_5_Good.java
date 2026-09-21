public class prac_5_Good{

    static char firstNonRepeatingChar(String str) {
            char ans=' ';
            for(char ch: str.toCharArray()){
                int firstIndex = str.indexOf(ch);
                int lastIndex = str.lastIndexOf(ch);
                if(firstIndex == lastIndex) return ch;
            }
            return ' ';
    }
    public static void main(String[] args) {
        String str = "hello";
        System.out.println(firstNonRepeatingChar("aaaabbbbccf"));
    }
}