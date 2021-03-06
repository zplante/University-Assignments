#!/afs/cats.ucsc.edu/courses/cmps112-wm/usr/smalltalk/bin/gst -f
"hzip.st by Zachary Plante, zplante"
"starter code by W. Mackey"
"god i hope this works"
"arguments need work"
"insert a vine compliation to match my mood after finishing typing this"
"FileStream by W. Mackey"

FileStream extend [
	|bitIndex currentChar|

	nextBit [
	   |bit|
	   bitIndex isNil ifTrue: [bitIndex := 0].
	   bitIndex = 0 ifTrue: [
		bitIndex := 8.
		currentChar := self next.
	   ].
	   bit := currentChar value bitAt: bitIndex.
	   bitIndex := bitIndex - 1.
	   ^ bit
	]

	atBitEnd [
	   ^ (bitIndex isNil | (bitIndex = 0)) & self atEnd
	]
]

"Leaf and Tree by W. Mackey"

Object subclass: Leaf [
	|char count|
	char [^ char]
	count [^ count]

	Leaf class >> new [
	   self shouldNotImplement 
	]
	
	Leaf class >> new: aChar count: aCount [
	   |result|
	   result := super new.
	   result setChar: aChar andCount: aCount.
	   ^result
	]

	setChar: aChar andCount: aCount [
	   char := aChar.
	   count := aCount.
	]

	<= other [
	   ^ (count < other count) |
	   ((count = other count) & (char <= other char))
	]
	printBase: aStream [
	   ^ aStream << self class << '(' << char << ',' << count
	]

	printOn: aStream [
	   (self printBase: aStream) << ')'.
	]

	inorder: visitor prefix: string [
	   visitor value: char value: string.
	]
	isLeaf[^true]

]


Leaf subclass: Tree [
	|left right|
	
	Tree class >> new: aChar count: aCount [
	   self shouldNotImplement
	]

	Tree class >> new: aChar count: aCount left: aLeft right: aRight [
	  |result|
	  result := super new: aChar count: aCount.
	  result setLeft: aLeft andRight: aRight.
	  ^ result
	]

	setLeft: aLeft andRight: aRight [
	   left := aLeft.
	   right := aRight.
	]

	inorder: visitor prefix: string [
	   left inorder: visitor prefix: string, '0'.
	   right inorder: visitor prefix: string, '1'.
	]
	postorder: writbit [
	  left postorder: writbit.
	  right postorder: writbit.
	  writbit writebit: 1.
	]
	isLeaf [^false]
]

"Character extend and ZeroArray by W. Mackey"

Character extend [
   isPrint [
      ^ (Character space <= self) & (self <= $~)
   ]
   visible [
      self isPrint ifTrue: [^ '$', self asString]
                   ifFalse: [^ self asInteger printStringRadix: 8]
   ]
]

Object subclass: ZeroArray [
   |theArray|

   ZeroArray class >> new [
      self shouldNotImplement.
   ]

   ZeroArray class >> new: size [
      |result|
      result := super new.
      result init: size.
      ^ result
   ]

   init: size [
      theArray := Array new: size.
   ]

   size [
      ^ theArray size.
   ]

   at: index [
      ^ theArray at: index + 1.
   ]

   at: index put: value [
      ^ theArray at: index + 1 put: value.
   ]

   incr: index [
      (self at: index) isNil
         ifTrue: [ self at: index put: 0].
      self at: index put: (self at: index) + 1.
   ]

   keysAndValuesDo: aBlock [
      (0 to: (self size) - 1) do: [:index |
         aBlock value: index value: (self at: index).
      ]
   ]

]

"OutBits by W. Mackey"
	
Object subclass: OutBits [
	|bitIndex currentByte myStream|
	OutBits class >> new [
	self shouldNotImplement.
	]
	OutBits class >> new: fileStream [
	  |result|
	  result := super new.
	  result init: fileStream.
	  ^result
	]
	clearByte [
	  bitIndex := 8.
	  currentByte := 0.
	]
	init: fileStream [
	  myStream := fileStream.
	  self clearByte.
	]
	flushByte[
		bitIndex = 8 ifFalse: [
		  myStream nextPutByte: currentByte.
		  self clearByte.
		]
	]
	writeBit: bit[
	currentByte := currentByte bitAt: bitIndex put: bit.
	bitIndex := bitIndex -1.
	bitIndex = 0 ifTrue: [self flushByte].
	]
]

