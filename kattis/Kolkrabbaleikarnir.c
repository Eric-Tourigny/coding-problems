#include <stdio.h>
#include <math.h>

int main()
{
    int n, m;
    scanf("%u", &n);
    scanf("%u", &m);
    double total = 0;
    if (m > n)
    {
        total = m - n;
        m = n;
    }
    else
    {
        total = 0;
    }

    double survivors = 0;
    double log_comb_prop = -n;
    for (unsigned int r = 0; r < m; r++)
    {
        survivors += pow(2, log_comb_prop) * (m - r);
        log_comb_prop = log_comb_prop + log2(n - r) - log2(r + 1);
    }
    
    total += survivors;
    printf("%.10lf", total);
}