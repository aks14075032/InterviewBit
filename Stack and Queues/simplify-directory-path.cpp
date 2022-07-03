// Problem -- https://www.interviewbit.com/problems/simplify-directory-path/
string Solution::simplifyPath(string A) {
    stack<string> st;
    
    int i=0, n = A.length();
    string dir;
    string res;
    res += '/';
    while(i < n){
        dir.clear();
        while(A[i] == '/'){
            i += 1;
        }
        
        while (i < n && A[i] != '/'){
            dir += A[i];
            i += 1;
        }
        //cout<<dir<<endl;
        if(dir.compare("..") == 0){
            if(!st.empty()){
                st.pop();
            }
        }
        else if(dir.compare(".") == 0){
            continue;
        }
        else if(dir.length() != 0){
            st.push(dir);
        }
        i += 1;
    }
    
    stack<string> st1;
    
    while(!st.empty()){
        st1.push(st.top());
        st.pop();
    }
    
    while(!st1.empty()){
        string temp = st1.top();
        if(st1.size() != 1){
            res.append(temp+'/');
        }
        else{
            res.append(temp);
        }
        st1.pop();
    }
    return res;
}
