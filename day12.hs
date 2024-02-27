stripDots :: String -> String
stripDots s
    |s == "" = ""
    |s !! 0 == '.' = stripDots $ drop 1 s
    |s !! ((length s) - 1) == '.' = stripDots $ take ((length s) - 1) s
    |otherwise = s

allHashtag :: String -> Bool
allHashtag "" = True
allHashtag (h:t)
    |h /= '#' = False
    |otherwise = allHashtag t

getCombinations :: String -> [String]
getCombinations "?" = ["#", "."] 
getCombinations "#" = ["#"]
getCombinations "." = ["."]
getCombinations ('?':t) = [ (hs : ts) | ts <- getCombinations t, hs <- ".#"]
getCombinations (h:t) = [ (h : ts) | ts <- getCombinations t]

getCleanCombinations :: String -> [String]
getCleanCombinations ls = map stripDots $ getCombinations ls

isValid :: [Int] -> String -> Bool
isValid [] "" = True
isValid [] (h:_) = False
isValid (h:_) [] = False
isValid (hn:tn) s
    |hn > length s = False
    |hn == (length s) && allHashtag s = isValid tn ""
    |hn == (length s) = False
    |(allHashtag $ take hn s) && ((head $ drop hn s) == '.') = isValid tn $ stripDots $ drop hn s
    |otherwise = False

countTrue :: [Bool] -> Int
countTrue ls = foldr (\x y -> if x then y + 1 else y) 0 ls

getValidCombinations :: String -> [Int] -> Int
getValidCombinations pattern nums = countTrue $ map (isValid nums) (filter (/="") $ map stripDots $ getCleanCombinations pattern)

result :: [(String, [Int])] -> Int
result ls = sum [getValidCombinations (fst p) (snd p) | p <- ls]

-- t :: [(String,[Int])] = [("???????????????#????", [4,8,1])]
t1 :: [(String,[Int])] = [("??", [2])]

main = putStrLn (show $ result t1)