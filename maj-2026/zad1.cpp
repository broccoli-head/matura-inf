#include <iostream>
#include <cmath>

static int callCount = 0;

int func_A(unsigned long long arg_m, unsigned long long arg_n) {
	callCount++;
	if (arg_n == 1) {
		std::cout << callCount << std::endl;
		callCount = 0;
		return arg_m;
	}
	else if (arg_n > 1 && arg_n % 2 == 0) {
		std::cout << "Wywolanie " << callCount << " : A(" << 2 * arg_m << ", " << arg_n / 2 << ")\n"; 
		return func_A(2 * arg_m, arg_n / 2);
	}
	else {
		std::cout << "Wywolanie " << callCount << ": A(" << arg_m << ", " << (arg_n - 1) / 2 << ")\n"; 
		return 2 * func_A(arg_m, (arg_n - 1) / 2) + arg_m;
	}
}

int main() {
	func_A(1, 8);
	func_A(1, 16);
	func_A(1, 32);
	std::cout << "======" << std::endl;
	func_A(1, 15);
	func_A(1, 31);
	return 0;
}
