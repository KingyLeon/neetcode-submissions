class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sCount = new HashMap<Character,Integer>();
        HashMap<Character, Integer> tCount = new HashMap<Character,Integer>();
        boolean result = true;
        if (s.length() != t.length()) {
            return false;
        }

        for (int i=0; i<s.length(); i++){
            if (!sCount.containsKey(s.charAt(i))){
                sCount.put(s.charAt(i), 1);
            }
            sCount.put(s.charAt(i), sCount.get(s.charAt(i))+1);
        }
        for (int i=0; i<t.length(); i++){
            if (!tCount.containsKey(t.charAt(i))){
                tCount.put(t.charAt(i), 1);
            }
            tCount.put(t.charAt(i), tCount.get(t.charAt(i))+1);
        }
        for (char c : sCount.keySet()) {
            if (sCount.get(c) != tCount.get(c)){
                result = false;
            }
            if(!result) {
                break;
            }
        }
        return result;
    }
}
