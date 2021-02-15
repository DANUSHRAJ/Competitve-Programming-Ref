#include <iostream>
using namespace std;
#define NO_OF_CHARS 256
bool checkPalindrome(string str)
{
    int count[NO_OF_CHARS]={0};
    for(int i=0;str[i];i++)
        count[str[i]]++;
    int odd=0;
    for(int i=0;i<NO_OF_CHARS;i++)
    {
        if(count[i]&1)
            odd++;
        if(odd>1)
            return false;
    }
    return true;
}
int main(int argc, char** argv)
{
    string S;
    cin>>S;
    checkPalindrome(S)?cout<<"yes\n":cout<<"no\n";
}
