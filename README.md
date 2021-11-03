IEEEXtreme

IEEEXtreme is a global competition organised every year by IEEE. Its duration is 24 hours and teams from all over the world try to solve algorithmic problems that come out every 30 minutes.

Personally, it was my first year participating as a student in this contest and I focused especially in two significant problems. My suggested solutions are not the optimal, since they were both accepted as correct (given the right outputs) but they didnt meet the best time constraints parameters. 
As a result they both performed 50% of the total points, but it was a nice approach to the problem.

First problem is called "Image Similarity" and in that case we were given a large amount of cases to examine. Each time the input data was two images consisting of dots (.) and hashtags (#) and the purpose was to find how similar they are by testing if the shape that all #s make in the first image is somehow appeared in the second. You could rotate, mirror and move the image in any way. 

My approach was to take the first image and test the current similarity factor by finding a Jaccard score for each row of the corresponding matrices. Then, flip, mirror and move the image in any possible way, do the same process again and finally output the best Jaccard Score that was found till that moment. Earlier termination criterion is when the max Jaccard possible score was found in the process.

Second problem was IEEE Teams, in that one we were given students and their abilities over some fields. The purpose was to find out how many combinations of given student we could make to finally construct a team that should satisfy some specific abilities.
