# Solve-Traffic-On-Networks

"""WHAT DOES IT TO""" ----> This program helps us to examine all the paths between two nodes for all the sub-graphs, get their Nash equilibrium when the traffic is balanced and calculates the optimal time of all possible paths between two nodes then return the best sub-graph and tell you which edges harmful to be optimal (based on braess's paradox).

"""PREREQUISITES""" ---> We are using braess's paradox, dynamic best-respone and following article https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch08.pdf by "David Easley and Jon Kleinberg" which is modeling the traffic with game theory. So it is necessary to read about basic game theory and those contents.

"""SAMPLES""" ---> There are samples for each code at the end of the code. Always check them even if you completely understand how codes work :)

"""NOTE""" ---> We considered the time function of each edge to be linear (ax + b) and when  we say {"ab":[a, b]} it means for edge which goes from a to b, we have "ax + b" this linear function which x is number of drivers in the edge !!!

To run the project just open the main.py and give it your example (you can check the sample input at end of each code!!!)

If you have any ideas or criticism to improve the code, be sure to share with us. samanarzaghi@ut.ac.ir rayanforsat@ut.ac.ir "School of Mathematics, Statistics and Computer Science College of Science, University of Tehran."
