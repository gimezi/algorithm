const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')


// 거짓말
const [N, M] = input[0].split(' ')
const blackListStr = input[1].split(' ')
const blackList = blackListStr.map((num) => parseInt(num))
const numberOfBlackList = blackList.shift()
const parties = new Array()
for (let i = 0; i < parseInt(M); i ++) {
    const party = input[2 + i].split(' ').map((num) => parseInt(num))
    party.shift()
    parties.push(party)
}

// 새롭게 업데이트할 블랙리스트
const updatedBlackList = [...blackList]

// n번 사람에 대해서 블랙리스트를 업데이트해주는 함수
function check(n) {
    parties.forEach((party) => {
        // n번 사람이 들어있는 파티일 경우
        if (party.includes(n)) {
            party.forEach((person) => {
                if (!updatedBlackList.includes(person)) {
                    // 같은 파티에 있는 사람들 추가해주고
                    updatedBlackList.push(person)
                    // 새롭게 업데이트 된 사람도 확인해보자
                    check(person)
                }
            })
        }
    })
}

for (let num = 0; num < numberOfBlackList; num++) {
    check(blackList[num])
}

// console.log('블랙리스트:', updatedBlackList)

let ans = 0

parties.forEach((party) => {
    let flag = true
    party.forEach((per) => {
        if (updatedBlackList.includes(per)) {flag = false}
    })

    if (flag) {ans += 1}
})


console.log(ans)