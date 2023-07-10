from  pyamaze import maze, agent, COLOR

def DFS(m):
    global child_cell
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        curr_cell = frontier.pop()
        if curr_cell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[curr_cell][d]==True:
                if d=='E':
                    child_cell=(curr_cell[0], curr_cell[1]+1)
                elif d=='W':
                    child_cell=(curr_cell[0], curr_cell[1]-1)
                elif d=='S':
                    child_cell=(curr_cell[0]+1,curr_cell[1])
                elif d=='N':
                    child_cell=(curr_cell[0]-1,curr_cell[1])
                if child_cell in explored:
                    continue
                explored.append(child_cell)
                frontier.append(child_cell)
                dfsPath[child_cell]=curr_cell
    fwdPath={}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath

if __name__ == '__main__':
    m = maze(30, 30)
    m.CreateMaze(loopPercent=100)
    path = DFS(m)
    a = agent(m, footprints=True)
    m.tracePath({a:path})

    m.run()