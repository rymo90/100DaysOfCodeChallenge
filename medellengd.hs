import Data.Char
findLetter :: String -> Int 
findLetter "" = 0
findLetter (x:xs) =
  if isLetter x
    then 1 + findLetter(xs)
    else findLetter(xs)
    
findWord :: String -> Int -> Int -> Int
findWord "" _ _  = 0
findWord (x:xs) word notWord  =
    if isLetter x
        then if notWord == 0
            then word+ 1  +  medellengd xs word 1 
            else word + medellengd xs word notWord 
    else word + medellengd xs word 0
    

medellangd x =
  let 
  coutnLetter = findLetter x 
  coutnWord = findWord x 0 0 
  in coutnLetter / coutnWord
