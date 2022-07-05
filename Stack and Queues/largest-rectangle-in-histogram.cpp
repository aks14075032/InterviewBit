//https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
int Solution::largestRectangleArea(vector<int> &A) {
    int n = A.size();
    stack<int> st;
    int tp, area_with_top;
    int max_area = INT_MIN;
    int i=0;
    while(i<n) {
        if(st.empty() || A[st.top()] <= A[i]){
            st.push(i++);
        }
        else{
            tp = st.top();
            st.pop();
            area_with_top = A[tp]* (st.empty() ? i: (i-st.top()-1));
            max_area = max(max_area, area_with_top);
        }
    }
    
    while(!st.empty()){
        tp = st.top();
        st.pop();
        area_with_top = A[tp]* (st.empty() ? i: (i-st.top()-1));
        max_area = max(max_area, area_with_top);
    }
    return max_area;
}
