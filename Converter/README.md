# Measurement Converter (Standards)

### Using as executable

- f2m -> feet to meters
- m2f -> meters to feets

```
mv converter.py converter; chmod +x converter

./convert f2m 1
./convert m2f 0.3
```

### Importing as library

```python
import converter as c

x = 3.0
y = ["x isn't large","x is large"][c.m2f(x)>=10.0]
print(y+" -> {feet:.3f}ft".format(feet=c.m2f(x)))
```