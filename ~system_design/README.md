# System Design Interview - Approach and Structure

https://www.youtube.com/watch?v=0163cssUxLA

## Phase 1: clarify questions and gathering requirement
* Interviewer wants to see two things from you and purposefully leave out details

#### Handle ambiguity - you are able to recognize the breath of the problem statement
* What kind of problem area he wants to get into - "do you want me to come up with a system design, or class hierarchy, should we get into some specific question and write some methods"

#### Systematic approach - how you approach the problem
* You want to show a clear and systematic approach how you want to tackle the problem
* It helps to take a step back and don't rush into one solution immediately
* It's time to ask questions and clarify some assumptions

## Phase 2: Draw high level diagram
* Draw couple of rectangles and explain the main components of the architecture
* Explain what considerations you're making, what properties should this database fulfill, what are the choices you're gonna make if you could chose a type database
* Try to keep it a bit more general, give a bit of detail but not too much

## Phase 3: Explain the critical parts
* Sometimes makes sense to talk about the data model - how you would store the media compare to user data and metadata about media or even draw a database schema for the most important parts of the system
* Some times make sense to define the APIs between two components which shows that you actually thought about why this is split up in components, how is it reusable, how it makes the system more efficient in general

## Phase 4: Dive into details
* Engage the interviewer and this feels like an actual conversation you have with a colleague or co-worker
* Try to communicate and encourage the interviewer to communicate with you because they're going to lead you into the direction they want to go
* You don't want to just have this monologue
* The interviewer is looking for certain properties you have and they want to confirm that you check those boxes
* If the interview is going well, it will lead naturally into one or two topics that you will talk about in more detail with the interviewer
* If the interview is not going that well, you need to actively ask the interviewer and try to find out what you should be talking about in more detail - ask "which component I shall talk about in more depth"
* Usually the conversations turn into optimizations and edge cases - adding caching layer, pre-computation, how to improve the customer experience by using a CDN
* You can also dive into operational topics - logging, metrics, auditing, making the system more reliable, replication, single point of failure
