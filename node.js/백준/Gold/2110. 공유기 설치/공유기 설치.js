const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

const [N, C] = input[0].split(' ')
const houses = new Array
for (let i = 1; i <= N; i++) {
    houses.push(parseInt(input[i]))
}

// 집 위치 정렬
houses.sort((a, b) => a - b)

// 간격이 d일 때, 설치가 가능한지 알아보는 함수
function checkInterval(d, C, houses) {
    // 1번 위치는 설치하고 시작
    let installed = 1
    // 위치를 비교할 인덱스1, 인덱스2
    let idx1 = 0
    let idx2 = 1
    while (installed < C) {
        // 만약 idx가 범위를 넘는다면
        if (idx2 >= N || idx1 >= N) {
            return false
        }

        // 거리가 된다면,
        if (houses[idx2] - houses[idx1] >= d) {
            idx1 = idx2
            idx2 = idx1 + 1
            installed += 1
        } else {
            // 거리가 안된다면 idx2 += 1
            idx2 += 1
        }
    }

    return true
}

// 이분탐색
function findInterval(C, houses) {
    let left = 1
    let right = 1000000000
    let result = 0

    while (left <= right) {
        let mid = Math.floor((left + right) / 2)
        let check = checkInterval(mid, C, houses)

        // 현재 간격이 가능하면 간격을 더 늘려보고
        if (check) {
            result = mid
            left = mid + 1
        } else {
            // 불가능하면 간격을 더 줄여보자
            right = mid - 1
        }
    }
    return result
}

console.log(findInterval(C, houses))