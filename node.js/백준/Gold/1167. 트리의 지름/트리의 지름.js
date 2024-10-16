const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n')

// 트리의 지름
const n = parseInt(input[0]);
const adj = Array(n + 1).fill().map(() => []); // 인접 리스트 사용

// 입력 데이터를 인접 리스트 형태로 저장
for (let i = 1; i <= n; i++) {
    const arr = input[i].split(' ').map(Number);
    const now = arr[0];
    for (let j = 1; j < arr.length - 1; j += 2) {
        const nextNode = arr[j];
        const dist = arr[j + 1];
        adj[now].push([nextNode, dist]);
    }
}

let maxDist = 0;
let farthestNode = 1;

// DFS 함수
function dfs(node, dist, visited) {
    visited[node] = true;

    // 거리가 최대일 때 갱신
    if (dist > maxDist) {
        maxDist = dist;
        farthestNode = node;
    }

    for (const [nextNode, nextDist] of adj[node]) {
        if (!visited[nextNode]) {
            dfs(nextNode, dist + nextDist, visited);
        }
    }
}

// 임의의 노드에서 가장 먼 노드를 찾는 DFS
let visited = Array(n + 1).fill(false);
dfs(1, 0, visited);

// 그 노드에서 다시 가장 먼 노드를 찾는 DFS
visited = Array(n + 1).fill(false);
maxDist = 0; // 초기화
dfs(farthestNode, 0, visited);

// 트리의 지름 출력
console.log(maxDist);
