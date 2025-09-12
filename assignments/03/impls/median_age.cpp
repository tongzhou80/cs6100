#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

double median(std::vector<int>& ages) {
    std::sort(ages.begin(), ages.end());
    size_t n = ages.size();
    if (n % 2 == 0)
        return (ages[n/2 - 1] + ages[n/2]) / 2.0;
    else
        return ages[n/2];
}

int main(int argc, char* argv[]) {
    std::ifstream file(argv[1]);
    std::string line;
    std::vector<int> ages;

    std::getline(file, line); // skip header
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string item;
        int col = 0;
        while (std::getline(ss, item, ',')) {
            if (col == 2) {
                ages.push_back(std::stoi(item));
                break;
            }
            col++;
        }
    }

    std::cout << median(ages) << std::endl;
    return 0;
}
