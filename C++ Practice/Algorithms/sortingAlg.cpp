#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

// hello
int main(){

    // Create vector
    vector <int> vect = {1,2,3,4,5};

    // Output vect size
    cout << vect.size() << endl;

    // Iterating using a for loop
    for(int i = 0; i < 5; i++){
        cout << vect[i] << endl;
    }
    
    // Note: iterator is a class
    vector <int>::iterator ptr;

    // Using an iterator
    // .begin() and .end() point to the address
    for(ptr = vect.begin(); ptr < vect.end(); ptr++){
        cout << *ptr << endl;
    }

    
    return 0;
}