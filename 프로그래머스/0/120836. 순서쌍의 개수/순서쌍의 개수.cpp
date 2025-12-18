#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int count = 0;
    for (int i=1; i<int(sqrt(n)+1); i++){
        if (n%i == 0){
            if (i*i==n){
                count++;
            } else {
                count += 2;
            }
        }
    }
    return count;
}