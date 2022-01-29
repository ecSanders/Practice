#include <iostream>
#include <vector>

std::vector<int> selectionSort(std::vector<int> &vec){
    short value = -1;
    short other_value = -1;
    for(auto curr_it = vec.begin(); curr_it != vec.end(); ++curr_it){
        for(auto t_it = curr_it; t_it != vec.end(); ++t_it){
            if(*curr_it > *t_it){
                value = *t_it;
                other_value = *curr_it;
            }
        }
        *t_it = other_value;
        *curr_it = value;
    }
    return vec;
}


int main(){
    std::vector<int> v = {10,9,8,7,6,5,4,3,2,1};


    std::vector<int> yeet = selectionSort(v);

    for(auto it = yeet.cbegin(); it != yeet.cend(); ++it){
        std::cout << *it << " ";
    }

    return 0;
}
