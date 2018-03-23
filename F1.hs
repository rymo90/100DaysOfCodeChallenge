module F1 where
  import Data.Char

  fib :: Integer -> Integer
  fib 0= 0
  fib 1 = 1
  fib n = fib(n-1) + fib(n-2)

  rovarsprak :: String -> String
  rovarsprak "" = ""
  rovarsprak (x:xs) =
    if  not(x `elem`  "aeiou")
      then [x]++"o"++[x]++rovarsprak(xs)
      else [x]++rovarsprak(xs)

  karpsravor :: String -> String
  karpsravor "" = ""
  karpsravor [x] = [x]
  karpsravor(x:xs)=
    if not(x `elem` "aeiou")
      then if head xs =='o'
        then karpsravor(tail xs)
        else [x]++karpsravor(xs)
      else [x]++karpsravor(xs)

  medellangd :: String -> Double
  medellangd ""= 1.0
  medellangd x=
    let
      countLetter = findLetter x
      countWord = findWord x 0 0
      in countLetter/countWord

  findLetter:: String -> Double
  findLetter""= 0
  findLetter(x:xs)=
    if isLetter x
      then 1 + findLetter(xs)
      else findLetter(xs)

  findWord :: String -> Double -> Double -> Double
  findWord "" _ _ = 0
  findWord(x:xs) word notWord =
    if isLetter x
      then if notWord==0
        then word+1 + findWord xs word 1
        else word +  findWord xs word notWord
      else word + findWord xs word 0
  skyffla :: String -> String
  skyffla "" = ""
