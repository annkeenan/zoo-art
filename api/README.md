# Format of Database

### Notes

- [variable] - substitute for the variable
- {} = dictionary
- () = set

### Classification

```
{
  [family]: {
    'Order': [order],
    'Class': [class],
    'Phylum': [phylum],
    'Kingdom': [kingdom],
    'Description': [description],
  },
  ...
}
```

### Exhibit

```
{
  [zoo name]: ([species], [species], ...),
  ...
}
```

### Habitat

```
{
  [habitat]: [description],
  ...
}
```

### Region

```
{
  [region]: [description],
  ...
}
```

### Species

```
{
  [species]: {
    'Common Name': [common name],
    'Genus': [genus],
    'Family': [family],
    'Region': [region],
    'Habitat': [habitat],
    'Status': [status],
  },
  ...
}
```

### State

```
{
  [abbreviation]: [state],
  ...
}
```

### Status

```
{
  [level]: {
    'Status': [status],
    'Description': [description]
  },
  ...
}
```

### Zoo

```
{
  [zoo name]: {
    'City': [city],
    'State': [state],
    'Address': [address],
    'Number of Animals': [number of animals],
    'Acres': [acres],
    'Opening Time': [opening time],
    'Closing Time': [closing time].
    'Annual Visitors': [annual visitors],
    'Website URL': [website url],
  },
  ...
}
```
