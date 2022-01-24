"""
* Assignment: OOP Method Nested
* Required: yes
* Complexity: medium
* Lines of code: 17 lines
* Time: 13 min

English:
    1. Define class `Iris`
    2. `Iris` has:
        a. "Sepal length" type `float`
        b. "Sepal width" type `float`
        c. "Petal length" type `float`
        d. "Petal width" type `float`
        e. "Species" type `str`
    3. `Iris` can:
        a. Return number of `float` type attributes
        b. Return list of all `float` type attributes
        c. Return sum of values of all `float` type attributes
        d. Return mean of all `float` type attributes
    4. Use `vars(self)` iteration to return values of numeric fields
    5. Create `setosa` object with attributes set at the initialization
    6. Create `virginica` object with attributes set at the initialization
    7. Method `.show()` returns sum, mean and species name, example:
       a. 'total=10.20 mean=2.55 setosa'
       b. 'total=15.50 mean=3.88 virginica'
    8. Do not use `@dataclass`
    9. Run doctests - all must succeed

Polish:
    1. Zdefiniuj klasę `Iris`
    2. `Iris` ma:
        a. "Sepal length" typu `float`
        b. "Sepal width" typu `float`
        c. "Petal length" typu `float`
        d. "Petal width" typu `float`
        e. "Species" typu `str`
    3. `Iris` może:
        a. Zwrócić liczbę pól typu `float`
        b. Zwrócić listę wartości wszystkich pól typu `float`
        c. Zwrócić sumę wartości pól typu `float`
        d. Zwrócić średnią arytmetyczną wartość pól typu `float`
    4. Użyj iterowania po `vars(self)` do zwrócenia wartości pól numerycznych
    7. Method `.show()` returns sumę, średnią oraz nazwę gatunku, przykład:
       a. 'total=10.20 mean=2.55 setosa'
       b. 'total=15.50 mean=3.88 virginica'
    8. Nie używaj `@dataclass`
    9. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `type(value) is float`
    * `vars(self).values()`
    * `{total=:.2f}`
    * `{mean=:.2f}`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> setosa = Iris(5.1, 3.5, 1.4, 0.2, 'setosa')
    >>> virginica = Iris(5.8, 2.7, 5.1, 1.9, 'virginica')

    >>> setosa.show()
    'total=10.20 mean=2.55 setosa'
    >>> virginica.show()
    'total=15.50 mean=3.88 virginica'
"""


class Iris:
    def __init__(self, sepal_length, sepal_width,
                 petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

    def get_numeric_values(self):
        return [x for x in vars(self).values() if type(x) is float]


