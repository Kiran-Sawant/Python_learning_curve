import finplot as fplt
import numpy as np
import pandas as pd

# Creating a randon Datetime index for x-axes.
dates = pd.date_range('01:00', '01:00:01.200', freq='1ms')

# Creating a random price Series for y-axes
prices = pd.Series(np.random.random(len(dates))).rolling(30).mean() + 4

# plotting a line
fplt.plot(dates, prices, legend='Nonscence')

# Drawing a interactive line
line = fplt.add_line((dates[100], 4.4), (dates[1100], 4.6), color='#9900ff', interactive=True)
# removing the interactive line
# fplt.remove_line(line)

# adding an immovable text.
text = fplt.add_text(pos=(dates[50], 4.4), s="I'm here alright!", color='#bb7700')
# removing the immovable text.
# fplt.remove_text(text)

# displaying the plot
fplt.show()