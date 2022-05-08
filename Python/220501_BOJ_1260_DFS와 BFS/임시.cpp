/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <string>
#include <stack>
#include <stdio.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);	cin.tie(0);	cout.tie(0);
    
    stack <char> s;
    
    string str;
    string bomb;
    
    cin>>str>>bomb;
    
    for(int i=str.length()-1;i>=0;i--){
        if(bomb[0]!=str[i]) s.push(str[i]);
        else{
            for(int i=1;i<bomb.length();i++){
                char c=s.top();
                if(c==bomb[i]) {
                    s.pop();
                }else{
                    for(int j=i-1;j>=0;j--){
                        s.push(bomb[j]);
                    }
                    break;
                }
            }
        }
    }
    
    if(s.empty()){
        printf("FRULA");
    }
    else{
    while(!s.empty()){
        char c = s.top();
        s.pop();
        printf("%c",c);
    }
    }
    
    
}
