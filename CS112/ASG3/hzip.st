#!/afs/cats.ucsc.edu/courses/cmps112-wm/usr/smalltalk/bin/gst -f
"hzip.st by Zachary Plante, zplante"
"starter code by W. Mackey"
"god i hope this works"

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
	DFS: aboi [
	  |count|
	  count := 8.
	  aboi writeBit: 0.
	  [count > 0] whileTrue:[
	  aboi writeBit: (char bitAt:count).
	  count := count - 1.
	  ].
	  char asInteger = 256 ifTrue:[
	  aboi writeBit: 1.
	].
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
	DFS: aboi [
	  left DFS: aboi.
	  right DFS: aboi.
	  aboi writeBit: 1.
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

		
		

"start main"
nl := Character nl.
Smalltalk arguments size > 3 ifTrue: [
stderr << 'please enter the proper number of arguments' << nl.].
Smalltalk arguments size < 2  ifTrue: [
	stderr << 'please enter the proper number of arguments' << nl.
] ifFalse: [
|flag inputname outputname|

inputname := Smalltalk getArgv: 2.
Smalltalk arguments size = 3 ifTrue:[
outputname := Smalltalk getArgv: 3.
]ifFalse:[
ouputname := stdout.
].
flag := (Smalltalk arguments at: 1).
flag = '-d' ifTrue: [
stdout << 'debugging is where you learn you cant read and cant count' << nl.
] ifFalse: [
flag = '-t' ifTrue: [
	|ftable root sorcol ptable input output name path|
	input := FileStream open: inputname mode: FileStream read.
	ftable := ZeroArray new: 257.
	 [input atEnd not] whileTrue:[
	    |tempChar|
	    tempChar := input next asInteger.
	    ftable incr: tempChar.
	  ].
	  input reset.
	  ftable at: 256 put: 1.
	  sorcol := SortedCollection new.
	   ftable keysAndValuesDo: [:char :count |
		((count isNil not) and: [count > 0]) ifTrue: [
			|leaf|
			leaf := Leaf new: char  count: count.
			sorcol add: leaf.
		]
	].
	
	[sorcol size > 1] whileTrue: [
	  |temp1 temp2 newtree leadchar treecount|
	  temp1 := sorcol removeFirst.
	  temp2 := sorcol removeFirst.
	  leadchar := temp1 char.
	  treecount := temp1 count + temp2 count.
  newtree := Tree new: leadchar count: treecount left: temp1 right: temp2.
	sorcol add: newtree.
	].	
	root := sorcol first.
	  ptable := ZeroArray new: 257.
	  root inorder: [:char :string |
		ptable at: char asInteger put: string.
	  ] prefix: ''. 
	Smalltalk arguments size =3 ifTrue:[
	output:= FileStream open: outputname.
        ]ifFalse:[
        output:=stdout.].
	  ftable keysAndValuesDo: [:char :count |
		(count isNil not and: [count > 0]) ifTrue:[
		 name:= char asCharacter visible.
        path:= ptable at: char.
        name asString size to: 10 do: [:skip| output << ' '].
        count asString size to: 10 do: [:skip| output<<' '].
        path asString size to: 10 do: [:skip| output << ' '].

		output << name<< ' '
                << count<< ' '
                << path<< nl. 
		].
	].
  
]ifFalse: [
flag = '-c' ifTrue: [

	|ftable root sorcol ptable input output writbit|
	input:= FileStream open: inputname
                mode: FileStream read.
	ftable := ZeroArray new: 257.
	 [input atEnd not] whileTrue:[
	    |tempChar|
	    tempChar := input next asInteger.
	    ftable incr: tempChar.
	  ].
	  input reset.
	  sorcol := SortedCollection new.
	   ftable keysAndValuesDo: [:char :count |
		(count isNil not and: [count>0]) ifTrue: [
			|leaf|
			leaf := Leaf new: char  count: count.
			sorcol add: leaf.
		].
	].
	
	[sorcol size > 1] whileTrue: [
	  |temp1 temp2 newtree leadchar treecount|
	  temp1 := sorcol removeFirst.
	  temp2 := sorcol removeFirst.
	  leadchar := temp1 char.
	  treecount := temp1 count + temp2 count.
  newtree := Tree new: leadchar count: treecount left: temp1 right: temp2.
	  sorcol add: newtree.
	].	
	root := sorcol first.
	  ptable := ZeroArray new: 257.
	  root inorder: [:char :string |
		ptable at: char asInteger put: string.
	  ] prefix: ''.
	Smalltalk arguments size = 3 ifTrue:[
	output := FileStream open: outputname mode: FileStream write] ifFalse:[
	output := stdout.].
 
	writbit := OutBits new: output.
		root DFS: writbit.
	 
	  [input atEnd not] whileTrue: [
		|temp path|
		temp := input next asInteger.
		path := ptable at: temp
		path do: [:count|
			count asString = '0' ifTrue:[ writbit writeBit: 0.]
			ifFalse: [writbit writeBit:1.].
		].
	  ].

	  ptable at:256 do: [:count|

		count asString = '0' ifTrue:[ writbit writeBit: 0.]
		ifFalse: [writbit writeBit: 1.].
].
	  writbit flushByte.
	  input close.
	  output close.

			
]ifFalse: [
flag = '-u' ifTrue: [ 
	|thebyte treenotdone root trav end orcol tempbit input output|
	input:= FileStream open: inputname
                mode: FileStream read.
	output := FileStream open outputname.
	thebyte :=0.
	treenotdone := true.
	orcol := OrderedCollection new.
	[treenotdone=true] whileTrue: [
	  tempbit := input nextBit.
	  tempbit = 0 ifTrue: [
		|count newleaf|
		count :=8.
		thebyte :=0.
		[count > 0] whileTrue:[
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
	Smalltalk arguments size =3 ifTrue:[
		output:= FileSTream open: outputname.]ifFalse:[
		output:=stdout.
		].
	[(input atEnd not)and:(end=false)] whileTrue: [
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
	input close.
	output close.

]ifFalse:[
stdout << 'dont be a smartass and please pick an actualy command'<<nl.
].

].
].
].
].
