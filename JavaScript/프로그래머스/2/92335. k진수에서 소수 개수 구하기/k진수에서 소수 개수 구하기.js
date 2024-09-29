// n진수로 바꿔주는 함수
function makeNotation(number, n) {
    let tempNum = number
    let result = ''
    
    while (tempNum > 0) {
        let rest = tempNum % n
        tempNum = Math.floor(tempNum / n)
        result = rest.toString() + result
    }
    
    return result
}

// 조건에 맞는 숫자 찾기
function find(target) {
    const result = new Array()
    let temp = ''
    
    for (let i = 0; i < target.length; i ++) {
        const num = target[i]
        if (num == '0') {
            if (temp != '') {
                result.push(parseInt(temp)) 
                temp = ''
            }
        } else {
            temp += num.toString()
        }
    }
    
    if (temp != '') {
        result.push(parseInt(temp))
    }
    
    return result
}


// 소수 판별 함수
function isPrime(num) {
    if (num < 2) return false;
    for (let i = 2; i * i <= num; i++) {
        if (num % i === 0) return false;
    }
    return true;
}

// 소수 개수 구하기
function countPrime(numbers) {
    if (numbers.length == 0) {return 0}
    
    const maxNum = Math.max(...numbers)

    // maxNum이 너무 크면 
    if (maxNum >= Math.pow(2, 32)) {
        let result = 0
        numbers.forEach((num) => {
            if (isPrime(num)) {
                result += 1
            }
        })
        
        return result
    }
    
    
    const primes = Array.from({length: maxNum + 1}, () => 1)
    primes[0] = 0
    primes[1] = 0
    
    let i = 2
    while (i <= maxNum) {
        let j = 2
        while (i * j <= maxNum) {
            primes[i * j] = 0
            j += 1
        }
        i += 1
    }
    
    let result = 0
    
    numbers.forEach((num) => {
        if (primes[num] == 1) {
            result += 1
        }
    })
    return result
}

function solution(n, k) {
    // k진수로 바꾸기
    const notation = makeNotation(n, k)
    // 조건에 맞는 숫자 뽑기
    const numbers = find(notation)
    // 소수의 개수 찾기
    return countPrime(numbers)
}