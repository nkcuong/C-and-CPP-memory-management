#include <iostream>

int main() {
    // Allocate memory for 5 integers on the heap
    int* numbers = new int[5];

    // Assign values to the integers
    for (int i = 0; i < 5; ++i) {
        numbers[i] = i;
    }

    // Print the integers
    for (int i = 0; i < 5; ++i) {
        std::cout << numbers[i] << std::endl;
    }

    // Deallocate the memory
    delete[] numbers;

    return 0;
}