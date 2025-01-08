#include<iostream>
#include<unordered_map>
#include<string>

using namespace std;
typedef struct Wallet
{
    int balance = 0;
    unordered_map<string,void*> method;
}Wallet;

void add(Wallet *self,int m){
    self->balance+=m;
}

int withdraw(Wallet *self,int m){
    self->balance-=m;
    return m;
}


int main(){
    struct Wallet w;
    void (*addFunction)(Wallet*,int) = &add;
    int (*withdrawFunction)(Wallet*,int) = &withdraw;
    w.method.insert({"add",reinterpret_cast<void*&>(addFunction)});
    w.method.insert({"withdraw",reinterpret_cast<void*&>(withdrawFunction)});
    // w.method["withdraw"] = withdraw;
    reinterpret_cast<void(*)(Wallet*,int)>(w.method["add"])(&w,500);
    cout << w.balance << "\n";
    reinterpret_cast<int(*)(Wallet*,int)>(w.method["withdraw"])(&w,300);
    cout << w.balance;
}