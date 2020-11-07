class Solution {
    public int romanToInt(String s) {
        int ret = 0;
        for(int i = s.length() - 1; i >= 0; --i){
            char c = s.charAt(i);
            switch(c){
                case 'I':
                    ret += ((ret >= 5) ? -1 : 1);
                    break;
                case 'V':
                    ret += 5;
                    break;
                case 'X':
                    ret += ((ret >= 50) ? -10 : 10);
                    break;
                case 'L':
                    ret += 50;
                    break;
                case 'C':
                    ret += ((ret >= 500) ? -100 : 100);
                    break;
                case 'D':
                    ret += 500;
                    break;
                case 'M':
                    ret += 1000;
                    break;
            }
        }
        return ret;
    }
}