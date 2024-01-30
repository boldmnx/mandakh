from Stack import Stack

s = Stack()
s.push('A')
s.push('b')
s.push('C')
print(s.getItems())
print(f'pop: {s.pop()}')

print(f'top: {s.top()}')
print(f'bot: {s.bottom()}')

print(f'lenn: {s.lenn()}')
print(f'isEmpty: {s.is_empty()}')
