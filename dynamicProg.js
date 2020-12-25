/*0-25m */
// O(2^n) time and O(n) space
// O(2^n) is a slow time complexity. It has an exponential time complexity

/*
const fib = (n) => {
  if (n <= 2) return 1;
  return fib(n - 1) + fib(n - 2);
};

//1 1 2 3 5 8 13
console.log(fib(1)); //1
console.log(fib(2)); //1
console.log(fib(3)); //2
console.log(fib(4)); //3
*/

// fib(50) //12586269025
// fib(50)   =   2^50 steps  =   1.12e+15  so this is an enormous amount of steps
//              12,586,269,025 steps

/*
// Both are O(2^n) time and O(n) space
const dib = (n) => {
  if (n <= 1) return;
  dib(n-1);
  dib(n-1);
}

const lib = (n) => {
  if (n <= 1) return;
  lib(n-2);
  lib(n-2);
}
*/

/*******  25m ********/
//memoization
//js object, key will be arg to fn, value will be the return value
//assign memo to be an empty object
// Now it is a linear time complexity O(n) time and O(n) space
const fib2 = (n, memo = {}) => {
  if (n in memo) return memo[n];
  if (n <= 2) return 1;
  memo[n] = fib2(n - 1, memo) + fib2(n - 2, memo);
  return memo[n];
};
console.log(fib2(6)); //8
console.log(fib2(7)); //13
console.log(fib2(8)); //21
console.log(fib2(50)); //12586269025
