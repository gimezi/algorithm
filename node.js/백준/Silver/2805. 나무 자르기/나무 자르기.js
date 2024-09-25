const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

function cut(trees, h) {
    let result = 0
    trees.forEach((tree) => {
        if (tree > h) {
            result += (tree - h)
        }
    })
    return result
}


const [_, M] = input[0].split(' ')
const trees = input[1].split(' ')

let top = 1000000001
let bottom = 0

function main(top, bottom, M, trees) {
    let result = 0
    while (top >= bottom) {
        const mid = Math.floor((top + bottom) / 2)
        const nowResult = cut(trees, mid)
        if (nowResult >= M) {
            result = mid
            bottom = mid + 1
        } else {
            top = mid - 1
        }
    }

    return result
}

console.log(main(top, bottom, M, trees))
