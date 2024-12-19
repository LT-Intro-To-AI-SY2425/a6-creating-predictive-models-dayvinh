# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
    The model isn't as accurate because the data wasn't scaled leading to skewed data, overall decreasing the model's accuracy.
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
    The model is quite accurate with a value of 0.78, seeing that it predicts correctly almost every time and has a value close to 1.0.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
    The model was correct with its predictions the majority of the cases. There wasn't any apparrent pattern as the model wrongly predicted both Male and Female at times.
4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
According to the model, she wouldn't buy an SUV.

