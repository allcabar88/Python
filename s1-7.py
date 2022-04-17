#7.	Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
for i in range(2):
    for j in range(2):
        for k in range(2):
            boolean = ~(i or j or k) == (~i and ~j and ~k)
            print('¬({0}⋁{1}⋁{2})=¬{0}⋀¬{1}⋀¬{2}', i, j, k, boolean)