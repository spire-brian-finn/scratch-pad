#include <iostream>
#include "CLI11.hpp"

int main(int argc, char** argv) {
  CLI::App app;
  bool flag = false;
  app.add_flag("-a,--enable-flag", flag);
  CLI11_PARSE(app, argc, argv);
  std::cout << "flag is " << flag << std::endl;
}