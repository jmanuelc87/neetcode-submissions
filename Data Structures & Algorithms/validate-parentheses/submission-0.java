class Solution {
    public boolean isValid(String s) {
        if (s.length() == 1)
        {
            return false;
        }

        var par = new Stack();

        for (int i = 0; i < s.length(); i++)
        {
            var c = s.charAt(i);

            if (c == '(' || c == '{' || c == '[')
            {
                par.add(c);
            }
            else if (!par.isEmpty() && (c == ')' || c == '}' || c == ']'))
            {
                par.pop();
            }
        }

        return par.size() == 0;
    }
}
