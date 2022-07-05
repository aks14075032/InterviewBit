//Problem -- https://www.interviewbit.com/problems/evaluate-expression/
int Solution::evalRPN(vector<string> &A) {
    stack<int> st;
    int ans=0;
    for (int i=0;i<A.size();i++){
        if(A[i] == "+" || A[i] == "-" || A[i] == "*" || A[i] == "/"){
            int b = st.top();
            st.pop();
            int a = st.top();
            st.pop();
            if(A[i] == "+"){
                ans = a+b;
            } 
            else if(A[i] == "-"){
                ans = a-b;
            }
            else if(A[i] == "*"){
                ans = a*b;
            }
            else{
                ans = int(a/b);
            }
            //cout<<a<<" "<<b<<" "<<A[i]<<" "<<ans<<endl;
            st.push(ans);
        }
        else{
            st.push(atoi(A[i].c_str()));
        }
    }
    return st.top();
}
