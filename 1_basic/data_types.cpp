#include <iostream>
#include <cmath>
#include <limits>
#include <iomanip>
using namespace std;

int main(){
    int age = 59;
    cout << "age is " << age << endl;
    cout << "size of int is " << sizeof(age) << endl;
    
    cout << "Max possible integer will be " << (int)(pow(2 , 31)) - 1 << endl;
    cout << "Max integer is " << INT32_MAX << endl;
    cout << "Number of decimal places in max int " << log10(INT32_MAX) << endl;

    float pi = 3.14152567899;
    double pi2 = 3.14152567899;
    cout << setprecision(10) << "float " << pi << endl;
    cout << setprecision(10) << "double " << pi2 << endl;

    bool flag = true;
    cout << flag << " size of bool is " << sizeof(flag) << endl;

    char ch = 'A';
    cout << ch << " size of char is " << sizeof(ch) << endl;
}