#include <stdlib.h>
#include <string>
#include <iostream>
#include <stack> 
#include <map>

using namespace std;
map<char,char> dict ={
    {'}','{'},
    {')','('},
    {']','['}
};

bool is_correct(string s){
    stack<char> pile;
    for(int k=0;k<s.size();k++){
        if(s[k]=='}'||s[k]==')'||s[k]==']'){
           char c=pile.top();
           pile.pop();
            if(pile.empty()||dict[s[k]]!=c)
                return false;
        }
        else 
            pile.push(s[k]);
    }
    return true;
}


int main(){
    string s="{()}";
    cout << is_correct(s);
    return 0;
}

 