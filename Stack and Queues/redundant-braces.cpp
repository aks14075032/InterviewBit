//Problem -- https://www.interviewbit.com/problems/redundant-braces/
int Solution::braces(string A) {
    int n = A.length();
    stack<char> st;
    
    for(int i=0;i<n;i++){
        if (A[i]=='+' || A[i]=='-' || A[i]=='/' || A[i]=='*' || A[i] == '('){
            st.push(A[i]);
        }
        else if(A[i] == ')'){
            if(st.top() == '('){
                return 1;
            }
            else{
                st.pop();
                while(!st.empty()){
                    if(st.top() == '('){
                        st.pop();
                        break;
                    }
                    st.pop();
                }
            }
        }
    }
    while(!st.empty()){
        if(st.top() == '('){
            return 1;
        }
        st.pop();
    }
    if(st.empty()){
        return 0;
    }
    return 1;
}
