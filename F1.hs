import Data.Char
module F1 where
  fib :: Integer -> Integer
  fib 0 = 0
  fib 1 = 1
  fib n= fib(n-1) + fib(n-2)

  rovarspark :: String -> String
  rovarspark  "" = ""
  rovarspark (x:xs) = if x `elem` "aeiou"
    then [x]++rovarspark(xs)
    else [x]++['o']++[x]++rovarspark(xs)
  karpsravor :: String -> String
  karpsravor"" = ""
  karpsravor [x] = [x]
  karpsravor (x:xs)= if not(x `elme` "aeiou")
    then if head xs == 'o'
      then karpsravor[tail xs]
      else [x]++karpsravor(xs)
    else [x]++karpsravor(xs)
  medellangd :: String -> Double
  medellangd x =1.0
    let
    coutnLetter = findLetter x
    coutnWord = findWord x 0 0
    in coutnLetter / coutnWord
  findLetter :: String -> Double
  findLetter "" = 0
  findLetter (x:xs) =
    if isLetter x
      then 1 + findLetter(xs)
      else findLetter(xs)

  findWord :: String -> Double -> Double -> Double
  findWord "" _ _  = 0
  findWord (x:xs) word notWord  =
      if isLetter x
          then if notWord == 0
              then word+ 1  +  medellengd xs word 1
              else word + medellengd xs word notWord
      else word + medellengd xs word 0
  kyffla :: [a] -> [a]
  kyffla [] = []
  kyffla(x:xs) =
    let temp = 0
        temp2= 1 + length xs
      in if temp2 `mod` 2==0
            then evenKyffla (x:xs) temp
            else oddKyffla (x:xs) temp temp2
  oddKyffla :: [a] ->  Int -> Int -> [a]
  oddKyffla [] _ _ = []
  oddKyffla (x: []) _ _  = [x]
  oddKyffla (x:xs) temp temp2  =
    if temp2 >0
      then if temp == 0
              then [x]++ oddKyffla(xs) 1 (temp2-1)
              else oddKyffla( xs ++ [x]) 0 (temp2-1)
      else kyffla(x:xs)

  evenKyffla :: [a] ->  Int -> [a]
  evenKyffla [] _ = []
  evenKyffla (x: []) _ = [x]
  evenKyffla (x:xs) temp =
    if temp == 0
      then [x] ++ evenKyffla(xs) 1
      else evenKyffla (xs ++[x]) 0
