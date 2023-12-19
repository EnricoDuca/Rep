#include <stdio.h>
#include <math.h>
//Calcolare la successione di Fibonacci fino a Fn e restituire Fn/Fn-1
double fib(int n){
    if(n<= 0)
        return -1;
    if(n == 1 || n==2)
        return 1;
    else{
        double x = (fib(n-2) + fib(n-1));
        double y = (fib(n-3) + fib(n-2));
        if (y == 0) {
            return -1;
        }

        double z = x/y;
        return z;
    }
}
