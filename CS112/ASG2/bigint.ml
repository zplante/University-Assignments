(* $Id: bigint.ml,v 1.5 2014-11-11 15:06:24-08 - - $ *)



(*ASG2, Zachary Plante, zplante, CS112 W18*)
open Printf

module Bigint = struct

    type sign     = Pos | Neg
    type bigint   = Bigint of sign * int list
    let  radix    = 10
    let  radixlen =  1


    let length 	  = List.length
    let car       = List.hd
    let cdr       = List.tl
    let map       = List.map
    let reverse   = List.rev
    let strcat    = String.concat
    let strlen    = String.length
    let strsub    = String.sub
    let zero      = Bigint (Pos, [])

    let charlist_of_string str = 
        let last = strlen str - 1
        in  let rec charlist pos result =
            if pos < 0
            then result
            else charlist (pos - 1) (str.[pos] :: result)
        in  charlist last []

    let bigint_of_string str =
        let len = strlen str
        in  let to_intlist first =
                let substr = strsub str first (len - first) in
                let digit char = int_of_char char - int_of_char '0' in
                map digit (reverse (charlist_of_string substr))
            in  if   len = 0
                then zero
                else if   str.[0] = '_'
                     then Bigint (Neg, to_intlist 1)
                     else Bigint (Pos, to_intlist 0)

    let string_of_bigint (Bigint (sign, value)) =
        match value with
        | []    -> "0"
        | value -> let reversed = reverse value
                   in  strcat ""
                       ((if sign = Pos then "" else "-") ::
                        (map string_of_int reversed))
 (*function to trim zeroes*)
	let trimzeros list =
    let rec trimzeros' list' = match list' with
        | []       -> []
        | [0]      -> []
        | car::cdr ->
             let cdr' = trimzeros' cdr
             in  match car, cdr' with
                 | 0, [] -> []
                 | car, cdr' -> car::cdr'
    in trimzeros' list



(*functions to find which number is larger*)
let rec indepthcheck value1 value2  =
        if (value1=[]) 
        then 0
        else if (car value1)>(car value2)
        then 1
        else if(car value1)<(car value2)
        then 2
        else (indepthcheck (cdr value1) (cdr value2))


let findbigger value1 value2 =
        if (length value1)>(length value2)
        then 1
        else if (length value1)<(length value2)
        then 2
        else (indepthcheck (reverse value1) (reverse value2))



(*add and sub helper functions*)
    let rec add' list1 list2 carry = match (list1, list2, carry) with
        | list1, [], 0       -> list1
        | [], list2, 0       -> list2
        | list1, [], carry   -> add' list1 [carry] 0
        | [], list2, carry   -> add' [carry] list2 0
        | car1::cdr1, car2::cdr2, carry ->
          let sum = car1 + car2 + carry
          in  sum mod radix :: add' cdr1 cdr2 (sum / radix)
(* insert sub here*)
	let rec sub' list1 list2 carry = match (list1, list2, carry) with
        | list1, [], 0       -> list1
	| [], list2, 0	     -> list2
        | list1, [], carry   -> sub' list1 [carry] 0
	| [], list2, carry   -> sub' [carry] list2 0
        | car1::cdr1, car2::cdr2, carry ->
          let dif = car1 - car2 + carry
          in if dif<0
         then (dif mod radix) + radix :: sub' cdr1 cdr2 (0-radix)
	else dif :: sub' cdr1 cdr2 0

(*add and sub*)
    let add (Bigint (neg1, value1)) (Bigint (neg2, value2)) =
        if neg1 = neg2
        then Bigint (neg1, add' value1 value2 0)
        else if findbigger value1 value2=1
	then (Bigint (neg1, (trimzeros (sub' value1 value2 0))))
	else if findbigger value1 value2=2
	then (Bigint (neg2,(trimzeros (sub' value2 value1 0))))
	else zero
	


    let sub (Bigint(sign1, value1)) (Bigint(sign2, value2)) =
	if sign2=Pos
	then add (Bigint(sign1, value1)) (Bigint(Neg, value2))
	else add (Bigint(sign1, value1)) (Bigint(Pos, value2))

(* praise lord 'chanka*)
(*mul and mul helper*)
  let rec mul' (multiplier, powerof2, multiplicand) =
     if findbigger powerof2 multiplier = 1
     then multiplier, []
     else let remainder, product =
        mul' (multiplier,add' powerof2 powerof2 0, add' multiplicand multiplicand 0)
          in  if findbigger remainder powerof2 = 2
              then remainder, product
              else trimzeros(sub' remainder powerof2 0), add' product multiplicand 0


    let mul (Bigint(sign1, value1)) (Bigint(sign2, value2))=
      let _, product = mul' (value1, [1], value2) in
      if sign1=sign2
        then (Bigint(Pos, product))
        else (Bigint(Neg, product))

(*div, rem and div helper*)
let rec div'(dividend, powerof2, divisor) =
    if findbigger divisor dividend = 1
    then [], dividend
    else let quotient, remainder =
             div' (dividend, add' powerof2 powerof2 0, add' divisor divisor 0)
         in  if findbigger remainder divisor = 2
             then quotient, remainder
             else add' quotient powerof2 0, trimzeros(sub' remainder divisor 0)


    let div (Bigint(sign1, value1)) (Bigint(sign2, value2))=
	let quo, _ = div' (value1, [1], value2) in
	if sign1 = sign2
        then (Bigint(Pos, quo))
        else (Bigint(Neg, quo))

    let rem (Bigint(sign1, value1)) (Bigint(sign2, value2))=
	let _, rem = div'(value1, [1], value2) in
	(Bigint(Pos, rem))
	(*power and power helper*)
	let rec pow'(Bigint(sign1, value1)) count (Bigint(sign2, value2)) =
		if findbigger count [2] = 1
		then (Bigint(sign2, value2))
		else pow' (Bigint(sign1, value1)) (trimzeros(sub' count [1] 0)) (mul (Bigint(sign1, value1)) (Bigint(sign2, value2)))

    let pow (Bigint(sign1, value1)) (Bigint(sign2, value2)) =
	let prod = (Bigint(sign1, value1))in
	pow' (Bigint(sign1,value1)) value2 prod

end

