// WAP to implement DDA algorithm
#include<iostream>
#include<math.h>
using namespace std;

int main()
{
    float x1,y1,x2,y2,dx,dy,m,xi,yi,xk,yk;
    int steps,i;
    cout<<"Enter starting co-ordinates x1 and y1:";
    cin>>x1>>y1;
    cout<<"Enter ending co-ordinates x2 and y2:";
    cin>>x2>>y2;
    xk = x1;
    yk = y1;
    dx = x2 - x1;
    dy = y2 - y1;
    m = dy/dx;
    if(m < 1)
        steps = fabs(dx);
    else if(m > 1)    
        steps = fabs(dy);
    else 
        steps = fabs(dy);
    xi = dx/float(steps);
    yi = dy/float(steps);
    for(i = 0;i < steps;i++)
    {
        cout<<"iteration:"<<i<<"\t"<<"xk:"<<xk<<"\t"<<"yk:"<<yk<<"\t"<<"(xk+1,yk+1):"<<"("<<roundf(xk)<<","<<roundf(yk)<<")"<<endl;
        xk = xk + xi;
        yk = yk + yi;
    }
    return 0;
}
