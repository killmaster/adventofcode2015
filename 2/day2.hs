import Data.List.Split

parseList :: [String] -> [(Int,Int,Int)]
parseList presents  =
  fmap ((\[l,w,h] -> (read l, read w,read  h)) . splitOn "x") presents

presentWrappingPaper :: (Int,Int,Int) -> Int
presentWrappingPaper (l,w,h) = 2*a1 + 2*a2 + 2*a3 + minimum[a1,a2,a3]
  where a1 = l * w
        a2 = w * h
        a3 = l * h

partOne :: [(Int,Int,Int)] -> Int
partOne = accum 0
  where
    accum n [] = n
    accum n (present: presents) =
      accum (n + presentWrappingPaper present) presents

presentWrappingRibbon :: (Int,Int,Int) -> Int
presentWrappingRibbon (l,w,h) = 2*a1 + 2*a2 + a3
  where a1 = minimum[l,w,h]
        a2 = secondSmallest[l,w,h]
        a3 = l * w * h
        lowPassFilter = filter (not . (== a1))
        secondSmallest ss
          | length (lowPassFilter ss) == 1 = a1
          | otherwise = minimum(lowPassFilter ss)

partTwo :: [(Int,Int,Int)] -> Int
partTwo = accum 0
  where
    accum n [] = n
    accum n (present: presents) =
      accum (n + presentWrappingRibbon present) presents

main = do
  input <- readFile "day2input.txt"
  let presents = lines input
  putStrLn(show(partOne(parseList presents)))
  putStrLn(show(partTwo(parseList presents)))
