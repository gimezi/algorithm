#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 101

typedef struct {
    int y, x, dire;
    char visited[MAX_N * MAX_N];
} State;

typedef struct {
    int dy, dx;
} Direction;

Direction dirs[3][3] = {
    {{0, 1}, {0, 0}, {1, 1}},
    {{0, 0}, {1, 0}, {1, 1}},
    {{0, 1}, {1, 0}, {1, 1}}
};

int N;
int MAP[MAX_N][MAX_N];

int is_valid(int y, int x) {
    return y >= 0 && y < N && x >= 0 && x < N;
}

int find(int sy, int sx, int n) {
    State queue[MAX_N * MAX_N];
    int front = 0, rear = 0;
    int cnt = 0;
    
    if (MAP[N-1][N-1] == 1) {
        return 0;
    }

    queue[rear++] = (State){sy, sx, n};
    strcpy(queue[rear - 1].visited, "(0, 1)");

    while (front < rear) {
        State current = queue[front++];
        int cy = current.y;
        int cx = current.x;
        int dire = current.dire;

        for (int i = 0; i < 3; i++) {
            int dy = dirs[dire][i].dy;
            int dx = dirs[dire][i].dx;
            int ny = cy + dy;
            int nx = cx + dx;

            if (is_valid(ny, nx) && MAP[ny][nx] == 0 && strchr(current.visited, '(') == NULL) {
                if (dy && dx) {
                    if (MAP[ny - 1][nx] == 0 && MAP[ny][nx - 1] == 0) {
                        if (ny == N - 1 && nx == N - 1) {
                            cnt++;
                        }
                        strcpy(queue[rear].visited, current.visited);
                        strcat(queue[rear++].visited, "(");
                        strcat(queue[rear - 1].visited, itoa(ny, NULL, 10));
                        strcat(queue[rear - 1].visited, ", ");
                        strcat(queue[rear - 1].visited, itoa(nx, NULL, 10));
                        strcat(queue[rear - 1].visited, ")");
                        queue[rear - 1].y = ny;
                        queue[rear - 1].x = nx;
                        queue[rear - 1].dire = 2;
                    }
                } else if (dy) {
                    if (ny == N - 1 && nx == N - 1) {
                        cnt++;
                    }
                    strcpy(queue[rear].visited, current.visited);
                    strcat(queue[rear++].visited, "(");
                    strcat(queue[rear - 1].visited, itoa(ny, NULL, 10));
                    strcat(queue[rear - 1].visited, ", ");
                    strcat(queue[rear - 1].visited, itoa(nx, NULL, 10));
                    strcat(queue[rear - 1].visited, ")");
                    queue[rear - 1].y = ny;
                    queue[rear - 1].x = nx;
                    queue[rear - 1].dire = 1;
                } else {
                    if (ny == N - 1 && nx == N - 1) {
                        cnt++;
                    }
                    strcpy(queue[rear].visited, current.visited);
                    strcat(queue[rear++].visited, "(");
                    strcat(queue[rear - 1].visited, itoa(ny, NULL, 10));
                    strcat(queue[rear - 1].visited, ", ");
                    strcat(queue[rear - 1].visited, itoa(nx, NULL, 10));
                    strcat(queue[rear - 1].visited, ")");
                    queue[rear - 1].y = ny;
                    queue[rear - 1].x = nx;
                    queue[rear - 1].dire = 0;
                }
            }
        }
    }
    return cnt;
}

int main() {
    scanf("%d", &N);
    int sy = 0, sx = 1;
    int result = find(sy, sx, 0);
    printf("%d\n", result);
    return 0;
}