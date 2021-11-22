"""
Program: inverstmentGUI.py
Author: Peter Rand 11/10/21
*** Note: The file breezypythongui.py MUST be in the same directory as the file in order for the application to work.***
"""

from breezypythongui import EasyFrame

class TextAreaDemo(EasyFrame):
	"""An Investment calculator that demonstrates the use of a multiline textarea widget"""

	def __init__(self):
		"""sets up the windows and the widgets"""
		EasyFrame.__init__(self, title = "Investment Calculator")
		self.addLabel(text = "Initial Ammount", row = 0, column = 0, background = "DarkSeaGreen")
		self.addLabel(text = "Number of Years", row = 1, column = 0, background = "DarkSeaGreen")
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0, background = "DarkSeaGreen")
		self.ammount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		#change that button color!
		self.button["background"] = "limegreen"
		self.outputArea["background"] = "white"
		self["background"] = "DarkSeaGreen"

	# Event handling method
	def compute(self):
		"""Computes the investment schedule based on the imputs and the outputs of the full report"""
		# obtain and validate the inputs
		startBalance = self.ammount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber()

		# If any of these inputs are zero, just exit the function
		if startBalance == 0 or years == 0 or rate == 0:
			self.outputArea["state"] = "normal"
			self.outputArea.setText("Please make sure that no inputs \ncontain a ZERO!")
			self.outputArea["state"] = "disabled"
			return
			#ends the function of the if - if applicable

		#Calculation phase
		#Convert the rate to a decimal number
		rate = rate / 100

		# Initialize the accumulator for the interest
		totalInterest = 0.0

		# Display the header for the table in tabular notation
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting balance", "Interest", "Ending balance")

		# Commute and append the results for each year
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest
			#end of for loop

		# Append the totals to the result string for the entire report
		result += "Ending balance: $%0.2f\n" % (endBalance)
		result += "Total interest earned: $%0.2f\n" % totalInterest

		#Output the result while preserving read-only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"


#definition of the main()function for program entry
def main():
	"""Instantiation and pops up the window."""
	TextAreaDemo().mainloop()

# global call to trigger the main()function
if __name__	== "__main__":
	main()