#include <iostream>
#include <ctime>
using namespace std;

int main() {
    time_t start_time;
    time_t end_time;

    cout << "Hello";

    start_time = time(NULL);
    for(long i = 0; i < 10; i++){

    }
    end_time = time(NULL);

    cout << end_time - start_time;

  return 0;
}