#include <bits/stdc++.h>
using namespace std;

long long a, b, c, i, n;
int main()
{
    cin >> n;
    i = 0;
    
    a = 0;
    b = 1;
    while (i <= n)
    {
        if (i == 0)
            cout << a;
        else if (i == 1)
            cout << b;
        else
        {
            c = (a + b) % 998244353;
            a = b;
            b = c;
            cout << c;
        }
        cout << "\n";
        i++;
    }
}
