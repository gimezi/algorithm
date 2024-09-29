const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

// 돌게임
const dol = parseInt(input[0])
if (dol % 2) {
    console.log('SK')
} else {
    console.log('CY')
}