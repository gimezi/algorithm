const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const T = parseInt(input[0])
// 1로만 이루어진건 무조건 있으니까 기본을 1로
const dp = Array.from({length: 100001}, () => 1)

// 2 더해주고
for (let i = 2; i < 10001; i++) {
    dp[i] += dp[i - 2]
}

// 3 더해주자
for (let i = 3; i< 10001; i++) {
    dp[i] += dp[i - 3]
}

for (let i = 0; i < T; i++) {
    const n = parseInt(input[i + 1])
    console.log(dp[n])
}