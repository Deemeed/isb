#include <iostream>
#include <fstream>
#include <random>
#include <bitset>
#include <string>

using namespace std;

/**
 * Generates a 128-bit pseudorandom binary sequence
 * @return String containing the binary sequence (128 '0' and '1' characters)
 */
string generate_128bit_sequence() {
    random_device rd;
    mt19937_64 generator(rd());

    uint64_t part1 = generator();
    uint64_t part2 = generator();

    string binary_str = bitset<64>(part1).to_string() + bitset<64>(part2).to_string();

    return binary_str;
}

/**
 * Saves string content to a file
 * @param content The string content to save
 * @param filename Target filename
 * @return true if successful, false on error
 */
bool save_to_file(const string& content, const string& filename) {
    ofstream outfile(filename);
    if (!outfile.is_open()) {
        return false;
    }
    outfile << content;
    outfile.close();

    return true;
}

int main() {
    const string filename = "cpp_sequence.txt";

    string sequence = generate_128bit_sequence();

    if (save_to_file(sequence, filename)) {
        cout << "Writed successfully" << endl;
    }
    else {
        cerr << "Error: Writing failed" << endl;
        return 1;
    }

    return 0;
}