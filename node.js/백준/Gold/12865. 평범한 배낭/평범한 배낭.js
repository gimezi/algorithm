const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

// 평범한 배낭
const [N, K] = input[0].split(' ').map(Number)
const stuff = new Array();
for (let i = 1; i <= N; i++) {
    stuff.push(input[i].split(' ').map(Number))
}

// 배낭문제 알고리즘
// dp[i][w] = i번째 물건까지 고려했을 떄, 배낭의 용량이 w일때 가질 수 있는 최대 가치
// 그럼 각 물건에 대해서 물건을 넣지않거나 / 넣거나
// 넣지 않았다면, dp[i][w] = dp[i - 1][w]
// 넣었다면, dp[i][w] = dp[i - 1][w - 지금물건무게] + 지금물건가치

const dp = Array(N + 1).fill().map(() => Array(K + 1).fill(0))
for (let n = 1; n <= N; n++) {
    const [weight, value] = stuff[n - 1] // 현재 물건의 무게, 가치
    for (let k = 0; k <= K; k++) {
        if (k < weight) {
            dp[n][k] = dp[n - 1][k] 
        } else {
            dp[n][k] = Math.max(dp[n - 1][k], dp[n - 1][k - weight] + value)
        }
    }
}
console.log(dp[N][K])