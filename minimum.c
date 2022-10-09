#include "minimum.h"
using namespace std;

int findMin(int N, int A[]) {
	int min = A[0];
	int i = 1;
  	while (i < N)
	{
    	if (A[i] < min)
      		min = A[i];
    	i++;
	}
  	return min;
}
