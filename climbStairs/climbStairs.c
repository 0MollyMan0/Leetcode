int climbStairs(int n) {
    int n1;
    int n2;
    int tmp;

    n1 = 1;
    n2 = 2;
    if (n == 1)
        return 1;
    while(n-- > 2)
    {
        tmp = n2;
        n2 += n1;
        n1 = tmp;
    }
    return (n2);
}