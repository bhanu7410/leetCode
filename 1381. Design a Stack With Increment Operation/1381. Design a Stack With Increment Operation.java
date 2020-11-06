import java.util.*;

class CustomStack {
    private List<Integer> stk = new ArrayList<>();
    private int sz;
    public CustomStack(int maxSize) {
        sz = maxSize;
    }
    
    public void push(int x) {
        if (stk.size() < sz) {
            stk.add(x);
        }
    }
    
    public int pop() {
        return stk.isEmpty() ? -1 : stk.remove(stk.size() - 1);
    }
    
    public void increment(int k, int val) {
        for (int i = 0; i < k && i < stk.size(); ++i) {
            stk.set(i, stk.get(i) + val);            
        }
    }
}