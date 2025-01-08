#include<iostream>
#include<string>

using namespace std;
typedef struct Var{
    void* val;
    string type;
}Var;

int main(){
    Var a;
    string type;
    string data;
    cin >> type >> data;
    if (type == "float"){
        a.val = (void*) new float(stof(data));
        a.type = type;
    }
    else{
        a.val = (void*) new int(stoi(data));
        a.type = type;
    }
    if (a.type == "float"){
        cout << *reinterpret_cast<float*>(a.val);
    }
    else{
        cout << *reinterpret_cast<int*>(a.val);
    }
}