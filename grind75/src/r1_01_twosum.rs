use std::collections::HashMap;

// def twoSum(self, nums: List[int], target: int) -> List[int]:
//     hm = {}
//     for index, num in enumerate(nums):
//         if target - num[index] in hm:
//             return [index, hm[target-num[index]]]
//         else:
//             hm[target-numb[index]] = index
//     return []

// write a function for twoSum that takes in an array of integers and a target integer
// return an array of the indices of the two numbers that add up to the target
// you may assume that each input would have exactly one solution, and you may not use the same element twice
// you can return the answer in any order
fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut hm = HashMap::new();
    for (index, num) in nums.iter().enumerate() {
        if hm.contains_key(&(target - num)) {
            return vec![index as i32, hm[&(target - num)] as i32];
        } else {
            hm.insert(num, index);
        }
    }
    vec![]
}

// write tests for twoSum
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_sum() {
        assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![1, 0]);
        assert_eq!(two_sum(vec![3, 2, 4], 6), vec![2, 1]);
        assert_eq!(two_sum(vec![3, 3], 6), vec![1, 0]);
    }
}