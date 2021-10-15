# rule-based-method-identifying-significant-weight-gain-factors

First of all, the patients and visit level data from Atheana health aggregated and all the data one-hot encoded. For privacy issue, the data is omitted from the repository.


To apply subgroup discovery method to generate rules in two levels of medication(low-level) and visit(high-level) in the [main.py](main.py)
we can select one of the arrays (high-level or low-level) and run the code. In this step, rules are generated and a WRAcc score assign to each of them. This process runs in an experimental analysis setting with 9 different variables (containing different width for the beam search and maximum number of features in each rule).
