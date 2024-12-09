# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?

What makes this model more effective is that it tests the line of best fit on data that isn't yet determined and sees whether if the line is accurate to the data or not, compared to Part 1 where the model simply creates a line of best fit based on the data without first creating a prediction.

2. What does the R squared coefficient tell you about the model?

The R squared coefficient determines whehther or not the line of best fit correlates with the data set. With a number closer to 0.99, a stronger correlation is suggested while a coefficient closer to 0.0 indicates a weaker correlation.


3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.

I would say that my model is somewhat accurate as someimes its prdictions can be quite close to the acutual value while other times it can be quite off. Through running the model 3 times, it brought up a r squared coefficient of 0.45, 0.65, 0.72. This indicates that the model can be a hit or miss when it comes to getting a highly correlated line of best fit with the data set. However, according to the AHA's website chart, the model isn't very reliable if it comes to identifying blood pressure categories because predictions made by the model are off enough from the actual values to incorrectly identify someone's blood pressure category.