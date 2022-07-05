//https://www.interviewbit.com/problems/min-stack/
stack<int> st;
int minEle;
MinStack::MinStack() {
    st = stack<int>();
}

void MinStack::push(int x) {
    if(st.empty()){
        st.push(x);
        minEle = x;
    }
    else{
        if(x < minEle){
            st.push(2*x - minEle);
            minEle = x;
        }
        else{
            st.push(x);
        }
    }
}

void MinStack::pop() {
    if(st.empty()){
        return;
    }
    if(st.top() < minEle){
        minEle = 2*minEle - st.top();
    }
    st.pop();  
}

int MinStack::top() {
    if (st.empty()) return -1;
    int ans = st.top();
    return max(ans, minEle);
}

int MinStack::getMin() {
    if (st.empty()) return -1;
    return minEle;
}

