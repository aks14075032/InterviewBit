// Problem -- https://www.interviewbit.com/problems/balanced-parantheses/
int Solution::solve(string A) {
    stack<char> st;
    
    int n = A.length();
    for (int i=0;i<n;i++){
        if(A[i] == ')' && st.empty()){
            return 0;
        }
        else if(A[i] == ')'){
            st.pop();
        }
        else{
            st.push(A[i]);
        }
    }
    if(st.empty()){
        return 1;
    }
    return 0;
}
