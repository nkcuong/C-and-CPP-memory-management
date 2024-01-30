#include <iostream>

float divide(float a, float b) {
	return a / b;
}

int main() {
	float x, y, z;
	x = 5;
	y = 2;
	z = divide(x, y);
	std::cout << z << std::endl;
   
}