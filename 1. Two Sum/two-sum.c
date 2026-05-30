int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i = 0;
    int *result = malloc(sizeof(int) * 2);
    int j;

    while(i < numsSize)
    {
        j = 0;
        while(j < numsSize)
        {
            if(nums[i] + nums[j] == target && i != j)
            {
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
            j++;
        }
        i++;
    }
    *returnSize = 0;
    free(result);
    return (NULL);
}