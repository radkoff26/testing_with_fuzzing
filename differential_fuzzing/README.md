## Differential fuzzing

This section represents differential type of fuzzing-testing.

Here are two implementations of the described type of fuzzing:

- `contracts`: this implementaion includes specification of contracts which functionality must obey. In the given example contracts are represented by keyword `assert` which forces program to throw error unless contract is satisfied;

- `exceptions`: this implementation bases on throwing particular error in case when outputs of different functionality implementations (libraries) are mismatched.
