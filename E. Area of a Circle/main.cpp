
#include <iostream>
#include<iomanip>

using namespace std;
int main()
{
    const double  PI = 3.141592653;
    double r;
    cin >> r;
    cout<< fixed << setprecision(9)<< PI*r*r << endl;
}
