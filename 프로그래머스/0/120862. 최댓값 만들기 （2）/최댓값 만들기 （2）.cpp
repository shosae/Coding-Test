#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> numbers) {
    sort(numbers.begin(), numbers.end());
    
    int n = numbers.size();
    int a = numbers[n-1] * numbers[n-2];
    int b = numbers[0] * numbers[1];
    
    return max(a, b);
}