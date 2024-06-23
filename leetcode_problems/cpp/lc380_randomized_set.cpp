#include <vector>
#include <unordered_map>
#include <iostream>
#include <cstdlib>
using std::vector, std::unordered_map;

class RandomizedSet
{
private:
    vector<int> array;
    unordered_map<int, int> mapper;

public:
    bool insert(int value)
    {
        if (mapper.find(value) == mapper.end())
        {
            array.push_back(value);
            mapper[value] = array.size() - 1;
            return true;
        }
        else
        {
            return false;
        }
    }

    bool remove(int value)
    {
        if (mapper.find(value) == mapper.end())
        {
            return false;
        }
        else
        {
            int last = array.back();
            array[mapper[value]] = array.back();

            array.pop_back();
            mapper[last] = mapper[value];
            mapper.erase(value);
            return true;
        }
    }

    int getRandom()
    {
        return array[rand() % array.size()];
    }

    void print()
    {
        auto iter = mapper.begin();
        while (iter != mapper.end())
        {
            std::cout << iter->first << std::endl;
            iter++;
        }
    }
};

int main()
{
    RandomizedSet rs1;
    RandomizedSet rs2;

    rs1.insert(1);
    rs1.insert(2);

    rs2.insert(3);
    rs2.insert(4);

    rs1.print();
    rs2.print();

    return 0;
}