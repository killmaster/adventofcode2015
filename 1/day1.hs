import Data.Char

main = do
  contents <- getContents
  putStrLn (show (findFloor contents))
  putStrLn (show (enterBasement contents 0 0))  -- starting on 0 because recursion
                                                -- takes one more step


findFloor :: [Char] -> Int
findFloor =
  foldl (\acc c ->
  case c of '(' -> (acc + 1)
            ')' -> (acc - 1)) 0

-- findFloor =
--   foldl (\acc c ->
--   if c == '('
--     then acc + 1
--     else if c == ')'
--       then acc - 1
--       else acc) 0



-- findFloor [] = 0
-- findFloor ('(': cs) = 1 + findFloor cs
-- findFloor (')': cs) = (-1) + findFloor cs
-- findFloor (_:cs) = findFloor cs

enterBasement :: String -> Int -> Int -> Int
enterBasement _ (-1) i        = i
enterBasement (c:cs) floor i  = case c of '(' -> enterBasement cs (floor + 1) (i + 1)
                                          ')' -> enterBasement cs (floor - 1) (i + 1)
                                          '_' -> enterBasement cs floor (i + 1)
