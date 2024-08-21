import seaborn as sns

from matplotlib import pyplot as plt


u = [0,0,1,6]
v = [0,0,4,2]
u_bis = [1,6,v[2],v[3]]
w = [0,0,5,8]
plt.quiver([u[0], u_bis[0], w[0]],
           [u[1], u_bis[1], w[1]],
           [u[2], u_bis[2], w[2]],
           [u[3], u_bis[3], w[3]],
           angles='xy', scale_units='xy', scale=1, color=sns.color_palette())
# plt.rc('text', usetex=True)
plt.xlim(-2, 6)
plt.ylim(-2, 9)
plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')

plt.text(-1, 3.5, r'$||\vec{u}||$', color=sns.color_palette()[0], size=20)
plt.text(2.5, 7.5, r'$||\vec{v}||$', color=sns.color_palette()[1], size=20)
plt.text(2, 2, r'$||\vec{u}+\vec{v}||$', color=sns.color_palette()[2], size=20)

plt.show()
plt.close()


'''



1. `u = [0, 0, 1, 6]`: Defines a vector `u` with elements [0, 0, 1, 6].

2. `v = [0, 0, 4, 2]`: This line seems to have a typo. It should be `v = [0, 0, 4, 2]`, defining a vector `v` with elements [0, 0, 4, 2].

3. `u_bis = [1, 6, v[2], v[3]]`: Defines a vector `u_bis` by combining elements from `u` and `v`. The first two elements are from `u`, and the last two elements are from `v`.

4. `w = [0, 0, 5, 8]`: Defines a vector `w` with elements [0, 0, 5, 8].

5. `plt.quiver([u[0], u_bis[0], w[0]],`: Plots the x-coordinates of vectors `u`, `u_bis`, and `w`.

6. `           [u[1], u_bis[1], w[1]],`: Plots the y-coordinates of vectors `u`, `u_bis`, and `w`.

7. `           [u[2], u_bis[2], w[2]],`: Plots the x-components of vectors `u`, `u_bis`, and `w`.

8. `           [u[3], u_bis[3], w[3]],`: Plots the y-components of vectors `u`, `u_bis`, and `w`.

9. `           angles='xy', scale_units='xy', scale=1, color=sns.color_palette())`: Sets the properties for the quiver plot, such as angles, scale units, scale, and color.

10. `plt.xlim(-2, 6)`: Sets the x-axis limits of the plot from -2 to 6.

11. `plt.ylim(-2, 9)`: Sets the y-axis limits of the plot from -2 to 9.

12. `plt.axvline(x=0, color='grey')`: Adds a vertical line at x=0 with a grey color.

13. `plt.axhline(y=0, color='grey')`: Adds a horizontal line at y=0 with a grey color.

14. `plt.text(-1, 3.5, r'$||\vec{u}||", color=sns.color_palette()[0], size=20)`: Adds text at coordinates (-1, 3.5) to label the magnitude of vector `u`.

15. `plt.text(2.5, 7.5, r'$||\vec{v}||", color=sns.color_palette()[1], size=20)`: Adds text at coordinates (2.5, 7.5) to label the magnitude of vector `v`.

16. `plt.text(2, 2, r'$||\vec{u}+\vec{v}||", color=sns.color_palette()[2], size=20)`: Adds text at coordinates (2, 2) to label the magnitude of the sum of vectors `u` and `v`.

17. `plt.show()`: Displays the plot.

18. `plt.close()`: Closes the plot window.


'''