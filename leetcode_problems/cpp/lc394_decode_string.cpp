#include <string>
#include <iostream>
#include <vector>
using std::string, std::vector;

class Solution
{
public:
    string parse(string &decoded, int &index)
    {
        string repeats = "";
        while (decoded[index] != '[')
        {
            repeats += decoded[index];
            index++;
        }
        index++;

        string symbols = "";
        while (decoded[index] != ']')
        {
            if (isdigit(decoded[index]))
            {
                symbols += parse(decoded, index);
            }
            else
            {
                symbols += decoded[index];
                index++;
            }
        }
        index++;

        string substr = "";
        for (int i = 0; i < std::stoi(repeats); i++)
        {
            substr += symbols;
        }

        return substr;
    }

    string run(string &decoded)
    {
        string encoded = "";

        int index = 0;
        bool search = false;
        while (index < decoded.length())
        {
            if (isdigit(decoded[index]))
            {
                encoded += parse(decoded, index);
            }
            else
            {
                encoded += decoded[index];
                index++;
            }
        }

        return encoded;
    }
};

int main()
{
    string str = "ab2[c3[d]]4[xz]";
    // string str = "abcd";

    Solution sol;
    string answer = sol.run(str);

    std::cout << answer << std::endl;
}