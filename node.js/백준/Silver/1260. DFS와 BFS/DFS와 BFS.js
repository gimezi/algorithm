const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

const [N, M, V] = input[0].split(' ')

// 인접행렬 만들기
const adj = Array.from({length: N}, () => Array.from({length: N}, () => 0))
for (let i = 1; i <= M; i++) {
    const [node1, node2] = input[i].split(' ')
    adj[node1 - 1][node2 - 1] = 1
    adj[node2 - 1][node1 - 1] = 1
}

// dfs는 스택을 사용
function dfs(start, adj) {
    const stack = new Array();
    const visited = new Array();
    visited.push(parseInt(start))
    let now = start
    while (true) {
        let flag = false
        for (let w = 0; w < N; w++) {
            if (adj[now - 1][w] == 1) {
                if (!visited.includes(parseInt(w + 1))) {
                    stack.push(now)
                    now = w + 1
                    visited.push(parseInt(now))
                    flag = true
                    break
                }
            }
        }

        if (!flag) {
            if (stack.length) {
                now = stack.pop()
            } else {
                break
            }
        } 
    }
    return visited.join(' ')
}

// bfs는 큐 사용
function bfs(start, adj) {
    const q = new Array();
    q.push(start)
    const visited = [parseInt(start)]

    while (q.length !== 0) {
        let now = q.shift();
        
        for (let i = 0; i < N; i++) {
            if (adj[now - 1][i] == 1) {
                if (!visited.includes(i + 1)) {
                    visited.push(i + 1)
                    q.push(i + 1)
                }
            }
        }
    }
    return visited.join(' ')
}

console.log(dfs(V, adj))
console.log(bfs(V, adj))