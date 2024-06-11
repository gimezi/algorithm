const makeNumber = (n) => {
    let newNum = n;
    while (true) {
        if (Math.floor(n / 10) >= 1) {
            newNum += n % 10
            n = Math.floor(n/10)
        } else {
            newNum += n
            break
        }
    }
    return newNum
}

const dic = Array.from({length: 10001}, () => 0)
dic[0] = 1
for (i=1; i<=10001; i++) {
    const nextNum = makeNumber(i)
    if (nextNum <= 10000) {
        dic[nextNum] = 1
    }
}

dic.forEach((ele, idx) => {
    if (ele == 0) {
        console.log(idx)
    }
})