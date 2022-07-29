# Singapore Polytechnic-Centroid Counter
 
*** 
<strong>Introduction</strong>
***

The aim of the project is to develop a simple algorithm to count the number of people in the room. This algorithm was part of a bigger project, but his repository will only focus on the algorithm.

Using OpenCV and python, the team achieved the aim by counting centroids. The way we ‘count’ the number of people in the room is to detect centroids moving pass a given threshold. A centroid is created and given and ID number when moving is detected. If the centroid moves past the ‘entry’ threshold, the program considers it as a person entering the room. Similarly, if a centroid moves past the ‘exit’ threshold, the program considers it as a person leaving the room.

If movement is detected near an existing centroid, that centroid is reused instead of making a new one.


***

<strong>Video demonstration</strong>

***

<iframe width="560" height="315" src="https://www.youtube.com/embed/nILaMWWoH28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
