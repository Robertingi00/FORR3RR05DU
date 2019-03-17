//
// Created by rober on 3/1/2019.
//
#include <iomanip>
#include <iostream>
#include <sstream>
#include <math.h>


using namespace std;

const int rad = 57.295779513;
const double pi = 3.14159265358979323846;

class Vigur{
private:
    double x;
    double y;
public:


    Vigur(double x, double y){
        this->x = x;
        this->y = y;
    };

    void prenta(){
        cout << "[" << x << "," << y <<"]" << endl;
    };

    float lengd(){
        return (sqrt(pow(x, 2) + pow(y, 2)));
    }

    void halli(){
        if(x != 0) {
            cout << "Halli: " << (y/x) << endl;
        }else{
            cout << "Þetta er bein lína" << endl;
        }
    }

    void thvervigur(){
        cout << "Þvervigur: [ " << -(y)<< ", " << x <<"]" << endl;
    }

    float stefnuhorn(){
        if(y >0){
            //Er fyrir ofan stefnuhorn verður alltaf +
            if(x < 0){
                return acos(y/lengd())*rad+90;
            }else{
                return acos(x/lengd())*(180/pi);
            }
        }else{
            if(x < 0){
                return -(acos(abs(y)/abs(lengd()))*rad)-90;
            }else{
                return -(acos(abs(x)/abs(lengd()))*rad);
            }
        }
    }

    void horn(Vigur* horn){
        cout << horn->x << horn->y << endl;
        float ofanSti =(x*horn->x)+(y * horn->y);
        float nedansti = this->lengd()*horn->lengd();
        cout << nedansti;

        cout << "Horn milli vigra: " << acos(ofanSti/nedansti)*rad << endl;
    }

    void summa(Vigur* horn){
        cout << "Summa: x: " << x + horn-> x << " y: " << y + horn->y << endl;
    }
};

int main(){


    Vigur* vigur1 = new Vigur(2, 4);
    Vigur* vigur2 = new Vigur(1, 0);
    string velmoguleikar[8]=  {"Prenta","Legnd","Halli","Þvervigur","Stefnuhorn","Horn","Summa","Hætta"};

    int val;
    string drasl;
    while(val != 8){
        for(int i = 1; i < 9;i++){
            cout << i << ". "<<velmoguleikar[i-1] << endl;
        }
        cout << "Hvað viltu gera: ";
        cin >> val;

        switch(val) {
            case 1:
                vigur1->prenta();
                break;
            case 2:
                cout << "Lengd: " << vigur1->lengd() << endl;
                break;
            case 3:
                vigur1->halli();
                break;
            case 4:
                vigur1->thvervigur();
                break;
            case 5:
                cout << "Stefnuhorn: " << vigur1->stefnuhorn()<< endl;
                break;
            case 6:
                vigur1->horn(vigur2);
                break;
            case 7:
                vigur1->summa(vigur2);
                break;
            case 8:
                cout << "takk fyrir að nota forritið" << endl;
                break;
        }

       cin >> drasl;
    }
    cout << "faasfa" << endl;
    cout << vigur1->stefnuhorn() << endl;
    return 0;

}