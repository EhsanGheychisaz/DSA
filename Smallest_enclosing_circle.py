# Given an array arr[][] containing N points in a 2-D plane with integer coordinates. The task is to find the centre and the radius of the minimum enclosing circle(MEC)
# Python3 program to find the minimum enclosing
# circle for N integer points in a 2-D plane
from math import sqrt

# Defining infinity
INF = 10**18

# Function to return the euclidean distance
# between two points
def dist(a, b):
	return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

# Function to check whether a point lies inside
# or on the boundaries of the circle
def is_inside(c, p):
	return dist(c[0], p) <= c[1]

# The following two functions are the functions used
# To find the equation of the circle when three
# points are given.

# Helper method to get a circle defined by 3 points
def get_circle_center(bx, by, cx, cy):
	B = bx * bx + by * by
	C = cx * cx + cy * cy
	D = bx * cy - by * cx
	return [(cy * B - by * C) // (2 * D),
			(bx * C - cx * B) // (2 * D) ]

# Function to return a unique circle that intersects
# three points
def circle_frOm(A, B,C):
	I = get_circle_center(B[0] - A[0], B[1] - A[1],
								C[0] - A[0], C[1] - A[1])
	I[0] += A[0]
	I[1] += A[1]
	return [I, dist(I, A)]

# Function to return the smallest circle
# that intersects 2 points
def circle_from(A, B):
	
	# Set the center to be the midpoint of A and B
	C = [ (A[0] + B[0]) / 2.0, (A[1] + B[1]) / 2.0]

	# Set the radius to be half the distance AB
	return [C, dist(A, B) / 2.0]

# Function to check whether a circle encloses the given points
def is_valid_circle(c, P):

	# Iterating through all the points to check
	# whether the points lie inside the circle or not
	for p in P:
		if (is_inside(c, p) == False):
			return False
	return True

# Function to return find the minimum enclosing
# circle from the given set of points
def minimum_enclosing_circle(P):

	# To find the number of points
	n = len(P)

	if (n == 0):
		return [[0, 0], 0]
	if (n == 1):
		return [P[0], 0]

	# Set initial MEC to have infinity radius
	mec = [[0, 0], INF]

	# Go over all pair of points
	for i in range(n):
		for j in range(i + 1, n):

			# Get the smallest circle that
			# intersects P[i] and P[j]
			tmp = circle_from(P[i], P[j])

			# Update MEC if tmp encloses all points
			# and has a smaller radius
			if (tmp[1] < mec[1] and is_valid_circle(tmp, P)):
				mec = tmp

	# Go over all triples of points
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j + 1, n):

				# Get the circle that intersects P[i], P[j], P[k]
				tmp = circle_frOm(P[i], P[j], P[k])

				# Update MEC if tmp encloses all points
				# and has smaller radius
				if (tmp[1] < mec[1] and is_valid_circle(tmp, P)):
					mec = tmp

	return mec

# Driver code

mec = minimum_enclosing_circle([ [ 0, 0 ],
								[ 0, 1 ],
								[ 1, 0 ] ])

print("Center = { ",mec[0][1],",",mec[0][1],
				"} Radius = ",round(mec[1],6))

mec2 = minimum_enclosing_circle([ [ 5, -2 ],
								[ -3, -2 ],
								[ -2, 5 ],
								[ 1, 6 ],
								[ 0, 2 ] ])

print("Center = {",mec2[0][0],",",mec2[0][1],
		"} Radius = ",mec2[1])
		
# This code is contributed by mohit kumar 29
