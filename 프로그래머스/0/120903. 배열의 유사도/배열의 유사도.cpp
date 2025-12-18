#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    vector<string> intersection;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(intersection));
    return intersection.size();
}