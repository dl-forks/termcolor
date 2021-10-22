## Example

```python
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
```

## Text Properties

### Text colors:

- grey
- red
- green
- yellow
- blue
- magenta
- cyan
- white

### Text highlights:

- on_grey
- on_red
- on_green
- on_yellow
- on_blue
- on_magenta
- on_cyan
- on_white

### Attributes:

- bold
- dark
- underline
- blink
- reverse
- concealed

## Terminal properties

| Terminal      | bold    | dark  | underline | blink      | reverse | concealed |
| ------------- | ------- | ----- | --------- | ---------- | ------- | --------- |
| xterm         | 🟢 yes  | ❌ no  | 🟢 yes     | bold       | 🟢 yes  | 🟢 yes    |
| linux         | 🟢 yes  | 🟢 yes | bold      | 🟢 yes      | 🟢 yes  | ❌ no     |
| rxvt          | 🟢 yes  | ❌ no  | 🟢 yes     | bold/black | 🟢 yes  | ❌ no     |
| dtterm        | 🟢 yes  | 🟢 yes | 🟢 yes     | reverse    | 🟢 yes  | 🟢 yes   |
| teraterm      | reverse | ❌ no  | 🟢 yes     | rev/red    | 🟢 yes   | ❌ no     |
| aixterm       | normal  | ❌ no  | 🟢 yes     | ❌ no        | 🟢 yes   | 🟢 yes  |
| PuTTY         | color   | ❌ no  | 🟢 yes     | ❌ no       | 🟢 yes    | ❌ no   |
| Windows       | ❌ no    | ❌ no  | ❌ no      | ❌ no       | 🟢 yes    | ❌ no    |
| Cygwin SSH    | 🟢 yes  | ❌ no  | color      | color      | color     | 🟢 yes  |
| Mac Terminal  | 🟢 yes  | ❌ no  | 🟢 yes     | 🟢 yes     | 🟢 yes    | 🟢 yes  |

## Changes
  
#### 1.1.0 (13.01.2011)

- Added cprint function.
        
#### 1.0.1 (13.01.2011)

- Updated README.rst.
        
#### 1.0.0 (13.01.2011)
        
- Changed license to MIT.
- Updated copyright.
- Refactored source code.
        
#### 0.2 (07.09.2010)
        
- Added support of Python 3.x.
        
#### 0.1.2 (04.06.2009)
       
- Fixed bold characters. (Thanks Tibor Fekete)
        
#### 0.1.1 (05.03.2009)
        
- Some refactoring.
- Updated copyright.
- Fixed reset colors.
- Updated documentation.
        
#### 0.1 (09.06.2008)

- Initial release.
        
