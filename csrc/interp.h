#ifndef _INTERP_H#define _INTERP_H 1// two point interpolatorsdouble linear_interp(double y1, double y2, double mu);double cosine_interp(double y1, double y2, double mu);// four point interpolatorsdouble cubic_interp(double y0, double y1, double y2, double y3, double mu);double hermite_interp(double y0, double y1, double y2, double y3, double mu,                      double tension, double bias);#endif