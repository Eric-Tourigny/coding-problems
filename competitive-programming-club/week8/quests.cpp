#include <set>
#include <iostream>
#include <string>
#include <utility>
#include <limits.h>

int main()
{
    int n;
    std::cin >> n;
    auto values = std::multiset<std::pair<long long, long long>>();

    for (int i = 0; i < n; i++)
    {
        std::string command;
        std::cin >> command;
        if (command == "add")
        {
            long long energy, gold;
            std::cin >> energy >> gold;
            values.emplace(energy, gold);
        }
        else
        {
            long long remaining_energy, total_gold, energy, gold;
            total_gold = 0;
            std::cin >> remaining_energy;
            while (1)
            {
                auto pair = std::pair(remaining_energy, INT_MAX);
                auto iter = values.lower_bound(pair);
                if (iter == values.begin())
                {
                    std::cout << total_gold << std::endl;
                    break;
                }
                iter--;
                auto [energy, gold] = *iter;
                values.erase(iter);
                remaining_energy -= energy;
                total_gold += gold;
            }
        }
    }
}