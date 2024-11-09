const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

// 감시 피하기
const N = parseInt(input[0])
const space = new Array()
const empties = new Array()
const teachers = new Array()
let flag = false

for (let i = 0; i < N; i++) {
    const line = input[i + 1].split(' ')
    line.forEach((kan, j) => {
        // 빈칸위치 기록
        if (kan == 'X') {
            empties.push([i, j])
        }
        if (kan == 'T') {
            teachers.push([i, j])
        }
    })
    space.push(input[i + 1].split(' '))
}

// 빈칸에 벽 놔둬보고 3개 되면
function pick(arr) {
    if (arr.length == 3) {
        // 함수 실행
        check(arr)
    } else {
        for (let i = 0; i < empties.length; i ++) {
            if (!arr.includes(empties[i])) {
                pick([...arr, empties[i]])
            }
        }
    }
}

// 깊은 복사 함수
function deepCopy(arr) {
    return arr.map(row => [...row]);
}

const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

// 장애물 위치가 세개 주어졌을 때, 다 가려지는지 확인
function check(obstacles) {
    const newMap = deepCopy(space)
    obstacles.forEach((obstacle) => {
        newMap[obstacle[0]][obstacle[1]] = 'O'
    })  

    let temp = true

    // 선생님마다 확인하면서 학생이 안바뀌는지 확인
    teachers.forEach((teacher) => {
        directions.forEach((dire) => {
            let k = 0
            while (true) {
                const [ny, nx] = [teacher[0] + k * dire[0], teacher[1] + k *dire[1]]
                if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                    if (newMap[ny][nx] == 'S') {
                        temp = false
                        break
                    }
                    if (newMap[ny][nx] == 'O') {
                        break
                    }
                    k += 1
                } else {
                    break
                }
            }
        })
    })

    if (temp) {
        flag = true
    }
    return
}

pick([])
console.log(flag ? 'YES' : 'NO')