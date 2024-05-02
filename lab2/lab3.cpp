// Program to implement  BLE algorithm
#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    float x1,y1,x2,y2,p0,xk,yk,pk,/*x_nxt,y_nxt,p_nxt,*/dy,dx,m;
    int i,steps;
    cout<<"Enter starting co-ordinates x1 and y1:";
    cin>>x1>>y1;
    cout<<"Enter ending co-ordonates x2 and y2:";
    cin>>x2>>y2;
    dx = x2 - x1;
    dy = y2 - y1;
    m = dy/dx;
   if(fabs(m) < 1)
   {
    steps = dx;
    p0 = 2*dy - dx;
    xk = x1;
    yk = y1;
    pk = p0;
    for(i = 0;i < steps;i++)
    {
        cout<<"Iteration:"<<i<<"\t"<<"Pk:"<<pk<<"\t"<<"("<<xk<<","<<yk<<")"<<endl;
        if(pk < 0)
        {
            
        }
    }
   }
}