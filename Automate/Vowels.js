function containsVowel(s) {
    const vowels = 'aeiouAEIOU';
    for (let i = 0; i < s.length; i++) {
        if (vowels.indexOf(s.charAt(i)) !== -1) {
            return true;
        }
    }
    return false;
}
const string = "Hello World";
if (containsVowel(string)) {
    console.log("The string contains at least one vowel.");
} else {
    console.log("The string does not contain any vowels.");
}