#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "interp.h"

// two point interpolators
double linear_interp(double y1, double y2, double mu) {
    return (y1*(1 - mu) + y2*mu);
}

double cosine_interp(double y1, double y2, double mu) {
    double mu2;

    mu2 = (1 - cos(mu*M_PI)) / 2;
    return (y1*(1-mu2) + y2*mu2);
}

// four point interpolators
double cubic_interp(double y0, double y1, double y2, double y3, double mu) {
    double a0, a1, a2, a3, mu2;

    mu2 = mu*mu;
    a0 = y3-y2 - y0+y1;
    a1 = y0-y1 - a0;
    a2 = y2-y0;
    a3 = y1;

    return (a0*mu*mu2 + a1*mu2 + a2*mu + a3);
}

double hermite_interp(double y0, double y1, double y2, double y3, double mu,
                      double tension, double bias) {
    double m0, m1, mu2, mu3;
    double a0, a1, a2, a3;

    mu2 = mu*mu;
    mu3 = mu2*mu;

    m0  = (y1-y0) * (1+bias) * (1-tension)/2;
    m0 += (y2-y1)*(1-bias)*(1-tension)/2;
    m1  = (y2-y1)*(1+bias)*(1-tension)/2;
    m1 += (y3-y2)*(1-bias)*(1-tension)/2;

    a0 =  2*mu3 - 3*mu2 + 1;
    a1 =    mu3 - 2*mu2 + mu;
    a2 =    mu3 -   mu2;
    a3 = -2*mu3 + 3*mu2;

    return(a0*y1+a1*m0+a2*m1+a3*y2);
}

int main(int argc, char* argv[]) {
    printf("interpolators are at %p %p %p %p\n", &linear_interp,
                                                 &cosine_interp,
                                                 &cubic_interp,
                                                 &hermite_interp);

    return 0;
}