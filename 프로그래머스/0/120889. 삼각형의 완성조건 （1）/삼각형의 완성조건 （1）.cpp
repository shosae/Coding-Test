#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    
    int total = accumulate(sides.begin(), sides.end(), 0);
    int max_val = *max_element(sides.begin(), sides.end());
    return (total > 2*max_val) ? 1 : 2;
}