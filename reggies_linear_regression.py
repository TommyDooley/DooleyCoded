#m = slope value
#b = intercept value
#x = x point on graph
#y = y point on graph

def get_y(m, b, x):
  y = m * x + b
  return y

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    return abs(get_y(m,b,x_point) -  y_point)

print(f"The error of the equation is: {calculate_error(0, 9, (7, 0))}")
print(f"The error of the equation is: {calculate_error(2, 10, (0, 3))}")
print(f"The error of the equation is: {calculate_error(4, 11, (10, 3))}")


#datapoints (how big the ball is, how high it bounced)
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def calculate_all_error(m, b, datapoints):
    total_error = 0
    for point in datapoints:
        calculate_error(m, b, point)
        total_error = total_error + calculate_error(m, b, point)
    return total_error

print(f"The total error is: {calculate_all_error(1, 0, datapoints)}")
print(f"The total error is: {calculate_all_error(5, 10, datapoints)}")
print(f"The total error is: {calculate_all_error(20, 500, datapoints)}")


possible_ms = m=[-10 + 0.1 * x for x in range(int((10-(-10))/0.1)+1)]
possible_bs = b=[-10 + 0.1 * x for x in range(int((20-(-20))/0.1)+1)]

smallest_error = float("inf")
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        if calculate_all_error(m, b, datapoints) < smallest_error:
            m = best_m
            b = best_b
            smallest_error = calculate_all_error(m, b, datapoints)

print (f"The best m is {best_m}, the best b is {best_b}, and the smallest error is {smallest_error}")

print(f"The bouncing ball model predicts that the ball will bounce: {(get_y(0.3, 1.7, 6))} meters!")