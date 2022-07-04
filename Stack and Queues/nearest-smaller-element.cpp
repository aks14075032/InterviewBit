//https://www.interviewbit.com/problems/nearest-smaller-element/
vector<int> Solution::prevSmaller(vector<int> &A) {
    vector<int> ans;
    int n = A.size();
    stack<int> st;
    for (int i = 0; i< n ; i++){
        while(!st.empty() && st.top() >= A[i]){
            st.pop();
        }
        if(st.empty()){
            ans.push_back(-1);
        }
        else{
            ans.push_back(st.top());
        }
        st.push(A[i]);
    }
    return ans;
}
