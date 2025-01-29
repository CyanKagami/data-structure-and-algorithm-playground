#include <iostream>
#include <vector>

class MinHeap{
  public:
    std::vector<int> data;

    void push(int val){
      this->data.push_back(val);
      this->Re_Heap_Up();
    }

    int pop(){
      int temp = this->data[0];
      this->data[0] = this->data[this->data.size()-1];
      this->data.pop_back();
      this->reHeapDown();
      return temp;
    }

    void traverse(){
      std::cout << "MinHeap: ";
      std::vector<int> temp;
      while (!this->is_empty()) {
        int num = this->pop();
        std::cout << num;
        if (!this->is_empty()){
          std::cout << " -> ";
        }
        temp.push_back(num);
      }
      this->data = temp;
      std::cout << '\n';
    }

    bool is_empty(){
      return this->data.empty();
    }

  private:
    void swap(int i1,int i2){
      int temp = this->data[i1];
      this->data[i1] = data[i2];
      this->data[i2] = temp;
    }

    void Re_Heap_Up(){
      int i = this->data.size()-1;
      while (this->data[i]<this->data[(i-1)/2]){
        this->swap(i,(i-1)/2);
        i = (i-1)/2;
      }
    }

    void reHeapDown(){
      int i = 0;
      while (((2*i)+1)<this->data.size()  && this->data[i]>this->data[(2*i)+1] || ((2*i)+2<this->data.size()) && this->data[i] > this->data[(2*i)+2]){
        if (this->data[i]>this->data[(2*i)+1] && this->data[i] > this->data[(2*i)+2]){
          if (this->data[(2*i)+1]<this->data[(2*i)+2]){
            this->swap(i,(2*i)+1);
            i = (2*i)+1;
          }
          else{
            this->swap(i,(2*i)+2);
            i = (2*i)+2;
          }
        }
        else if (this->data[i]>this->data[(2*i)+1]){
          this->swap(i,(2*i)+1);
          i = (2*i)+1;
        }
        else{
          this->swap(i,(2*i)+2);
          i = (2*i)+2;
        }
      }
    }
};
int main (int argc, char *argv[]) {
  MinHeap m = MinHeap();
  for(int i = 10;i>=0;i--){
    m.push(i);
    m.traverse();
  }
  return 0;
}
