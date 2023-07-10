from pyamaze import maze,agent
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1-x2) + abs(y1-y2)

def astar(m):
    start = (m.rows, m.cols)
    g_score = {cell : float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, (1, 1))

    open = PriorityQueue()
    open.put((h(start, (1,1)), h(start,(1,1)), start))  # fscore, hscore & start
    apath = {}
    while not open.empty():
        curr_cell = open.get()[2]
        if curr_cell == (1,1):
            break
        for d in 'ESNW':
            if m.maze_map[curr_cell][d]==True:
                if d == 'E':
                    child_cell = (curr_cell[0], curr_cell[1]+1)
                if d == 'W':
                    child_cell = (curr_cell[0], curr_cell[1]-1)
                if d == 'N':
                    child_cell = (curr_cell[0]-1, curr_cell[1])
                if d == 'S':
                    child_cell = (curr_cell[0]+1, curr_cell[1])

                temp_g_score = g_score[curr_cell]+1
                temp_f_score = temp_g_score + h(child_cell, (1,1))

                if temp_f_score < f_score[child_cell]:
                    g_score[child_cell] = temp_g_score
                    f_score[child_cell] = temp_f_score
                    open.put((temp_f_score, h(child_cell,(1,1)), child_cell))
                    apath[child_cell] = curr_cell

    fwdpath = {}
    cell = (1, 1)
    while cell != start:
        fwdpath[apath[cell]] = cell
        cell = apath[cell]
    return  fwdpath


if __name__=='__main__':
    m=maze(30,30)
    m.CreateMaze()
    path=astar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})

    m.run()
