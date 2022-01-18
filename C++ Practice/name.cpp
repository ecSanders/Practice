#include <iostream>
#include <vector>
#include <iterator>

int largestProduct(std::vector<int> &n){
    std::vector<int>::iterator it;
    int num1 = 0;
    int num2 = 0;
    
    for (it = n.begin(); it < n.end(); it++){
        if(*it > num1){
            num1 = *it;
        }
    }
    std::cout << num1 << std::endl;
    return 0;
}


int main(){
    std::vector<int> n;

    largestProduct(n);

    return 0;
}
