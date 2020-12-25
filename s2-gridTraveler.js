/**
 * Say that you are a traveler on a 2D grid. You begin in the top-left corner
 * and your goal is to travel to the bottom-right corner. You may only move down or right.
 *
 * In how many ways can you travel to the goal on a grid with dimension m * n?
 */
// write a function gridTraveler(m, n) that calculates this.

//Brute force with exponential time complexity O(2^n+m) time and O(n + m) space
/*
const gridTraveler = (m, n) => {
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0) return 0;
                        //down                  //right
  return gridTraveler(m - 1, n) + gridTraveler(m, n - 1);
};

console.log(gridTraveler(1, 1)); //1
console.log(gridTraveler(2, 3)); //3
console.log(gridTraveler(3, 2)); //3
console.log(gridTraveler(3, 3)); // 6
// grid is too big to calculate with brute force method
console.log(gridTraveler(18, 18)); //?
*/

// USING MEMOIZATION Linear time complexity O(n * m) time and O(n + m) space
const gridTraveler = (m, n, memo = {}) => {
  const key = m + ',' + n;
  if (key in memo) return memo[key];
  // are the args in the memo
  if (m === 1 && n === 1) return 1;
  if (m === 0 || n === 0) return 0;
  /*                            //down                      //right  */
  memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo);
  return memo[key];
};

console.log(gridTraveler(1, 1)); //1
console.log(gridTraveler(2, 3)); //3
console.log(gridTraveler(3, 2)); //3
console.log(gridTraveler(3, 3)); // 6
console.log(gridTraveler(18, 18)); //2333606220
