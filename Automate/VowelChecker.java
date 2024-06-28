public class VowelChecker {

    public static boolean containsVowel(String s) {
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++) {
            if (vowels.indexOf(s.charAt(i)) != -1) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String string = "Hello World";
        if (containsVowel(string)) {
            System.out.println("The string contains at least one vowel.");
        } else {
            System.out.println("The string does not contain any vowels.");
        }
    }
}
