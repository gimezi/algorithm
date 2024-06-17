let fs = require('fs');
// 여러줄일때
// let input = fs.readFileSync('/dev/stdin').toString().split('\n')
// 한 줄일 때,
let input = fs.readFileSync('/dev/stdin').toString().split(' ')
const N = Number(input[0]);
const M = Number(input[1]);
console.log(N * M - 1)