// 0을 제거하고 남은 1의 갯수와 제거된 0의 갯수를 반환를 반환해주는 함수
function reduceZero(string) {
    const arr = string.split('')
    let cnt0 = 0
    let cnt1 = 0
    arr.forEach((num) => {
        if (num === '1') {
            cnt1 += 1
        } else {
            cnt0 += 1
        }
    })
    return {cnt0, cnt1}
}

// 숫자받아서 이진수로 변환해주는 함수
function change(number) {
    let arr = []
    while (number > 0) {
        arr.push(number % 2)
        number = Math.floor(number / 2)
    }
    arr.reverse()
    
    return arr.join('')
}

function solution(s) {
    // 이진변환 횟수
    let cnt = 0
    // 제거된 총 0의 갯수
    let zeros = 0
    
    while (s !== '1') {
        cnt += 1
        // 제거된 0개수, 남은 1개수
        const {cnt0, cnt1} = reduceZero(s)
        zeros += cnt0
        s = change(cnt1)
    }
    
    return [cnt, zeros]
}