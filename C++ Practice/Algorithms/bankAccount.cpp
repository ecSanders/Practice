#include <iostream>
#include <string>

bool checkCredentials(std::string user, std::string pass){
    if(user == "my_user" && pass == "secret123"){
        return true;
    }
    else{
        return false;
    }
} 

int main(){
    std::string username;
    std::string password;
    bool verify = true;


    while (verify){
        std::cout << "Please enter your username: ";
        std::cin >> username;
        std::cout << "Please enter your password: ";
        std::cin >> password;

        if (checkCredentials(username, password) == true){
            verify = false;
            std::cout << "\nWelcome to Untagged bank\n\n";
        }
        else{
            std::cout << "Incorrect credentials, please try again\n\n";
        };
    }
    



    return 0;
}