//
// Created by rober on 3/1/2019.
//

#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;


class Node{
private:
    int data;
    Node* prev;
    Node* next;
public:
    int getData(){
        return data;
    }

    void setNext(Node* newNext){
        next = newNext;
    }
    void setPrev(Node* newPrev){
        prev = newPrev;
    }
    Node* getNext(){
        return next;
    }
    Node* getPrev(){
        return prev;
    }

    Node(int data){
        this->data = data;
        prev = nullptr;
        next = nullptr;
    }
    Node(int data, Node* object){
        this->data = data;
        prev = object;
        next = nullptr;
    }

    bool append(int data){
        if(next) {
            return next->append(data);
        }else{
            next = new Node(data, this);

        }
    }

    void printList() {
        cout << data;
        if (next) {
            cout << "--->";
            next->printList();
        }
        cout << endl;
    }

    bool find(int data){
        if(data == this->data){
            return true;
        }else{
            if(next){
                return next->find(data);
            }else{
                return false;
            }
        }
    }

    bool dele(int data){
        if(data == this->data){
            prev->setNext(next);
            if(next) {
                next->setPrev(prev);
            }
            return true;
        }else{
            if(next){
                return next->dele(data);
            }else{
                return false;
            }
        }
    }
};


class DLL{
private:
    Node* head;
public:

    Node* getHead(){
        return head;
    }

    DLL(){
        head = nullptr;
    }
    bool push(int data) {
        if (head) {
            Node *temp = new Node(data);
            temp->setNext(head);
            head->setPrev(temp);
            head = temp;
        } else {
            head = new Node(data);
        }
    }
    bool append(int data){
        if(head){
            return head->append(data);
        }else{
            head = new Node(data);
        }
    }

    void printList(){
        if(head) {
            head->printList();
        }else{
            cout << "List is emty";
        }
    }


    bool find(int data){
        if(head){
            return head->find(data);
        }else{
            return false;
        }

    }

    bool dele(int data){
        if(head->getData() == data){
            head = head->getNext();
            return true;
        }
        if(head){
            return head->dele(data);
        }else{
            return false;
        }
    }
};


int main()
{
    DLL* dll = new DLL();
    dll->push(10);
    dll->append(4);
    dll->append(2);
    dll->push(5);
    dll->printList();
    cout << dll->dele(5) << endl;
    dll->printList();

    /*
    dll->push(3);
    dll->append(6);
    dll->append(20);
    dll->append(24);
    dll->append(22);

    dll->printList();
    dll->append(55);
    dll->push(55);
    cout << "Find" << endl;
    cout << dll->find(3) << endl;
    cout << dll->find(222) << endl;

    cout << dll->dele(3) << endl;
    cout << dll->dele(222) << endl;
    dll->printList();
     */




}

