Topic: Association Rule Learning

Mission: Market basket optimization

Model: Apriori

Note:
- support(X) = num of records containing X / total number of records
- confidence(I_1->I_2) = num of records containing I_1 and I_2 / total number of records containing I_1
- lift(I_1->I_2) = confidence (I_1->I_2) / support(I_2)

Idea:
1. set a min. support and confidence
2. take all the subsets in transactions having higher suport than min. support
3. take all the rules of these subsets having higher confidence than min. confidence
4. sort the rules by decreasing lift
