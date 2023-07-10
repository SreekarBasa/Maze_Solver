from pyamaze import maze,agent,COLOR

def BFS(m):
    start = (m.rows, m.cols)
    frontier = [start]
    explored = [start]
    bfspath = {}
    while len(frontier)>0:
        curr_cell = frontier.pop(0)   # Using as queue
        if curr_cell == (1,1):
            break
        for d in 'ESNW':
            if m.maze_map[curr_cell][d] == True:
                if d == 'E':
                    child_cell = (curr_cell[0], curr_cell[1]+1)
                elif d == 'W':
                    child_cell = (curr_cell[0], curr_cell[1]-1)
                elif d == 'N':
                    child_cell = (curr_cell[0]-1, curr_cell[1])
                elif d == 'S':
                    child_cell = (curr_cell[0]+1, curr_cell[1])
                if child_cell in explored:
                    continue
                frontier.append(child_cell)
                explored.append(child_cell)
                bfspath[child_cell] = curr_cell
    fwdpath = {}
    cell = (1,1)
    while cell != start:
        fwdpath[bfspath[cell]] = cell
        cell = bfspath[cell]
    return fwdpath

if __name__=='__main__':
    m=maze(30,30)
    m.CreateMaze(loopPercent=30)
    path=BFS(m)
    a=agent(m,footprints=True)
    m.tracePath({a:path})


    m.run()