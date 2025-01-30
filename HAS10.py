def itinerary(tick):
    fmap = {}
    for src, dest in sorted(tick):
        if src in fmap:
            fmap[src].append(dest)
        else:
            fmap[src] = [dest]
    itin = []
    def dfs(airprt):
        while airprt in fmap and fmap[airprt]:
            ndest = fmap[airprt].pop(0)
            dfs(ndest)
        itin.append(airprt)
    dfs("JFK")
    return itin[::-1]

tick = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(itinerary(tick))



