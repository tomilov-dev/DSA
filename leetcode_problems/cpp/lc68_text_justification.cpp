#include <vector>
#include <string>
#include <iostream>
using std::vector, std::string;

class Solution
{
public:
    string right(vector<string> &words,
                 int maxWidth,
                 int index,
                 int &last_index,
                 int wc,
                 int curlen)
    {
        int residue = (maxWidth - curlen);
        int splen = residue / (wc - 1);
        vector<string> spaces(wc - 1, string(splen, ' '));
        residue = residue % (wc - 1);
        int sp_index = 0;
        while (residue)
        {
            spaces[sp_index++] += ' ';
            residue--;
        }

        string word = "";
        sp_index = 0;
        while (last_index < index)
        {
            word += words[last_index];
            if (last_index < index - 1)
            {
                word += ' ' + spaces[sp_index++];
            }
            last_index++;
        }
        return word;
    }

    string left(vector<string> &words,
                int maxWidth,
                int index,
                int &last_index,
                int curlen)
    {
        int residue = (maxWidth - curlen);

        string word = "";
        while (last_index < index)
        {
            word += words[last_index];
            if (last_index < index - 1)
            {
                word += ' ';
            }
            last_index++;
        }
        if (residue > 0)
        {
            word += string(residue, ' ');
        }
        return word;
    }

    vector<string> run(vector<string> &words, int maxWidth)
    {
        if (words.size() == 1)
        {
            return words;
        }

        vector<string> output;

        int last_index = 0;
        int index = 0;
        while (index < words.size())
        {
            int curlen = words[index++].length();
            while (index < words.size() && curlen <= maxWidth)
            {
                if (curlen + words[index].length() <= maxWidth - 1)
                {
                    curlen += words[index++].length() + 1;
                }
                else
                {
                    break;
                }
            }
            bool last_line = index == words.size();
            int wc = index - last_index;

            bool left_case = wc == 1 || last_line;
            string word;
            if (left_case)
            {
                word = left(words, maxWidth, index, last_index, curlen);
            }
            else
            {
                word = right(words, maxWidth, index, last_index, wc, curlen);
            }

            output.push_back(word);
        }

        return output;
    }
};

int main()
{
    vector<string> words = {"a"};
    int maxWidth = 1;

    Solution sol;
    vector<string> ws = sol.run(words, maxWidth);

    for (string w : ws)
    {
        std::cout << "'" << w << "'" << std::endl;
    }
}