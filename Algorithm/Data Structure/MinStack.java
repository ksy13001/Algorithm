class MinStack {

    private Stack<Integer> s;
    private int m;

    public MinStack() {
        this.s = new Stack<>();
        this.m = Integer.MAX_VALUE;
    }
    
    public void push(int val) {
        if(val <= this.m){
            this.s.push(this.m);
            this.m = val;
        }
        this.s.push(val);
    }
    
    public void pop() {
        if(this.s.pop() == this.m){
            this.m = this.s.pop();
        }
    }
    
    public int top() {
        return this.s.peek();
    }
    
    public int getMin() {
        return this.m;
    }
}

// 변수 하나에 최소값 저장
// 최소값 갱신하기 전, 기존 최소값을 먼저 push, 새로운 최소값이 pop 되어도 이전 최소값을 알수있도록
