# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE SalesPerson.name NOT IN (SELECT name 
                               FROM SalesPerson JOIN Orders
                               ON SalesPerson.sales_id = Orders.sales_id
                               WHERE Orders.com_id NOT IN (SELECT Orders.com_id
                                                           FROM Orders JOIN Company
                                                           ON Orders.com_id = Company.com_id
                                                           WHERE Company.name != "RED"
                                                           )
                               )