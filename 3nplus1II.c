#include <bits/stdc++.h>
using namespace std;

long long result;
int n;
int main (){
	cin >> result >> n;

	while(n > 1)
	{
	  if (result % 2 == 0)
		result /= 2;
	  else if (result <= 1)
		result = -1;
	  else
		result = result * 3 + 1;
	  n--;
	}

	cout << result;
}