Object subclass: TreeBuilder [
	
	TreeBuilder class >> new[
	  |result|
	  result := super new.
	  ^result
	]

	buildtable: file[
	|table|
	table := ZeroArray new: 257
	 file atEnd not whileTrue:[
	    |tempChar|
	    tempChar := file next asInteger.
	    table incr: tempChar.
	  ].
	  file reset.
	  ^table
]

	maketree: table [
	|root sorcol|
	  sorcol := SortedCollection new.
	   table keysAndValuesDo: [:char :count |
		count isNil not & count>0 ifTrue: [
			|leaf|
			leaf := Leaf new: char  count: count
			sorcol add: leaf
		]
	].
	
	sorcol size > 1 whileTrue: [
	  |temp1 temp2 newtree leadchar treecount|
	  temp1 := sorcol removeFirst.
	  temp2 := sorcol removeFirst.
	  leadchar := temp1 char.
	  treecount = temp1 count + temp2 count.
  newtree := Tree new: leadchar count: treecount left: temp1 right: temp2
	].	
	root := sorcol first.
	^root
]
	makepathstrings: root[
	  |pathtable|
	  pathtable := ZeroArray new: 257.
	  root inorder: [:char :string |
		pathtable at char asInteger put: string.
	  ] prefix: ''. 

	]
	printtreetable: root andFT: table andPT: path [
	  table keysAndValuesDo: [:char :count |
		(count isNil not and: count>0) ifTrue:[
		stdout<<char visible<<' '<<count asFixedWidth: 7<<' '<<
		path at: char<<Character nl. 
		]
	]
]
]
Object subclass: Compressor [
	Compressor class >> new [
	  |result|
	  result := super new.
	  ^result.
	]
      writecfile: writbit andOut: output andIn: input andTree: root andPT:path[
	  root postorder: writbit.
	  writbit writeBit: 1.
	  input reset.
	  [input atEnd not] whileTrue: [
		|temp|
		temp := input next asInteger.
		writbit writeBitString: (path at: temp).
	  ]

	  writbit writeBitString: (path at: 256).
	  writbit flushByte.
	  input close.
	  output close.
	]

      writeufile:input andOut: output [
	|thebyte treenotdone root trav end orcol tempbit|
	thebyte :=0.
	treenotdone := true.
	orcol := OrderedCollection new.
	(treenotdone) whileTrue: [
	  tempbit := input nextBit.
	  tempbit = 0 ifTrue: [
		|count newleaf|
		count :=8.
		thebyte :=0.
		count > 0 whileTrue:[
		  tempbit := input nextBit.
		  thebyte := thebyte bitAt: count put: tempbit.
		  count := count -1.
		  ].
		thebyte = 0 ifTrue: [
		  tempbit := input nextBit.
		  tempbit = 1 ifTrue: [
			 thebyte := thebyte + 256.
			].
		].
		
		"insert animal crossing joke"
		newleaf := Leaf new: thebyte asCharacter count:1.
		orcol addFirst: newleaf.
		]ifFlase: [

		  orcol size =1 ifTrue: [

			treenotdone:=false.
			]ifFalse:[
		  |temp1 temp2 newtree|
		  temp2:= orcol removeFirst.
		  temp1:= orcol removeFirst.
		  
	     newtree :=Tree new: (temp2 char) count:1 left: temp1 right:temp2.
		  orcol addFirst: newtree.
		
		].
		].

	   ].
	end := false.
	root := orcol removeFirst.
	trav := root.
	(input atEnd not)&(end=false) whileTrue: [
		tempbit := input nextBit.
		trav isLeaf ifTrue:[
		trav char asInteger =256 ifTrue: [end :=true].
		]ifFalse:[
		tempbit=0 ifTrue:[
		trav := trav left.
		trav isLeaf ifTrue:[
		trav char asInteger = 256 ifTrue: [end :=true]
		ifFalse:[ output<<trav char.
				trav:=root. ].
		].
		]ifFalse:[
		trav:=trav right.
		trav isLeaf ifTrue:[
		trav char asInteger = 256 ifTrue:[end:=true]
		ifFalse: [ output<<trav char.
				trav:=root.].
		].
		].
		].
	].
	
	]
	
	

]


"start main"
nl := Character nl.
Smalltalk arguments size > 3 ifTrue: [
stderr << 'please enter the proper number of arguments' << nl.].
Smalltalk arguments size < 2  ifTrue: [
	stderr << 'please enter the proper number of arguments' << nl.
] ifFalse: [
|input output flag|

input := FileStream open: (Smalltalk arguments at: 2)
mode: FileStream read.
Smalltalk arguments size = 3 ifTrue: [
	output := FileStream open: (Smalltalk arguments at: 3)
	mode: FileStream write.
	] ifFalse: [
	output :=stdout.
].
flag := (Smalltalk arguments at: 1).

flag = '-d' ifTrue: [
stdout << 'debugging is where you learn you cant read and cant count' << nl.
] ifFalse: [
flag = '-t' ifTrue: [
	|treeB root ftable ptable|
	treeB := TreeBuilder new.
	ftable := treeB buildtable: input.
	root := treeB maketree:ftable.
	ptable := treeB makepathstrings: root.
	treeB printtreetable: root andFT: ftable andPT: ptable.  
]ifFalse: [
flag = '-c' ifTrue: [
	|treeB comp bitwrit root ftable ptable|
	treeB := TreeBuilder new.
	comp := Compressor new.
	bitwrit := OutBits new: output.
        ftable := treeB buildtable: input.
        root := treeB maketree:ftable.
        ptable := treeB makepathstrings: root.
comp writcfile: writbit andOut: output andIn: input andTree: root andPT: ptable.
	
]ifFalse: [
flag = '-u' ifTrue: [ 
	|comp|
	comp := Compresor new.
	comp writeufile: input andOut: output.
]ifFalse:[
stdout << 'dont be a smartass and please pick an actualy command'<<nl.
].

].
].
].
].





