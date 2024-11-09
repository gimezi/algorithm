const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

// 회의실 배정
const N = parseInt(input[0])
const meetings = new Array()
for (let i = 0; i < N; i++) {
    meetings.push(input[i + 1].split(' ').map(Number))
}

// 종료시간 기준으로 정렬
meetings.sort((a, b) => {
    if (a[1] == b[1]) return a[0] - b[0]
    return a[1] - b[1]
})

let cnt = 0
let lastEnd = 0

for (let i = 0; i < N; i ++) {
    if (meetings[i][0] >= lastEnd) {
        cnt ++
        lastEnd = meetings[i][1]
    }
}

console.log(cnt)