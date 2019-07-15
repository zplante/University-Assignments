/* Zachary Plante, zplante */
/* CMPS 112, W. Mackey, W18 */
/* ASG 4, TZA Schedule Maker */
/* if youre here, and Im here, then WHO'S FLYING THE PLAIN?"*/
toradians(degmin( Degrees, Minutes), Result) :-
	Result is (Degrees + Minutes/60) * pi / 180.

/*function based on given haversine.perl and the Haversine formula*/
haversinedis( Lat1, Lon1, Lat2, Lon2, Distance) :-
	toradians(Lat1, Rlat1),
	toradians(Lon1, Rlon1),
	toradians(Lat2, Rlat2),
	toradians(Lon2, Rlon2),

	DeltaLat is Rlat2 - Rlat1,
	DeltaLon is Rlon2 - Rlon1,

	A is sin(DeltaLat/2) * sin(DeltaLat/2) + cos(Rlat1) *cos(Rlat2)*
		sin(DeltaLon/2) * sin(DeltaLon/2),
	C is 2 * atan2(sqrt(A), sqrt(1-A)),
	Distance is C * 3961.

traveltime(flight(AirportD,AirportA,_),TTime) :-
	airport(AirportD, _ ,Lat1,Lon1),
	airport(AirportA, _ ,Lat2,Lon2),
	haversinedis(Lat1, Lon1, Lat2, Lon2, Distance),
	TTime is Distance/500.

converthours(Hour,Minutes,Con):-
	Con is Hour + Minutes/60.
converthours(time(Hour,Minutes),Con):-
	Con is Hour + Minutes/60.
converttime(Hours,ConHours,ConMinutes):-
	Temp is floor( Hours * 60 ),
	ConHours is Temp // 60,
	ConMinutes is Temp mod 60.

/*function to fix minutes running over 59*/
refresh(time(Hours,Minutes)):-
	converthours(Hours,Minutes,Con),
	converttime(Con,ConHours,ConMinutes),
	Hours is ConHours,
	Minutes is ConMinutes.
arrive(flight(AirportD,AirportA,time(Hour,Minute)),ATime):-
	converthours(Hour,Minute,Con),
	traveltime(flight(AirportD,AirportA,time),TTime),
	ATime is Con + TTime.

not(X):-
	X,
	!,
	fail.
not(_).

withinday(flight(AirportD,AirportA,DTime)):-
	arrive(flight(AirportD,AirportA,DTime),ATime),
	ATime < 24.
withinday(ATime):-
	ATime < 24.
makeflight(DepTime,ArrTime):-
	MakeFlight is DepTime - ArrTime - 0.5,
	MakeFlight >=0.

/*creates list of flights*/
/*inspired by graphpath.pl by W. Mackey*/
/*"Surely you can't be serious captain!"
 * "I am, and don't call me Shirley."*/
schedueler(Destination,Destination,_, [Destination], _ ).
schedueler(Prev,Destination, Visited,[[Prev,DepTime,ArrTime] | List],Dep) :-
	flight(Prev,Destination,Dep),
	not(member(Destination,Visited)),
	converthours(Dep,DepTime),
	arrive(flight(Prev,Destination,Dep),ArrTime),
	withinday(ArrTime),
	schedueler(Destination,Destination,[Destination | Visited], List, _).

schedueler(Prev,Destination,Visited,[[Prev, DepTime, ArrTime] | List], Dep) :-
	flight(Prev,Next,Dep),
	not(member(Next,Visited)),
	converthours(Dep,DepTime),
	arrive(flight(Prev,Next,Dep),ArrTime),
	withinday(ArrTime),
	flight(Next, _, NextDep),
	converthours(NextDep,NextDTime),
	makeflight(NextDTime,ArrTime),
	schedueler(Next,Destination,[Next|Visited],List,NextDep).

/*prints*/
/*I'm sick of these monkey-fighting print errors in my Monday through Friday
 * CODE!*/
padzero(Num) :-
	Num<10, 
	print(0), 
	print(Num).
padzero(Num) :-
	Num>= 10, print(Num).
printtime(SomeTime) :-
	converttime(SomeTime,Hours,Mins),
	padzero(Hours), 
	print(':'), 
	padzero(Mins).

printer([]) :-
	nl.
printer([[CodeD, DepTime, ArrTime],CodeA|[]]) :-
	airport(CodeD,NameD,_,_),
	airport(CodeA,NameA,_,_),
	write('depart   '),
	write(CodeD),
	write('  '),
	write(NameD),
	write('     '),
	printtime(DepTime),
	nl,
	write('arrive   '),
	write(CodeA),
	write('  '),
	write(NameA),
	write('     '),
	printtime(ArrTime),
	nl,
	!, true.

printer( [[CodeD, DepTime, ArrTime], [CodeA, ADepTime, AArrTime] | List] ) :-
	airport(CodeD,NameD,_,_),
	airport(CodeA,NameA,_,_),
	write('depart   '),
	write(CodeD),
	write('  '),
	write(NameD),
	write('     '),
	printtime(DepTime),
	nl,
	write( 'arrive   '),
	write(CodeA),
	write('  '),
	write(NameA),
	write('     '),
	printtime(ArrTime),
	nl,
	!, 
	printer( [[CodeA, ADepTime, AArrTime] | List] ).


/*main function*/
fly(Start,Finish):-
	airport(Start,_,_,_),
	airport(Finish,_,_,_),
	schedueler(Start,Finish,[Start],List,_),
	!,
	nl,
	printer(List),
	true. 

fly(Start,Finish):-
	airport(Start,_,_,_),
        airport(Finish,_,_,_),
	write('flight not possible'),
	nl,
	!,
	fail.
fly(Start,Start):-
	write('your already there dummie'),
	nl,
	!,
	fail.
fly(_,_):-   
	write('those dont exist dummie'),
	nl,
	!,
	fail. 
