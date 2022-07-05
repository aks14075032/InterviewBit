//https://www.interviewbit.com/problems/sliding-window-maximum/
vector<int> Solution::slidingMaximum(const vector<int> &A, int B) {
    multiset<int, greater<int>> mst;
    vector<int> ans;
    int n = A.size();
    if(B > n){
        return ans;
    }
    int j=0;
    for(int i=0;i<n; i++){
        mst.insert(A[i]);
        if(i >= B-1){
            auto itr = mst.begin();
            ans.push_back(*itr);
            mst.erase(mst.find(A[j]));
            j += 1;
        }
    }   
    return ans;    
}
