//https://www.interviewbit.com/problems/generate-all-parentheses/
int Solution::isValid(string A) {
    int n = A.length();
    stack<char> st;
    for (int i=0;i<n;i++){
        if(A[i]==')' || A[i]=='}' || A[i]==']'){
            if(st.empty()) return 0;
            if(A[i]==')' && st.top() != '(') return 0;
            if(A[i]=='}' && st.top() != '{') return 0;
            if(A[i]==']' && st.top() != '[') return 0;
            st.pop();
        }
        else{
            st.push(A[i]);
        }
    }
    if(st.empty()) return 1;
    return 0;
}
