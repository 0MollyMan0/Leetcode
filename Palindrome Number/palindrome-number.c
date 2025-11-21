int lenDigits(int x)
{
    int count = 1;
    while (x/10)
    {
        count++;
        x /= 10;
    }
    return (count);
}

bool isPalindrome(int x) {
    int i = 0;
    if (x < 0)
        return (false);
    int len = lenDigits(x);
    int *tab = malloc(sizeof(int) * len);
    while (x/10)
    {
        tab[i] = x % 10;
        x /= 10;
        i++;
    }
    tab[i] = x;
    int j = 0;
    while (j < len / 2)
    {
        if (tab[i] != tab[j])
            return (false);
        i--;
        j++;
    }
    return (true);
}