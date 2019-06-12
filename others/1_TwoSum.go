func twoSum(nums []int, target int) []int {
    numMap := map[int]int{}
    for i := 0; i < len(nums); i++ {
        complement := target - nums[i]
        index, exists := numMap[complement]
        if exists {
            out := make([]int, 2)
            if i < index {
                out[0] = i
                out[1] = index
            } else {
                out[0] = index
                out[1] = i
            }
            return out
        }
        numMap[nums[i]] = i
    }
    return []int{0, 0}
}
