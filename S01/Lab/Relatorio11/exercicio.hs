-- 1)
lista1 :: [Int]
lista1 = [30,29..1]

lista2 :: [Int]
lista2 = map (*3) lista1

lista3 :: [Int]
lista3 = reverse lista2

x :: Int
x = last lista3

main :: IO ()
main = do
    putStrLn $ "ultimo elemento: " ++ show x


------------------------------------------------------------------------------------

-- 2)
foo :: Integer -> Integer
foo n
  | n > 0     = f n
  | otherwise = n * 2

f :: Integer -> Integer
f 0 = 1
f n = n * f (n - 1)

main :: IO ()
main = do
  input <- getLine
  let numero = read input :: Integer
  print (foo numero)

