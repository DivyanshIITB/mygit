#include <bits/stdc++.h>
using namespace std;

// Creating a class
class GfG {
public:

    // Data member
    int val;
    
    // Member function
    void show() {
        cout << "Value: " << val << endl;
    }
    
};

int main() {
    
    // Create Object
    GfG obj;
    
    // Access data member and assign
    // it some value
    obj.val = 10;
    
    // Access member method
    obj.show();
    
    return 0;
}