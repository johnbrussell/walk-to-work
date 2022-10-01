### The problem

I want to know the fastest route to walk to work given the signal timing of the intersections I could choose to go through on the way.  I start by walking down Broadway toward Kendall Square; the scope of the problem I am trying to solve is the part of my route that takes me from the western corner of the Broadway/Technology Square/Hampshire intersection to the southeastern corner of the Main/Ames intersection.

### The data

The data I have for these intersections is as of yet incomplete, but the Main/Ames intersection is a 90 second signal cycle at rush hour; it seems plausible that all of the intersections in this project are also 90 second cycles.  So, I've plugged in the following signal timings:
- Broadway and Technology Square/Hampshire: 30 seconds green on Broadway, 60 seconds red
- Broadway and Binney/Galileo Galilei: 30 seconds green on Broadway, 60 seconds red
- Broadway and Ames: 30 seconds green on Broadway, 60 seconds red
- Main and Vassar/Galileo Galilei: 45 seconds green on Broadway, 45 green on Vassar/Galileo Galilei
- Main and Ames: 30 seconds green on Main, 60 seconds green on Ames (10 seconds of which has no pedestrian signal).  (Currently the only intersection with measured, rather than estimated, data).

For each of these intersections, I deduct a commensurate amount of time to account for the fact that crossing the street takes a nontrivial number of seconds.  Although this will vary somewhat, my best estimate for the non-crossable green-lit time across each street is:
- To cross Tech Sq on Broadway: 5 seconds
- To cross Binney/Galileo Galilei on Broadway: 10 seconds
- To cross Ames on Broadway: 5 seconds
- To cross Vassar/Galileo Galilei on Main: 15 seconds
- To cross Main on Vassar/Galileo Galilei: 15 seconds
- To cross Ames on Main: 5 seconds
- To cross Main on Ames: 5 seconds

I further assume that these durations are equivalent to the amount of time it takes to cross these streets (note: this assumption is great for simplifying the problem, particularly at Main and Vassar/Gailieo Galilei, but it's also not entirely true, particularly at Main and Vassar/Galileo Galilei, where crossing either street is probably a 10 second affair (or maybe 7 to cross Main)).  This assumption is potentially somewhat more problematic than it seems on the surface: because this program measures only time spent waiting to cross and time spent walking down Technology Square and Galileo Galilei specifically, assuming a longer-than-true walking time across certain intersections ends up favoring those intersections by adding less delay than they actually cause.

Although predictable 90 second cycles will not behave independently in practice, I make this assumption anyway to simplify the calculations in this analysis.

Furthermore, I add a penalty of 24 seconds to walk down Technology Square and 9 seconds to walk down Galileo Galilei because these routes are longer than the shortest possible walking route (which is to walk on Broadway until its intersection with Ames).  

These results are only valid for the walk to work, not for the walk home.

### Results

The route with the least combined average delay from additional walking time and waiting to cross intersections is to turn right on Technology Square, left on Main Street, then cross both Main Street and Vassar/Galileo Galilei at their intersection, then continue down the southern side of Main until reaching the southeastern corner of Main and Ames.

But, this route is not guaranteed to be the fastest: although the shortest possible route is not the fastest on average, it is possible that on a very lucky day one would not need to wait any time to cross any of the intersections along it.

Some routes are guaranteed to have more expected delay:
- if you cross Binney/Galileo Gailiei on Broadway, you should never proceed to walk down Galileo Galilei toward Main St.
- when approaching the northwest corner of Main and Vassar/Galileo Galilei and Main and Ames, you should always plan on crossing whichever direction becomes crossable first.  Planning to cross one direction or the other first is always slower.
- planning to cross Ames at Broadway has a higher expected delay than turning right onto Ames and heading to the Main/Ames intersection.
