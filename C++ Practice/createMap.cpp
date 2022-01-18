#include <iostream>
#include <string>
#include <map>
#include <cassert>

void displayMap(std::map<int, std::string>& m, int num){
    assert (num == NULL);
    for(auto it = m.begin(); it != m.end(); it++){
        std::cout << it->first << "\t" << it->second << "\n";
    }
}

int main(){
    auto num = 5;
    std::cout << num << std::endl;
    std::map<int, std::string>myMap = {{1, "Apple",},
                                {2, "Banana",},
                                {3, "Mango",},
                                {4, "Raspberry",},
                                {5, "Blackberry",},
                                {6, "Cocoa",}};

    displayMap(myMap,num);
    return 0;
}