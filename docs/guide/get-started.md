# Getting started
This section will help you a basic **Cornelius** documentation for ground up.

:::info
cornelius is currently in `v0.0.3` there is a possibility that there are bugs or some error within this version, you can report any bug or problem to cornelius developers.
:::

## Step 1: Create a new proyect.
Create your directory and into the new directory created.
```sh
mkdir py-project && cd py-project
```

## Step 2: Importing cornelius to our project.
Install cornelius using the **python package manager** also known as `pip`
```sh
pip install cornelius
```

## Step 3: Verifing if cornelius works.
Create a `.py` file and inside the file import the cornelius module.
```python
import cornelius
```
Also, you can import cornelius classes like this
```python{1}
from cornelius import Cursor
cursor = Cursor()
```
As you can see, we imported _`Cursor`_ class using traditional module importation and
we created a variable called _`cursor`_ calling the class _`Cursor()`_

Any doubt? contact the development team of cornelius.