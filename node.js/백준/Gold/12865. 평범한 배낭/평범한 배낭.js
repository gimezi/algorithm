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
// 최대이익[K][W] = 최대 W까지 쓸 수 있는 배낭에서 물건을 K번째까지 봤을 때의 최대 이익
// 그럼 다음 물건을 담으면 어떻게 되나
// dp[k + 1][w] = dp[k][w], dp[k][w - 무게] + 가치

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