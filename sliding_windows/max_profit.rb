=begin
PROBLEM:
We are given an array of stock prices.
  - indices are days
  - so the prices are from day 0 to the day n
  - for example:
  [2, 3, 4, 5, 1]
  - price on day 0 is 2, day 1 is 3, day 2 is 4, day 3 is 5 and day 4 is 1

From these prices we need to find out the maximum profits we can have.
From buying on the lowest price day and selling on highest price day.
We can sell in the past, so a stock bought on day 2 cannot be sold on day 0
can only be sold in the following days.

EXAMPLE:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

AL:
for each price we need to figure out the mximum possible profit we can earn
store the profit in a variable, update the variable if there is a higher profit
return the variable at the end
If not possible to earn profit, return 0

PSEUDO CODE:
Iterate over the prices array
on each iteration, get the positive diff between current price and the min of the following prices
store the positive diff in the profit variable
update the variable if on any iteration profit is higher
reurn the profit variable at the end
profit variable be by default zero
=end

def max_profit_old(prices)
  profit = 0
  prices.each_with_index do |price, idx|
    possible_max_profit = prices[idx..-1].max - price 
    profit = possible_max_profit if possible_max_profit > profit
  end

  profit
end



# The above solution works but it is exceeding the time limit on leetcode.
# So we need to find a time efficient solution
# So we iterate over the array, and on each iteration we can save the price
# into a hash, that would be the previous possible prices
# and each current price, gets compared to the previous possible prices and we compute the max profit possible
# if its higher than the profit at previous price we can update the profit

def max_profit(prices)
  profit = 0
  prev_possible_buys = []

  prices.each do |price|
    if prev_possible_buys.size > 0 && (price - prev_possible_buys.min > profit)
      profit = price - prev_possible_buys.min
    end

    prev_possible_buys << price
  end

  profit
end

puts max_profit([7,1,5,3,6,4])
puts max_profit([7,6,4,3,1])

# same again, it's not fast engouh