"""
2023/09/12
rubyでFizzBuzzを行うコード
"""

for i in 1..50
    if i%3==0 and i%5==0
        puts "FizzBuzz"
    elsif i%3==0
        puts "Fizz"
    elsif i%5==0 
        puts "Buzz"
    else
        puts i
    end
end

