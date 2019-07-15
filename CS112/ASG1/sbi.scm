#!/afs/cats.ucsc.edu/courses/cmps112-wm/usr/racket/bin/mzscheme -qr
;; $Id: sbi.scm,v 1.3 2016-09-23 18:23:20-07 - - $
;; Zachary Plante
;; CS112, ASG 1
;; CruzID: zplante
;;
;; CAN ONLY RUN FIRST 3 FILES
;; NAME
;;    sbi.scm - silly basic interpreter
;;
;; SYNOPSIS
;;    sbi.scm filename.sbir
;;
;; DESCRIPTION
;;    The file mentioned in argv[1] is read and assumed to be an SBIR
;;    program, which is the executed.
;;


;;
;;symbol tabel, based on symbols.scm in the class directory
(define *symbol-table* (make-hash))
(define (symbol-get key)
        (hash-ref *symbol-table* key))
(define (symbol-put! key value)
        (hash-set! *symbol-table* key value))

(for-each
    (lambda (pair)
            (symbol-put! (car pair) (cadr pair)))
    `(

        (log10_2 0.301029995663981195213738894724493026768189881)
        (sqrt_2  1.414213562373095048801688724209698078569671875)
        (e       2.718281828459045235360287471352662497757247093)
        (pi      3.141592653589793238462643383279502884197169399)
        (/     ,(lambda (x y) (floor (/ x y))))
        (log10   ,(lambda (x) (/ (log x) (log 10.0))))
        (%     ,(lambda (x y) (- x (* (/ x y) y))))
        (quot    ,(lambda (x y) (truncate (/ x y))))
        (rem     ,(lambda (x y) (- x (* (quot x y) y))))
        (+       ,+)
        (^       ,expt)
        (ceil    ,ceiling)
        (exp     ,exp)
        (floor   ,floor)
        (log     ,log)
        (sqrt    ,sqrt)
	(print	,print)
	(*	,*)
	(-	,-)
	(goto ,	(lambda(x) (label-get x)	))
	(let , (lambda(x y) (symbol-put! x y)))
	(if , (lambda(x y z) (if x y z)))
	(input , (lambda(x) (symbol-put! input x))) 
	(dim , (lambda(x y) (symbol-put! x y)))
		

     ))

;;
;;label tabel, based on code from symbols.scm in the class directory
(define *label-table* (make-hash))
(define (label-get key)
        (hash-ref *label-table* key))
(define (label-put! key value)
        (hash-set! *label-table* key value))

;;
;;pass through program to find labels
(define (label-first-pass program )
	(cond 
	[(null? program)
	(+ 1 1)]
	[else
	(if (not(null? (cdr(car program))))
	(label-put! (cdr(car program)) (cdr program))
	(+ 1 1))
	(label-first-pass (cdr program))
]
)

)

;;sbi.scm functions, based on or borrowed from the class directory
(define *stderr* (current-error-port))

(define *run-file*
    (let-values
        (((dirpath basepath root?)
            (split-path (find-system-path 'run-file))))
        (path->string basepath))
)

(define (die list)
    (for-each (lambda (item) (display item *stderr*)) list)
    (newline *stderr*)
    (exit 1)
)

(define (usage-exit)
    (die `("Usage: " ,*run-file* " filename"))
)

(define (readlist-from-inputfile filename)
    (let ((inputfile (open-input-file filename)))
         (if (not (input-port? inputfile))
             (die `(,*run-file* ": " ,filename ": open failed"))
             (let ((program (read inputfile)))
                  (close-input-port inputfile)
                         program))))
(define (write-program-by-line filename program)
    (map (lambda (line) (printf "~s~n" line)) program)
    (printf ")~n"))
;;interprets the lines of code
(define (interpret-line line)
	(cond
	[ (null? line)
	(+ 1 1)]
	
	[else (interpret-line (cdr line))
	(apply (symbol-get (caar line)) (cdar line))]
	
))
;;cycles through lines
(define (do-program-by-line program)
	(cond
	[ (null? program)
	(newline)]
	[else 
	(interpret-line (cdr(car program)))
	(do-program-by-line (cdr program)) ]
))
(define (main arglist)
    (if (or (null? arglist) (not (null? (cdr arglist))))
        (usage-exit)
        (let* ((sbprogfile (car arglist))
               (program (readlist-from-inputfile sbprogfile)))
		(label-first-pass program)
              (do-program-by-line program))))
;;main
(main (vector->list (current-command-line-arguments)))
