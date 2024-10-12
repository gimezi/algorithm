const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

// 햄최몇
const N = parseInt(input[0])
const hamburgers = input[1].split(' ').map(Number)
// 햄버거 값의 합
let maxH = 0
hamburgers.forEach((ha) => {
    maxH += ha
})

// maxH * maxH 크기의 2차원 dp
// dp[x][y] = 선배1이 x, 선배2가 y가 가능한지?
const dp = Array(maxH + 1).fill().map(() => Array(maxH + 1).fill(false))
dp[0][0] = true

hamburgers.forEach((ham) => {
    for (let x = maxH; x >= 0; x--) {
        for (let y = maxH; y >= 0; y--) {
            if (x - ham >= 0) {
                dp[x][y] = (dp[x][y] || dp[x - ham][y])
            }
            if (y - ham >= 0) {
                dp[x][y] = (dp[x][y] || dp[x][y - ham])
            }
        }
    }
})

let answer = 0 

for (let i = 0; i <= maxH; i++){
    for (let j = 0; j <= i; j++) {
        let maknae = maxH - i - j
        if (dp[i][j] && (j >= maknae)) {
            answer = Math.max(answer, maknae)
        }
    }
}

console.log(answer)