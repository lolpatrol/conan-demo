#include <iostream>
#include <stringprovider.h>
#include "stringprinter.h"

void printString() {
    std::cout << provideString() << std::endl;
}

void printAnotherString() {
    std::cout << provideAnotherString() << std::endl;
}
