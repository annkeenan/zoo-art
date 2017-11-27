# API

## Use

### Classification

The classification holds the classification of a family, the Order, Class,
Phylum, Kingdom, and Description. The programmer has the load and get methods.

### Exhibit

The Exhibit database holds the Zoo Names, which are references for the Zoo
database, and the Species, which are references for the Species database. The
programmer has the load, post, delete, and get methods.

### Habitat

The Habitat database holds the habitats and a description of the habitats.
The programmer has the load and get methods.

### Region

The Region database holds the regions and a description of the regions. The
programmer has the load and get methods.

### Species

The Species database holds the Species and its Common Names, Genus, Family
(references for the Classification database), Region (references for the
Region database), Habitat (references for the Habitat database), and Status
(reference for the Status database). The programmer has the load, put, post,
and get methods.

### State

The State database holds the Abbreviation and full name for each State. The
programmer has the load and get methods.

### Status

The Status database holds all classifications by the International Union for
Conservation of Nature Red List as described by Status and their
corresponding Level number and description. The programmer has the load and
get methods, with one get method returning a list of all statuses in order of
severity and the other getting the description of a specified status.

### Zoo

The Zoo database stores the Zoo Names and their City, State (reference to the
State database), Address, Number of Animals, Acres, Opening Time, Closing
Time, Annual Visitors, and Website URL. The programmer has the load, put,
post, and get methods.

## Format

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
    'Desc': ([name], [name], ...)
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
    'Common Name': ([common name], [common name], ...),
    'Genus': [genus],
    'Family': [family],
    'Region': [region],
    'Habitat': [habitat],
    'Status': [status]
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
  [status]: {
    'Level': [level],
    'Desc': [description]
  },
  ...
}
```

### Zoo

```
{
  [zoo name]: {
    'City': [city],
    'State': [state abbreviation],
    'Address': [address],
    'Number of Animals': [number of animals],
    'Acres': [acres],
    'Opening Time': [opening time],
    'Closing Time': [closing time].
    'Annual Visitors': [annual visitors],
    'Website URL': [website url]
  },
  ...
}
```
