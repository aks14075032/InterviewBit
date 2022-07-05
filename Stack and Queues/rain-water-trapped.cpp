//https://www.interviewbit.com/problems/rain-water-trapped/
int Solution::trap(const vector<int> &A) {
    stack<int> st;
    int ans = 0;
    for(int i=0;i<A.size();i++){
        while((!st.empty()) && A[i] > A[st.top()]){
            int height = A[st.top()];
            st.pop();
            
            if(st.empty()) break;
            
            int distance = i-st.top()-1;
            int min_height = min(A[st.top()], A[i])-height;
            
            ans += (min_height*distance);
        }
        st.push(i);
    }
    return ans;
}
